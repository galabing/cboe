#!/usr/local/bin/python3

import os
import subprocess

post_data_file = '/tmp/download_option_quotes_post_data.txt'
s = os.stat(post_data_file)
content_length = s.st_size

p = subprocess.Popen(['./wget1.sh', str(content_length)],
                     stdout=subprocess.PIPE)
text = p.stdout.read().decode('utf-8')
retcode = p.wait()
print('DEBUG: return code is %d' % retcode)
#assert retcode == 8

query_data = None
for line in text.splitlines():
  #print('DEBUG: %s' % line)
  assert not line.startswith('  Set-Cookie: DownLoadError=Symbol Not Found.')
  if line.startswith('  Set-Cookie: QueryData='):
    query_data = line[14:line.find(';')]
assert query_data is not None
assert len(query_data) > len('QueryData=')

p = subprocess.Popen(['./wget2.sh', query_data], stdout=subprocess.PIPE)
text = p.stdout.read().decode('utf-8')
retcode = p.wait()
print('DEBUG: return code is %d' % retcode)

for line in text.splitlines():
  assert not line.startswith('  Set-Cookie: DownLoadError=Symbol Not Found.')

