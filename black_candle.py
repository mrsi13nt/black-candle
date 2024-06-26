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
import socket


def check_network():
        try:
            # Try to resolve the hostname
            socket.gethostbyname("google.com")
            return True
        except socket.error:
            return False


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

    if args.web:
        # Open offline HTML file
        home_directory = os.path.expanduser('~')
        html_file_path = os.path.abspath(f"{home_directory}/.local/black_candle/how_to_use_me.html")
        webbrowser.open(f"file:///{html_file_path}")
        return
    

    if not check_network():
        print("[\033[31mError\033[0m] No network connection. Please check your internet connection and try again.")
        sys.exit(1)
    print("Network connection is available. Continuing with the program...")

    
    # Check if URL is provided
    if not args.url and not args.web:
        slowprint("[\033[31mError\033[0m] -u/--url option is required.")
        parser.print_help()
        sys.exit(1)

    

    # Print the random logo
    random_logo()

# ======== SQL =========        
    if args.url and args.sql:
        random_logo()
        url = args.url
        sqli_scan(url,params,payloads,output_s=False)
    elif args.url and args.sql and args.output:
        random_logo()
        url = args.url
        sqli_scan(url,params,payloads,output_s=True)
    elif args.url and args.payload and args.sql:
        random_logo()
        url = args.url
        payload = args.payload
        sqli_scan(url,params,payload,output_s=False)
    elif args.url and args.payload and args.sql and args.output:
        random_logo()
        url = args.url
        payload = args.payload
        sqli_scan(url,params,payload,output_s=True)
    elif args.url and args.data and args.sql:
        random_logo()


# ======== Host Header Injection =========
    if args.hhi and args.url:
        random_logo()
        hhi(args.url,None)
    elif args.hhi and args.url and args.output:
        random_logo()
        hhi(args.url,None)
    elif args.hhi and args.host and args.url:
        random_logo()
        hhi(args.url, args.host)
    elif args.hhi and args.host and args.url and args.output:
        random_logo()
        hhi(args.url, args.host)


    # Handle JavaScript scanning
    if args.js:
        print("Running JavaScript Scanner")
        url = args.url
        js_scanner(url)

# ======== Scan XSS =========
    elif args.reflected:
        random_logo()
        scanner = ReflectedXSSScanner(args.url,reflected_xss_payloads,output_s=False)
        try:
            scanner.crawl_and_scan()
        except KeyboardInterrupt:
            if asking():
                random_logo()
                scanner = ReflectedXSSScanner(args.url,reflected_xss_payloads,output_s=False)
                scanner.crawl_and_scan()
            else:
                sys.exit()
    elif args.reflected and args.output:
        random_logo()
        scanner = ReflectedXSSScanner(args.url,reflected_xss_payloads,output_s=True)

        try:
            scanner.crawl_and_scan()
        except KeyboardInterrupt:
            if asking():
                random_logo()
                scanner = ReflectedXSSScanner(args.url,reflected_xss_payloads,output_s=True)
                scanner.crawl_and_scan()
            else:
                sys.exit()


    if args.dom:
        random_logo()
        scanner = DOMXSSScanner(args.url,dom_based_xss_payloads,output_s=False)
        try:
            scanner.crawl_and_scan()
        except KeyboardInterrupt:
            if asking():
                random_logo()
                scanner = DOMXSSScanner(args.url,dom_based_xss_payloads,output_s=False)
                scanner.crawl_and_scan()
            else:
                sys.exit()
    elif args.dom and args.output:
        random_logo()
        scanner = DOMXSSScanner(args.url,dom_based_xss_payloads,output_s=True)
        try:
            scanner.crawl_and_scan()
        except KeyboardInterrupt:
            if asking():
                random_logo()
                scanner = DOMXSSScanner(args.url,dom_based_xss_payloads,output_s=True)
                scanner.crawl_and_scan()
            else:
                sys.exit()
    elif args.blind:
        random_logo()
        scanner = BlindXSSScanner(args.url,blind_xss_payloads,output_s=False)
        try:
            scanner.crawl_and_scan()
        except KeyboardInterrupt:
            if asking():
                random_logo()
                scanner = BlindXSSScanner(args.url,blind_xss_payloads,output_s=False)
                scanner.crawl_and_scan()
            else:
                sys.exit()
    if args.blind and args.output:
        random_logo()
        scanner = BlindXSSScanner(args.url,blind_xss_payloads,output_s=True)


    elif args.blind and args.output:
        random_logo()
        scanner = BlindXSSScanner(args.url,blind_xss_payloads,output_s=True)
        try:
            scanner.crawl_and_scan()
        except KeyboardInterrupt:
            if asking():
                random_logo()
                scanner = BlindXSSScanner(args.url,blind_xss_payloads,output_s=True)
                scanner.crawl_and_scan()
            else:
                sys.exit()
        
    else:
        print("[\033[31mError\033[0m]")
        slowprint("please try again with true usage")
        parser.print_help()
        sys.exit(1)

    





if __name__ == '__main__':
    #update()
    main()
