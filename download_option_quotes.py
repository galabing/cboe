#!/usr/local/bin/python3

import argparse
import codecs
import os
import sys
import time

WGET = '/usr/local/bin/wget'
FD2PD = './form_data_to_post_data.py'
DLWRAPPER = './wget.py'

ASPX_URL = 'http://www.cboe.com/DelayedQuote/QuoteTableDownload.aspx'
TMP_ASPX_FILE = '/tmp/download_option_quotes_root_aspx.aspx'
TMP_FORM_DATA_FILE = '/tmp/download_option_quotes_form_data.txt'
TMP_POST_DATA_FILE = '/tmp/download_option_quotes_post_data.txt'
TMP_OUTPUT_FILE = '/tmp/download_option_quotes_output.csv'

SLEEP_SEC_DL = 5
SLEEP_SEC_TK = 10

def print_and_run(cmd):
  print('Executing command: %s' % cmd)
  sys.stdout.flush()
  return os.system('%s 2>&1' % cmd)

def download(url, output_file):
  if os.path.isfile(output_file):
    os.remove(output_file)
  cmd = '%s %s -q -O %s' % (WGET, url, output_file)
  assert print_and_run(cmd) == 0
  assert os.path.isfile(output_file)

def find_value(content, element_id):
  p = content.find('id="%s"' % element_id)
  assert p >= 0
  q = content.find('value="', p)
  assert q > p
  r = content.find('"', q+len('value="'))
  assert r > q
  return content[q+len('value="'):r]

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--ticker_file', required=True)
  parser.add_argument('--output_dir', required=True)
  parser.add_argument('--overwrite', action='store_true')
  args = parser.parse_args()

  with open(args.ticker_file, 'r') as fp:
    tickers = fp.read().splitlines()
  print('Processing %d tickers' % len(tickers))

  for i in range(len(tickers)):
    if i > 0:
      print('Sleeping for %.2f sec before next ticker' % SLEEP_SEC_TK)
      time.sleep(SLEEP_SEC_TK)

    ticker = tickers[i]
    print('%d/%d: %s' % (i+1, len(tickers), ticker))

    output_file = '%s/%s.csv' % (args.output_dir, ticker)
    if os.path.isfile(output_file):
      if not args.overwrite:
        print('Output file exists for %s, skipping' % ticker)
        continue
      os.remove(output_file)

    # Download the root aspx file, parse out __EVENTVALIDATION and __VIEWSTATE.
    download(ASPX_URL, TMP_ASPX_FILE)
    with open(TMP_ASPX_FILE, 'rb') as fp:
      content = fp.read().decode('utf-8', 'ignore')
    event_validation = find_value(content, '__EVENTVALIDATION')
    view_state = find_value(content, '__VIEWSTATE')
    #print('__EVENTVALIDATION: %s' % event_validation)
    #print('__VIEWSTATE: %s' % view_state)
    with open(TMP_FORM_DATA_FILE, 'w') as fp:
      print(event_validation, file=fp)
      print(view_state, file=fp)

    # Convert form data to post data.
    # Notice that '.' needs to be removed from ticker symbol for cboe.
    cmd = ('%s --form_data_file=%s --ticker=%s --post_data_file=%s'
           % (FD2PD, TMP_FORM_DATA_FILE, ticker.replace('.', ''),
              TMP_POST_DATA_FILE))
    assert print_and_run(cmd) == 0

    print('Sleeping for %.2f sec before download' % SLEEP_SEC_DL)
    time.sleep(SLEEP_SEC_DL)

    # Download quotes.
    cmd = '%s' % DLWRAPPER
    if print_and_run(cmd) != 0:
      print('Download of %s failed' % ticker)
    else:
      assert os.path.isfile(TMP_OUTPUT_FILE)
      os.rename(TMP_OUTPUT_FILE, output_file)

if __name__ == '__main__':
  main()

