#!/bin/sh

CONTENT_LENGTH=$1

wget --post-file=/tmp/download_option_quotes_post_data.txt\
 https://www.cboe.com/DelayedQuote/QuoteTableDownload.aspx\
 --header='Host: www.cboe.com'\
 --header='Connection: keep-alive'\
 --header="Content-Length: $CONTENT_LENGTH"\
 --header='Cache-Control: max-age=0'\
 --header='Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'\
 --header='Origin: https://www.cboe.com'\
 --header='User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36'\
 --header='Content-Type: application/x-www-form-urlencoded'\
 --header='Referer: https://www.cboe.com/DelayedQuote/QuoteTableDownload.aspx'\
 --header='Accept-Encoding: gzip,deflate,sdch'\
 --header='Accept-Language: en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'\
 --header='Cookie: CBOEMobileCookie=False; __utma=91891016.89552075.1380094251.1380333083.1380401308.14; __utmb=91891016.3.10.1380401308; __utmc=91891016; __utmz=91891016.1380401308.14.13.utmcsr=cboe.com|utmccn=(referral)|utmcmd=referral|utmcct=/DelayedQuote/QuoteTableDownload.aspx'\
 --server-response\
 --max-redirect=0\
 2>&1

