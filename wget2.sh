#!/bin/sh

QUERY_DATA=$1
#QUERY_DATA='QueryData=3821821958DFD74E943DA5316B53CD7E1375776FB8B4D8E455E31A805389FBF324952B59F6363F19DC7EFF3A96DEA480AE7138C9C6D3D5489003B3A48F9A7AFD1D5F0F9A3CA746092C16F9998B231A51D3E180EF32E08F4428DC2E5F0ACE2926D725E62CEC8A2880EEA9C394308D641EEB65B16BABEC6D4BC3F7DDF3'

wget\
 https://www.cboe.com/DelayedQuote/QuoteData.dat\
 -O /tmp/download_option_quotes_output.csv\
 --header='Host: www.cboe.com'\
 --header='Connection: keep-alive'\
 --header='Cache-Control: max-age=0'\
 --header='Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'\
 --header='User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36'\
 --header='Referer: https://www.cboe.com/DelayedQuote/QuoteTableDownload.aspx'\
 --header='Accept-Encoding: gzip,deflate,sdch'\
 --header='Accept-Language: en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'\
 --header="Cookie: __utma=91891016.89552075.1380094251.1380238732.1380243172.11; __utmc=91891016; __utmz=91891016.1380243172.11.10.utmcsr=cboe.com|utmccn=(referral)|utmcmd=referral|utmcct=/DelayedQuote/QuoteTable.aspx; $QUERY_DATA"\
 --server-response\
 2>&1

