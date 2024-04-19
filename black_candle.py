import requests
import sys
import time
import os
import argparse
from function import *
from logo import *
from config import *

def main():
    usage = "usage: python3 black_candle.py [options] arg"
    parser = argparse.ArgumentParser(
                    prog='black candle',
                    description='a simple sql scanner',
                    epilog='Text at the bottom of help',
                    usage='%(prog)s -u URL')
    sql_group = parser.add_argument_group('SQL')
    sql_group.add_argument('--data', dest='data', metavar='"data"', help='Data string to be sent through POST (e.g. "id=1")')
    sql_group.add_argument('-p','--payload', dest='payload', metavar='payload', help='you can add custom payload' )
    hhi_group = parser.add_argument_group('Host Header Injection')
    hhi_group.add_argument('-hh', dest='hhi',action='store_true' ,help='run host header injection scanner')
    hhi_group.add_argument('--host', dest='host', metavar='Host', help='add custom host header (e.g. --host "www.ping.com")')
    js_group = parser.add_argument_group('JS scan')
    js_group.add_argument('-js', dest='js', action='store_true' ,help='scan all java script files of full website from api keys and more..')
    xss_group = parser.add_argument_group('XSS')
    xss_group.add_argument('-rf', dest='reflected', action='store_true', help='scan for reflected XSS')
    xss_group.add_argument('-d', dest='dom', action='store_true', help='scan for DOM XSS')
    xss_group.add_argument('-b', dest='blind',action='store_true' ,help='scan for blind xss')
    output_group = parser.add_argument_group('Output')
    output_group.add_argument('-o', dest='output', metavar='string', type=argparse.FileType('w', encoding='latin-1'), help='file to write output to') #x
    parser.add_argument('-u', '--url', dest='url', action='store', metavar='URL', help='Target URL (e.g. "http://www.site.com/vuln.php?id=1")')
    args = parser.parse_args()

    # check the target url or list
    if not args.url:
        print("[\033[31mError\033[0m] Either -u/--url or -l/--list option is required.")
        parser.print_help()
        sys.exit(1)

# ======== SQL =========        
    if args.url and args.data:
        random_logo()
        url = args.url
        data = args.data
        sqli_scan(url,data,payloads)
    elif args.url and args.payload:
        random_logo()
        url = args.url
        payload = args.payload
        sqli_scan(url,params,payload)
    elif args.url and args.data and args.payload:
        random_logo()
        url = args.url
        payload = args.payload
        data = args.Data
        sqli_scan(url,data,payload)
# ======== Host Header Injection =========
    elif args.hhi and args.url:
        random_logo()
        hhi(args.url,None)
    elif args.hhi and args.host and args.url:
        random_logo()
        hhi(args.url, args.host)
# ======== Scan Java Script Files =========
    elif args.js:
        random_logo()
        js_scanner(args.url)
# ======== Scan XSS =========
    elif args.reflected:
        random_logo()
        scanner = ReflectedXSSScanner(args.url,reflected_xss_payloads)
        scanner.crawl_and_scan()
    elif args.dom:
        random_logo()
        DOMXSSScanner(args.url,dom_based_xss_payloads)
        DOMXSSScanner.crawl_and_scan()
    elif args.blind:
        random_logo()
        BlindXSSScanner(args.url,blind_xss_payloads)
        BlindXSSScanner.crawl_and_scan()
    else:
        print("[\033[31mError\033[0m]")
        slowprint("please try again with true usage")
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
