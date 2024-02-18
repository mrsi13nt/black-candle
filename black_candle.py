import requests
import sys
import time
from bs4 import BeautifulSoup
import json
import argparse
from function import *
from logo import *




# new main page


def main():
    usage = "usage: python3 black_candle.py [options] arg"
    parser = argparse.ArgumentParser(
                    prog='black candle',
                    description='a simple sql scanner',
                    epilog='Text at the bottom of help',
                    usage='%(prog)s -u URL')
    request_group = parser.add_argument_group('Request')
    request_group.add_argument('--data', dest='data', metavar='"data"', help='Data string to be sent through POST (e.g. "id=1")')
    request_group.add_argument('--cookie', dest='cookie', metavar='"cookies"', help='HTTP Cookie header value (e.g. "PHPSESSID=a8d127e..")')
    detection_group = parser.add_argument_group('Detection')
    detection_group.add_argument('--level',dest='level', metavar='int', action='store', type=int, help='the level of scan from 1 to 3 (default 1)')
    output_group = parser.add_argument_group('Output')
    output_group.add_argument('-o', dest='output', metavar='string', type=argparse.FileType('w', encoding='latin-1'), help='file to write output to')
    parser.add_argument('-u', '--url', dest='url', action='store', metavar='URL', required=True, help='Target URL (e.g. "http://www.site.com/vuln.php?id=1")')
    parser.add_argument('-l', '--list', dest='urlist', action='store', metavar='file_path', help='target list of urls')
    args = parser.parse_args()

    # check the target url or list
    if not args.url and not args.urlist:
        print("Error: Either -u/--url or -l/--list option is required.")
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
