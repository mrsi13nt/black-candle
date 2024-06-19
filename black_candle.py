#!/usr/bin/python3
import requests
import sys
import time
import os
import argparse
from configs.function import *
from configs.logo import *
from configs.config import *
import webbrowser

def main():
    usage = "usage: python3 black_candle.py [options] arg"
    parser = argparse.ArgumentParser(
                    prog='black candle',
                    description=logo_menu,formatter_class=argparse.RawTextHelpFormatter,
                    epilog=examples_help,
                    usage='%(prog)s -u URL')
    sql_group = parser.add_argument_group('SQL')
    sql_group.add_argument('-sql', dest='sql', action='store_true', help='run sql scanner')
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
    output_group.add_argument('-r', dest='output', action='store_true', help='full report for all the scanning')
    parser.add_argument('-u', '--url', dest='url', action='store', metavar='URL', help='Target URL (e.g. "http://www.site.com/vuln.php?id=1")')
    parser.add_argument('-help', action='store_true', dest='web', help="for more info and tips")
    args = parser.parse_args()

    # Check if URL is provided
    if not args.url and not args.web:
        slowprint("[\033[31mError\033[0m] -u/--url option is required.")
        parser.print_help()
        sys.exit(1)

    if args.web:
        webbrowser.open("how_to_use_me.html")
        return

    # Print the random logo
    random_logo()

    # Handle SQL scanning
    if args.sql:
        url = args.url
        params = args.data if args.data else {}
        payloads = [args.payload] if args.payload else []
        output_s = args.output if args.output else False
        sqli_scan(url, params, payloads, output_s)

    # Handle Host Header Injection
    if args.hhi:
        url = args.url
        host = args.host if args.host else None
        hhi(url, host)

    # Handle JavaScript scanning
    if args.js:
        url = args.url
        js_scanner(url)

    # Handle Reflected XSS scanning
    if args.reflected:
        url = args.url
        output_s = args.output if args.output else False
        scanner = ReflectedXSSScanner(url, [], output_s)
        try:
            scanner.crawl_and_scan()
        except KeyboardInterrupt:
            if asking():
                random_logo()
                scanner.crawl_and_scan()
            else:
                sys.exit()

    # Handle DOM XSS scanning
    if args.dom:
        url = args.url
        output_s = args.output if args.output else False
        scanner = DOMXSSScanner(url, [], output_s)
        try:
            scanner.crawl_and_scan()
        except KeyboardInterrupt:
            if asking():
                random_logo()
                scanner.crawl_and_scan()
            else:
                sys.exit()

    # Handle Blind XSS scanning
    if args.blind:
        url = args.url
        output_s = args.output if args.output else False
        scanner = BlindXSSScanner(url, [], output_s)
        try:
            scanner.crawl_and_scan()
        except KeyboardInterrupt:
            if asking():
                random_logo()
                scanner.crawl_and_scan()
            else:
                sys.exit()





if __name__ == '__main__':
    update()
    main()
