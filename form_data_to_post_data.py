#!/usr/local/bin/python3

import argparse
from urllib.parse import urlencode

parser = argparse.ArgumentParser()
parser.add_argument('--form_data_file', required=True)
parser.add_argument('--ticker', required=True)
parser.add_argument('--post_data_file', required=True)
args = parser.parse_args()

m = dict()
m['__EVENTTARGET'] = ''
m['__EVENTARGUMENT'] = ''
m['ctl00$ctl00$AllContent$ucHeader$ucCBOEHeaderQuoteBox$txtHeaderQuote'] = (
    'Quote')
m['ctl00$ctl00$AllContent$ucHeader$CBOEHeaderSearchBox$txtHeaderSearch'] = (
    'Search')
m['ctl00$ctl00$AllContent$ContentMain$QuoteTableDownloadCtl1$txtTicker'] = (
    args.ticker)
m['ctl00$ctl00$AllContent$ContentMain$QuoteTableDownloadCtl1$cmdSubmit'] = (
    'Download')

with open(args.form_data_file, 'r') as fp:
  lines = fp.read().splitlines()
assert len(lines) == 2
m['__EVENTVALIDATION'] = lines[0]
m['__VIEWSTATE'] = lines[1]

post_data = urlencode(m)
with open(args.post_data_file, 'w') as fp:
  print(post_data, file=fp)

