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


    # Check if URL is provided
    if not args.url and not args.web:
        slowprint("[\033[31mError\033[0m] -u/--url option is required.")
        parser.print_help()
        sys.exit(1)

    
    if args.web:
        # Open offline HTML file
        home_directory = os.path.expanduser('~')
        html_file_path = os.path.abspath(f"{home_directory}/.local/black_candle/how_to_use_me.html")
        webbrowser.open(f"file:///{html_file_path}")
        return

    # Print the random logo
    random_logo()
    if not check_network():
        print("[\033[31mError\033[0m] No network connection. Please check your internet connection and try again.")
        sys.exit(1)
    print("Network connection is available. Continuing with the program...")

    # Handle SQL scanning
    if args.sql:
        print("Running SQL Scanner")
        url = args.url
        params = args.data if args.data else {}
        payloads = [args.payload] if args.payload else []
        output_s = args.output if args.output else False
        sqli_scan(url, params, payloads, output_s)

    # Handle Host Header Injection
    if args.hhi:
        print("Running Host Header Injection Scanner")
        url = args.url
        host = args.host if args.host else None
        hhi(url, host)

    # Handle JavaScript scanning
    if args.js:
        print("Running JavaScript Scanner")
        url = args.url
        js_scanner(url)

    # Handle Reflected XSS scanning
    if args.reflected:
        print("Running Reflected XSS Scanner")
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
        print("Running DOM XSS Scanner")
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
        print("Running Blind XSS Scanner")
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
