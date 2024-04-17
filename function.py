import time
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs, urlencode
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
                new_url = url + payload
                print('trying.. '+ new_url)
            else:
                response = requests.get(url + "?" + parameter + "=" + payload)
                new_url = url + "?" + parameter + "=" + payload
                print('trying.. '+ new_url)

            # Check if the response contains any of the SQL error messages
            for error_message in errors_msgs:
                if error_message in response.text:
                    vulnerable_parameters.append((parameter, payload, 'Vulnerable (Error-based)'))
                    print("sql injection in " + new_url)
                    slowprint("you can read this artical to learn more about this vulnerability and how to fix it")
                    print("linkre")

    # Check for boolean-based SQL injection
    for parameter in parameters:
        for payload in boolean_based_payloads:
            # Send a GET request with the SQL injection payload
            if '?' in url and '=' in url: #check if url have parameter
                start_time = time.time()
                response = requests.get(url + payload)
                new_url = url + payload
                print('trying.. '+ new_url)
                execution_time = time.time() - start_time
            else:
                start_time = time.time()
                response = requests.get(url + "?" + parameter + "=" + payload)
                new_url = url + "?" + parameter + "=" + payload
                print('trying.. '+ new_url)
                execution_time = time.time() - start_time

            # Check if the response contains the specified payload
            if payload in response.text:
                vulnerable_parameters.append((parameter, payload, 'Vulnerable (Boolean-based)'))
                print("sql injection in " + new_url)
                slowprint("you can read this artical to learn more about this vulnerability and how to fix it")
                print("linkre")
                

    # Check for time-based SQL injection
    for parameter in parameters:
        for payload in time_based_payloads:
            # Send a GET request with the SQL injection payload
            if '?' in url and '=' in url: #check if url have parameter
                start_time = time.time()
                response = requests.get(url + payload)
                new_url = url + payload
                print('trying.. '+ new_url)
                execution_time = time.time() - start_time
            else:
                start_time = time.time()
                response = requests.get(url + "?" + parameter + "=" + payload)
                new_url = url + "?" + parameter + "=" + payload
                print('trying.. '+ new_url)
                execution_time = time.time() - start_time

            # Check if the execution time is significantly different from the default execution time
            if execution_time > 5:  # Adjust this threshold as needed
                vulnerable_parameters.append((parameter, payload, 'Vulnerable (Time-based)'))
                print("sql injection in " + new_url)
                slowprint("you can read this artical to learn more about this vulnerability and how to fix it")
                print("linkre")

    # Check for UNION SELECT-based SQL injection
    for parameter in parameters:
        for payload in union_select_payloads:
            # Send a GET request with the SQL injection payload
            if '?' in url and '=' in url: #check if url have parameter
                response = requests.get(url + payload)
                new_url = url + payload
                print('trying.. '+ new_url)
            else:
                response = requests.get(url + "?" + parameter + "=" + payload)
                new_url = url + "?" + parameter + "=" + payload
                print('trying.. '+ new_url)

            # Check if the response contains the specified payload
            if payload in response.text:
                vulnerable_parameters.append((parameter, payload, 'Vulnerable (UNION SELECT-based)'))
                print("sql injection in " + new_url)
                slowprint("you can read this artical to learn more about this vulnerability and how to fix it")
                print("linkre")


    return vulnerable_parameters


def hhi(url, head=None): # host header injection scanner singel url
    try:
        if head:
            r = requests.get(url, headers={'Host': head}, verify=False)
        else:
            r = requests.get(url, headers=headers, verify=False)

        if r.status_code == 200:
            print(f'url has host header injection\n {url}')
            slowprint("you can read this artical to learn more about this vulnerability and how to fix it")
            print("linkre")
        else:
            print(f'url does not have host header injection\n {url}')

    except requests.exceptions.SSLError as e:
        print(f"SSL Certificate Verification Error: {e}")
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
                    slowprint("you can read this artical to learn more about this vulnerability and how to fix it")
                    print("linkre")
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
class ReflectedXSSScanner:
    def __init__(self, base_url, payloads):
        self.base_url = base_url
        self.payloads = payloads
        self.visited_urls = set()
        self.vulnerable_urls = set()

    def _get_all_urls(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            urls = [urljoin(url, link['href']) for link in links]
            return urls
        except Exception as e:
            print(f"Error fetching URLs from {url}: {e}")
            return []

    def _check_reflected_xss(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            forms = soup.find_all('form')
            for form in forms:
                form_action = form.get('action')
                if form_action:
                    form_url = urljoin(url, form_action)
                    form_inputs = form.find_all('input', {'type': 'text'})
                    for input_field in form_inputs:
                        input_name = input_field.get('name')
                        for payload in self.payloads:
                            modified_params = {input_name: payload}
                            modified_url = form_url + '?' + urlencode(modified_params)
                            response = requests.get(modified_url)
                            if payload in response.text:
                                self.vulnerable_urls.add(form_url)
                                print(f"Reflected XSS found in {form_url} with payload: {payload}")
                                slowprint("you can read this artical to learn more about this vulnerability and how to fix it")
                                print("linkre")
        except Exception as e:
            print(f"Error checking reflected XSS in {url}: {e}")

    def crawl_and_scan(self):
        urls_to_scan = [self.base_url]
        while urls_to_scan:
            current_url = urls_to_scan.pop(0)
            if current_url in self.visited_urls:
                continue
            self.visited_urls.add(current_url)
            print(f"Scanning {current_url} for reflected XSS...")
            self._check_reflected_xss(current_url)
            urls_to_scan.extend(self._get_all_urls(current_url))


# xss dom scanner
class DOMXSSScanner:
    def __init__(self, base_url, payloads):
        self.base_url = base_url
        self.payloads = payloads
        self.visited_urls = set()
        self.vulnerable_urls = set()

    def _get_all_urls(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            urls = [urljoin(url, link['href']) for link in links]
            return urls
        except Exception as e:
            print(f"Error fetching URLs from {url}: {e}")
            return []

    def _check_dom_xss(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            script_tags = soup.find_all('script')
            for script_tag in script_tags:
                for payload in self.payloads:
                    if payload in script_tag.get_text():
                        self.vulnerable_urls.add(url)
                        print(f"DOM-based XSS found in {url} with payload: {payload}")
                        slowprint("you can read this artical to learn more about this vulnerability and how to fix it")
                        print("linkre")
                        break
        except Exception as e:
            print(f"Error checking DOM XSS in {url}: {e}")

    def crawl_and_scan(self):
        urls_to_scan = [self.base_url]
        while urls_to_scan:
            current_url = urls_to_scan.pop(0)
            if current_url in self.visited_urls:
                continue
            self.visited_urls.add(current_url)
            print(f"Scanning {current_url} for DOM-based XSS...")
            self._check_dom_xss(current_url)
            urls_to_scan.extend(self._get_all_urls(current_url))

# xss blind scanner
class BlindXSSScanner:
    def __init__(self, base_url, payloads):
        self.base_url = base_url
        self.payloads = payloads
        self.visited_urls = set()
        self.vulnerable_urls = set()

    def _get_all_urls(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            urls = [urljoin(url, link['href']) for link in links]
            return urls
        except Exception as e:
            print(f"Error fetching URLs from {url}: {e}")
            return []

    def _check_blind_xss(self, url):
        try:
            for payload in self.payloads:
                response = requests.post(url, data={"input": payload})
                if payload in response.text:
                    self.vulnerable_urls.add(url)
                    print(f"Blind XSS found in {url} with payload: {payload}")
                    slowprint("you can read this artical to learn more about this vulnerability and how to fix it")
                    print("linkre")
        except Exception as e:
            print(f"Error checking Blind XSS in {url}: {e}")

    def crawl_and_scan(self):
        urls_to_scan = [self.base_url]
        while urls_to_scan:
            current_url = urls_to_scan.pop(0)
            if current_url in self.visited_urls:
                continue
            self.visited_urls.add(current_url)
            print(f"Scanning {current_url} for Blind XSS...")
            self._check_blind_xss(current_url)
            urls_to_scan.extend(self._get_all_urls(current_url))

# WAF bypass
class WAFBypass:
    def __init__(self, enable_bypass=False):
        self.enable_bypass = enable_bypass

    def _detect_waf(self, url):
        try:
            response = requests.get(url)
            if 'Web Application Firewall' in response.headers.get('Server', ''):
                print(f"WAF detected on {url}")
                return True
            else:
                print(f"No WAF detected on {url}")
                return False
        except Exception as e:
            print(f"Error checking WAF in {url}: {e}")
            return False

    def _bypass_waf(self, url):
        # Add your WAF bypass techniques here
        print(f"Bypassing WAF on {url}...")

    def bypass(self, url):
        if self.enable_bypass:
            if self._detect_waf(url):
                self._bypass_waf(url)


def check_file_existence(file_path):
    return os.path.exists(file_path)
