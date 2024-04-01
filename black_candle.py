import requests
import sys
import time
import os
import argparse
from function import *
from logo import *
from config import *



# code here


def main():
    usage = "usage: python3 black_candle.py [options] arg"
    parser = argparse.ArgumentParser(
                    prog='black candle',
                    description='a simple sql scanner',
                    epilog='Text at the bottom of help',
                    usage='%(prog)s -u URL')
    sql_group = parser.add_argument_group('SQL')
    sql_group.add_argument('--data', dest='data', metavar='"data"', help='Data string to be sent through POST (e.g. "id=1")')
    sql_group.add_argument('--cookie', dest='cookie', metavar='"cookies"', help='HTTP Cookie header value (e.g. "PHPSESSID=a8d127e..")') # x
    sql_group.add_argument('-p','--payload', dest='payload', metavar='payload', help='you can add custom payload' )
    hhi_group = parser.add_argument_group('Host Header Injection')
    hhi_group.add_argument('-hh', dest='hhi', help='run host header injection scanner')
    hhi_group.add_argument('--host', dest='host', metavar='Host', help='add custom host header (e.g. --host "www.ping.com")')
    js_group = parser.add_argument_group('JS scan')
    js_group.add_argument('-js', dest='js', action='store_true' ,help='scan all java script files of full website from api keys and more..')
    xss_group = parser.add_argument_group('XSS')
    xss_group.add_argument('-rf', dest='reflected', action='store_true', help='scan for reflected XSS')
    xss_group.add_argument('-d', dest='dom', action='store_true', help='scan for DOM XSS')
    detection_group = parser.add_argument_group('Detection')
    detection_group.add_argument('--level',dest='level', metavar='int', action='store', type=int, help='the level of scan from 1 to 3 (default 1)') # x
    output_group = parser.add_argument_group('Output')
    output_group.add_argument('-o', dest='output', metavar='string', type=argparse.FileType('w', encoding='latin-1'), help='file to write output to') # x
    parser.add_argument('-u', '--url', dest='url', action='store', metavar='URL', help='Target URL (e.g. "http://www.site.com/vuln.php?id=1")')
    parser.add_argument('-l', '--list', dest='urlist', action='store', metavar='file_path', help='target list of urls')
    args = parser.parse_args()

    # check the target url or list
    if not args.url and not args.urlist:
        print("Error: Either -u/--url or -l/--list option is required.")
        parser.print_help()
        sys.exit(1)
# ======== list of urls ===========
    if args.urlist:
        file_p = args.urlist
        #check if the file exist
        if check_file_existence(file_p):
            # Read lines from the file
            with open(file_p, 'r') as file:
                lines = [line.strip() for line in file]
                for line in lines:
                    sqli_scan(line,params,payloads)
        else:
            slowprint(f"the file {file} not exist\n please try again with full path")
    elif args.urlist and args.payload:
        file_p = args.urlist
        payload = args.payload
        #check if the file exist
        if check_file_existence(file):
            # Read lines from the file
            with open(file_p, 'r') as file:
                lines = [line.strip() for line in file]
                for line in lines:
                    sqli_scan(line,params,payload)
        else:
            slowprint(f"the file {file} not exist\n please try again with full path")

    elif args.urlist and args.payload and args.data:
        file_p = args.urlist
        payload = args.payload
        data = args.data
        #check if the file exist
        if check_file_existence(file):
            # Read lines from the file
            with open(file_p, 'r') as file:
                lines = [line.strip() for line in file]
                for line in lines:
                    sqli_scan(line,data,payload)
        else:
            slowprint(f"the file {file} not exist\n please try again with full path")
    else:
        slowprint

# ======== SQL =========        
    if args.url and args.data:
        url = args.url
        data = args.data
        sqli_scan(url,data,payloads)
    elif args.url and args.payload:
        url = args.url
        payload = args.payload
        sqli_scan(url,params,payload)
    elif args.url and args.data and args.payload:
        url = args.url
        payload = args.payload
        data = args.Data
        sqli_scan(url,data,payload)
# ======== Host Header Injection =========
    elif args.hhi and args.url:
        hhi(args.url,None)
    elif args.hhi and args.host and args.url:
        hhi(args.url, args.host)
    elif args.hhi and args.list:
        hhi_list(args.list,None)
    elif args.hhi and args.host and args.list:
        hhi_list(args.list, args.host)
# ======== Scan Java Script Files =========
    elif args.js:
        js_scanner(args.url)
# ======== Scan XSS =========
    elif args.reflected:
        xss_re(args.url)
    elif args.dom:
        xss_dom(args.url)
    else:
        slowprint("please try again with true usage")
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
