import time
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from config import errors_msgs,boolean_based_payloads,time_based_payloads,union_select_payloads,headers,reflected_xss_payloads,dom_based_xss_payloads
from config import error_based_payloads as ebp


# Suppress only the InsecureRequestWarning caused by skipping certificate verification
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)


def sqli_scan(url, parameters, payloads):

    payloads = ebp
    # Initialize empty list to store results
    vulnerable_parameters = []

    # Check for error-based SQL injection
    for parameter in parameters:
        for payload in payloads:
            # Send a GET request with the SQL injection payload
            if '?' in url and '=' in url: #check if url have parameter
                response = requests.get(url + payload)
            else:
                response = requests.get(url + "?" + parameter + "=" + payload)
                new_url = url + "?" + parameter + "=" + payload
                print('trying.. '+ new_url)

            # Check if the response contains any of the SQL error messages
            for error_message in errors_msgs:
                if error_message in response.text:
                    vulnerable_parameters.append((parameter, payload, 'Vulnerable (Error-based)'))
                    print("sql injection in " + new_url)

    # Check for boolean-based SQL injection
    for parameter in parameters:
        for payload in boolean_based_payloads:
            # Send a GET request with the SQL injection payload
            if '?' in url and '=' in url: #check if url have parameter
                start_time = time.time()
                response = requests.get(url + payload)
                execution_time = time.time() - start_time
            else:
                start_time = time.time()
                response = requests.get(url + "?" + parameter + "=" + payload)
                execution_time = time.time() - start_time

            # Check if the response contains the specified payload
            if payload in response.text:
                vulnerable_parameters.append((parameter, payload, 'Vulnerable (Boolean-based)'))

    # Check for time-based SQL injection
    for parameter in parameters:
        for payload in time_based_payloads:
            # Send a GET request with the SQL injection payload
            if '?' in url and '=' in url: #check if url have parameter
                start_time = time.time()
                response = requests.get(url + payload)
                execution_time = time.time() - start_time
            else:
                start_time = time.time()
                response = requests.get(url + "?" + parameter + "=" + payload)
                execution_time = time.time() - start_time

            # Check if the execution time is significantly different from the default execution time
            if execution_time > 5:  # Adjust this threshold as needed
                vulnerable_parameters.append((parameter, payload, 'Vulnerable (Time-based)'))

    # Check for UNION SELECT-based SQL injection
    for parameter in parameters:
        for payload in union_select_payloads:
            # Send a GET request with the SQL injection payload
            if '?' in url and '=' in url: #check if url have parameter
                response = requests.get(url + payload)
            else:
                response = requests.get(url + "?" + parameter + "=" + payload)

            # Check if the response contains the specified payload
            if payload in response.text:
                vulnerable_parameters.append((parameter, payload, 'Vulnerable (UNION SELECT-based)'))


    return vulnerable_parameters


def hhi(url, head=None): # host header injection scanner singel url
    try:
        if head:
            r = requests.get(url, headers={'Host': head}, verify=False)
        else:
            r = requests.get(url, headers=headers, verify=False)

        if r.status_code == 200:
            print(f'url has host header injection\n {url}')
        else:
            print(f'url does not have host header injection\n {url}')

    except requests.exceptions.SSLError as e:
        print(f"SSL Certificate Verification Error: {e}")
        # Handle SSL certificate verification error

def hhi_list(urls, head=None): # host header injection scanner list of urls
    for url in urls:
        try:
            if head:
                r = requests.get(url, headers={'Host': head}, verify=False)
            else:
                r = requests.get(url, headers=headers, verify=False)

            if r.status_code == 200:
                print(f'url has host header injection\n {url}')
            else:
                print(f'url does not have host header injection\n {url}')

        except requests.exceptions.SSLError as e:
            print(f"SSL Certificate Verification Error for {url}: {e}")
            # Handle SSL certificate verification error

def js_scanner(url): # scan for api key or any secrets in java script files

    def extract_js_files(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                content = response.text
                js_files = re.findall(r'<script.*?src="(.*?)"', content)
                js_files = [urljoin(url, js_file) for js_file in js_files]
                return js_files
            else:
                print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error extracting JS files from {url}: {e}")
            return []

    def crawl_js_files(start_url, depth=3, output_file='js_files.txt'):
        visited = set()
        queue = [(start_url, 0)]

        with open(output_file, 'w') as file:
            while queue:
                url, level = queue.pop(0)
                if level > depth:
                    continue

                if url not in visited:
                    visited.add(url)
                    print(f"Crawling {url}...")
                    js_files = extract_js_files(url)
                    for js_file in js_files:
                        file.write(js_file + '\n')

                    response = requests.get(url)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.content, 'html.parser')
                        links = [link.get('href') for link in soup.find_all('a', href=True)]
                        links = [urljoin(url, link) for link in links if link and urlparse(link).netloc == urlparse(start_url).netloc]
                        queue.extend([(link, level + 1) for link in links])

        print(f"Crawling completed. JavaScript URLs saved to {output_file}")

    crawl_js_files(url)
    def extract_api_keys_from_js(js_code):
        api_keys = re.findall(r'(?:["\'])(?:api(?:[_-])?(?:key|token)|secret(?:[_-])?key|access(?:[_-])?token)(?:["\'])\s*:\s*(?:["\'])(.*?)(?:["\'])', js_code)
        return api_keys

    def extract_api_keys_from_html(html_code):
        api_keys = re.findall(r'(?:["\'])(?:api(?:[_-])?(?:key|token)|secret(?:[_-])?key|access(?:[_-])?token)(?:["\'])\s*=\s*(?:["\'])(.*?)(?:["\'])', html_code)
        return api_keys

    def check_webpage(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                content_type = response.headers.get('content-type')
                if 'javascript' in content_type:
                    api_keys = extract_api_keys_from_js(response.text)
                elif 'html' in content_type:
                    api_keys = extract_api_keys_from_html(response.text)
                else:
                    print(f"Unsupported content type for {url}")
                    return

                if api_keys:
                    print(f"API keys found in {url}: {api_keys}")
                else:
                    print(f"No API keys found in {url}")
            else:
                print(f"Failed to fetch {url}: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")

    def check_wordlist(wordlist_file):
        with open(wordlist_file, 'r') as file:
            urls = file.read().splitlines()
            for url in urls:
                check_webpage(url)
    wordlist_file = "js_files.txt"
    check_wordlist(wordlist_file)


def send_request(url, payload):
    try:
        response = requests.get(url + payload)


        # Check if the response contains the payload
        if response.status_code == 200 and payload in response.text:
            return True
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return False


# xss reflected scanner
def xss_re(url):
    def check_reflected_xss(url):
        print("Checking for reflected XSS...")
        if "?" not in url or "=" not in url:
            for payload in reflected_xss_payloads:
                if send_request(url, "?q=" + payload):
                    print(f"Reflected XSS found with payload: {payload}")
                    return True
            return False
        else:
            for payload in reflected_xss_payloads:
                if send_request(url + payload):
                    print(f"Reflected XSS found with payload: {payload}")
                    return True
            return False
    if not check_reflected_xss(url):
        print("No reflected XSS found.")

# xss dom scanner
def xss_dom(url):
    def check_dom_based_xss(url):
        print("Checking for DOM-based XSS...")
        if "?" not in url or "=" not in url:
            for payload in dom_based_xss_payloads:
                if send_request(url, "#" + payload):
                    print(f"DOM-based XSS found with payload: {payload}")
                    return True
            return False
        else:
            for payload in dom_based_xss_payloads:
                if send_request(url + payload):
                    print(f"DOM-based XSS found with payload: {payload}")
                    return True
            return False
    if not check_dom_based_xss(url):
        print("No DOM-based XSS found.")


def check_file_existence(file_path):
    return os.path.exists(file_path)
