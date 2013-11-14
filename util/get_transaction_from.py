import urllib2
import cookielib
from pyquery import PyQuery

def get_transaction_from(transaction_id):
    cookies = cookielib.CookieJar()
    request = urllib2.Request('http://blockexplorer.com/testnet/tx/%s' % transaction_id)
    request.add_header('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
    html = opener.open(request).read()
    pq = PyQuery(html)
    try:
        return pq.find('.txtable td a')[5].text
    except Exception as e:
        return None

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print 'Expects 1 arg, a transaction id'
    else:
        print get_transaction_from(sys.argv[1])   
