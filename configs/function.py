import time
import requests
import re
import sys
from bs4 import BeautifulSoup
import subprocess
from urllib.parse import urljoin, urlparse, parse_qs, urlencode
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from configs.config import errors_msgs,boolean_based_payloads,time_based_payloads,union_select_payloads,headers,reflected_xss_payloads,dom_based_xss_payloads,__version__
from configs.config import error_based_payloads as ebp








# skipping certificate verification
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# slow printing
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)

# quistion for exiting
def asking():
    print("[\033[32m+\033[0m] Do you want to \033[32mcontinue\033[0m attacking, or \033[31mexit\033[0m (\033[32mc\033[0m, \033[31me\033[0m)?")
    answer = input(">> ")
    if answer == 'continue' or answer == 'c':
        slowprint("sorry we will start over")
        return True
    elif answer == 'exit' or answer == 'e':
        slowprint('Thanks for using our tool and keep updated :)')
        return False
        sys.exit
    else:
        slowprint('sorry we didn\'t understand your answer thanks for your time\nexiting...')
        return False
        sys.exit


def sqli_scan(url, parameters, payloads, output_s=False):
    if output_s == True:
        try:
            # Initialize empty list to store results
            vulnerable_parameters = []

            # open output file
            with open('vulnerable_links.txt', 'w') as output_file:
                output_file.write("SQL :\n\n")
                # Check for error-based SQL injection
                for parameter in parameters:
                    for payload in payloads:
                        # Send a GET request with the SQL injection payload
                        if '?' in url and '=' in url: #check if url have parameter
                            response = requests.get(url + payload)
                            new_url = url + payload
                            print('[\033[32m+\033[0m] trying.. '+ new_url)
                        else:
                            response = requests.get(url + "?" + parameter + "=" + payload)
                            new_url = url + "?" + parameter + "=" + payload
                            print('[\033[32m+\033[0m] trying.. '+ new_url)

                        # Check if the response contains any of the SQL error messages
                        for error_message in errors_msgs:
                            if error_message in response.text:
                                vulnerable_parameters.append((parameter, payload, 'Vulnerable (Error-based)'))
                                output_file.write(f"{new_url} : {payload}\n")
                                output_file.write("you can read more here about SQLi \n")
                                output_file.write("https://owasp.org/www-community/attacks/SQL_Injection_Prevention_Cheat_Sheet\n")

                # Check for boolean-based SQL injection
                for parameter in parameters:
                    for payload in boolean_based_payloads:
                        # Send a GET request with the SQL injection payload
                        if '?' in url and '=' in url: #check if url have parameter
                            start_time = time.time()
                            response = requests.get(url + payload)
                            new_url = url + payload
                            print('[\033[32m+\033[0m] trying.. '+ new_url)
                            execution_time = time.time() - start_time
                        else:
                            start_time = time.time()
                            response = requests.get(url + "?" + parameter + "=" + payload)
                            new_url = url + "?" + parameter + "=" + payload
                            print('[\033[32m+\033[0m] trying.. '+ new_url)
                            execution_time = time.time() - start_time

                        # Check if the response contains the specified payload
                        if payload in response.text:
                            vulnerable_parameters.append((parameter, payload, 'Vulnerable (Boolean-based)'))
                            output_file.write(f"{new_url} : {payload}\n")
                            output_file.write("you can read more here about SQLi \n")
                            output_file.write("https://owasp.org/www-community/attacks/SQL_Injection_Prevention_Cheat_Sheet\n")


                # Check for time-based SQL injection
                for parameter in parameters:
                    for payload in time_based_payloads:
                        # Send a GET request with the SQL injection payload
                        if '?' in url and '=' in url: #check if url have parameter
                            start_time = time.time()
                            response = requests.get(url + payload)
                            new_url = url + payload
                            print('[\033[32m+\033[0m] trying.. '+ new_url)
                            execution_time = time.time() - start_time
                        else:
                            start_time = time.time()
                            response = requests.get(url + "?" + parameter + "=" + payload)
                            new_url = url + "?" + parameter + "=" + payload
                            print('[\033[32m+\033[0m] trying.. '+ new_url)
                            execution_time = time.time() - start_time

                        # Check if the execution time is significantly different from the default execution time
                        if execution_time > 5:  # Adjust this threshold as needed
                            vulnerable_parameters.append((parameter, payload, 'Vulnerable (Time-based)'))
                            output_file.write(f"{new_url} : {payload}\n")
                            output_file.write("you can read more here about SQLi \n")
                            output_file.write("https://portswigger.net/web-security/sql-injection/blind\n")

                # Check for UNION SELECT-based SQL injection
                for parameter in parameters:
                    for payload in union_select_payloads:
                        # Send a GET request with the SQL injection payload
                        if '?' in url and '=' in url: #check if url have parameter
                            response = requests.get(url + payload)
                            new_url = url + payload
                            print('[\033[32m+\033[0m] trying.. '+ new_url)
                        else:
                            response = requests.get(url + "?" + parameter + "=" + payload)
                            new_url = url + "?" + parameter + "=" + payload
                            print('[\033[32m+\033[0m] trying.. '+ new_url)

                        # Check if the response contains the specified payload
                        if payload in response.text:
                            vulnerable_parameters.append((parameter, payload, 'Vulnerable (UNION SELECT-based)'))
                            output_file.write(f"{new_url} : {payload}\n")
                            output_file.write("you can read more here about SQLi \n")
                            output_file.write("https://owasp.org/www-community/attacks/SQL_Injection_Prevention_Cheat_Sheet\n")


            return vulnerable_parameters
        except KeyboardInterrupt:
            asking()
            if asking == True:
                sqli_scan(url,parameters,payloads,output_s=True)
            else:
                sys.exit
    else:
        try:
            # Initialize empty list to store results
            vulnerable_parameters = []
            # Check for error-based SQL injection
            for parameter in parameters:
                for payload in payloads:
                    # Send a GET request with the SQL injection payload
                    if '?' in url and '=' in url: #check if url have parameter
                        response = requests.get(url + payload)
                        new_url = url + payload
                        print('[\033[32m+\033[0m] trying.. '+ new_url)
                    else:
                        response = requests.get(url + "?" + parameter + "=" + payload)
                        new_url = url + "?" + parameter + "=" + payload
                        print('[\033[32m+\033[0m] trying.. '+ new_url)

                    # Check if the response contains any of the SQL error messages
                    for error_message in errors_msgs:
                        if error_message in response.text:
                            vulnerable_parameters.append((parameter, payload, 'Vulnerable (Error-based)'))
                            print("sql injection in " + new_url)
                            slowprint("you can read this artical to learn more about this vulnerability and how to fix it")
                            print("https://owasp.org/www-community/attacks/SQL_Injection_Prevention_Cheat_Sheet")

            # Check for boolean-based SQL injection
            for parameter in parameters:
                for payload in boolean_based_payloads:
                    # Send a GET request with the SQL injection payload
                    if '?' in url and '=' in url: #check if url have parameter
                        start_time = time.time()
                        response = requests.get(url + payload)
                        new_url = url + payload
                        print('[\033[32m+\033[0m] trying.. '+ new_url)
                        execution_time = time.time() - start_time
                    else:
                        start_time = time.time()
                        response = requests.get(url + "?" + parameter + "=" + payload)
                        new_url = url + "?" + parameter + "=" + payload
                        print('[\033[32m+\033[0m] trying.. '+ new_url)
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
                        print('[\033[32m+\033[0m] trying.. '+ new_url)
                        execution_time = time.time() - start_time
                    else:
                        start_time = time.time()
                        response = requests.get(url + "?" + parameter + "=" + payload)
                        new_url = url + "?" + parameter + "=" + payload
                        print('[\033[32m+\033[0m] trying.. '+ new_url)
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
                        print('[\033[32m+\033[0m] trying.. '+ new_url)
                    else:
                        response = requests.get(url + "?" + parameter + "=" + payload)
                        new_url = url + "?" + parameter + "=" + payload
                        print('[\033[32m+\033[0m] trying.. '+ new_url)

                    # Check if the response contains the specified payload
                    if payload in response.text:
                        vulnerable_parameters.append((parameter, payload, 'Vulnerable (UNION SELECT-based)'))
                        print("sql injection in " + new_url)
                        slowprint("you can read this artical to learn more about this vulnerability and how to fix it")
                        print("linkre")


            return vulnerable_parameters
        except KeyboardInterrupt:
            asking()
            if asking == True:
                sqli_scan(url,parameters,payloads,output_s=False)
            else:
                sys.exit


def hhi(url, head=None,output_s=False): # host header injection scanner singel url
    if output_s == True:
        try:
            if head:
                r = requests.get(url, headers={'Host': head}, verify=False)
            else:
                r = requests.get(url, headers=headers, verify=False)

            if r.status_code == 200:
                print(f'url has host header injection\n {url}')
                slowprint("you can read this artical to learn more about this vulnerability and how to fix it")
                print("linkre")

                # Open the output file for writing and save the vulnerable URL
                with open('vulnerable_urls.txt', 'a') as output_file:
                    output_file.write("Host Header Injection :")
                    output_file.write(f"{url}\n")
            else:
                print(f'url does not have host header injection\n {url}')

        except requests.exceptions.SSLError as e:
            print(f"SSL Certificate Verification Error: {e}")
            # Handle SSL certificate verification error
        except KeyboardInterrupt:
            asking()
            if asking == True:
                hhi(url,head=None)
            else:
                sys.exit
    else:
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
        except KeyboardInterrupt:
            asking()
            if asking == True:
                hhi(url,head=None)
            else:
                sys.exit

def js_scanner(url,output_s=False): # scan for api key or any secrets in java script files
    if output_s == True:
        try:
            def extract_js_files(url):
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        content = response.text
                        js_files = re.findall(r'<script.*?src="(.*?)"', content)
                        js_files = [urljoin(url, js_file) for js_file in js_files]
                        return js_files
                    else:
                        print(f"[\033[31mError\033[0m] Failed to retrieve content from {url}. Status code: {response.status_code}")
                        return []
                except Exception as e:
                    print(f"[\033[32m+\033[0m] extracting JS files from {url}: {e}")
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
                            print(f"[\033[32m+\033[0m] Crawling {url}...")
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

            def check_webpage(url,output_file):
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        content_type = response.headers.get('content-type')
                        if 'javascript' in content_type:
                            api_keys = extract_api_keys_from_js(response.text)
                        elif 'html' in content_type:
                            api_keys = extract_api_keys_from_html(response.text)
                        else:
                            print(f"[\033[31mError\033[0m] Unsupported content type for {url}")
                            return

                        if api_keys:
                            print(f"API keys found in {url}: {api_keys}")
                            output_file.write(f"{url}: {api_keys}\n")  # Write to output file
                            slowprint("you can read this artical to learn more about this vulnerability and how to fix it")
                            print("linkre")
                        else:
                            print(f"No API keys found in {url}")
                    else:
                        print(f"[\033[31mError\033[0m] Failed to fetch {url}: {response.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"[\033[31mError\033[0m] fetching {url}: {e}")

            def check_wordlist(wordlist_file,output_file):
                with open(wordlist_file, 'r') as file:
                    urls = file.read().splitlines()
                    for url in urls:
                        check_webpage(url,output_file)
            # Open the output file for writing
            output_file_path = 'api_keys_urls.txt'
            with open(output_file_path, 'w') as output_file:
                wordlist_file = "js_files.txt"
                check_wordlist(wordlist_file, output_file)
        except KeyboardInterrupt:
            asking()
            if asking == True:
                js_scanner(url)
            else:
                sys.exit
    else:
        try:
            def extract_js_files(url):
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        content = response.text
                        js_files = re.findall(r'<script.*?src="(.*?)"', content)
                        js_files = [urljoin(url, js_file) for js_file in js_files]
                        return js_files
                    else:
                        print(f"[\033[31mError\033[0m] Failed to retrieve content from {url}. Status code: {response.status_code}")
                        return []
                except Exception as e:
                    print(f"[\033[32m+\033[0m] extracting JS files from {url}: {e}")
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
                            print(f"[\033[32m+\033[0m] Crawling {url}...")
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
                            print(f"[\033[31mError\033[0m] Unsupported content type for {url}")
                            return

                        if api_keys:
                            print(f"API keys found in {url}: {api_keys}")
                            slowprint("you can read this artical to learn more about this vulnerability and how to fix it")
                            print("linkre")
                        else:
                            print(f"No API keys found in {url}")
                    else:
                        print(f"[\033[31mError\033[0m] Failed to fetch {url}: {response.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"[\033[31mError\033[0m] fetching {url}: {e}")

            def check_wordlist(wordlist_file):
                with open(wordlist_file, 'r') as file:
                    urls = file.read().splitlines()
                    for url in urls:
                        check_webpage(url)
            wordlist_file = "js_files.txt"
            check_wordlist(wordlist_file)
        except KeyboardInterrupt:
            asking()
            if asking == True:
                js_scanner(url)
            else:
                sys.exit


def send_request(url, payload):
    try:
        response = requests.get(url + payload)


        # Check if the response contains the payload
        if response.status_code == 200 and payload in response.text:
            return True
    except requests.exceptions.RequestException as e:
        print(f"[\033[31mError\033[0m] An error occurred: {e}")

    return False


# xss reflected scanner
class ReflectedXSSScanner:
        def __init__(self, base_url, payloads,output_s):
            self.base_url = base_url
            self.payloads = payloads
            self.visited_urls = set()
            self.vulnerable_urls = set()
            self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

        def _get_all_urls(self, url):
            headers = {'User-Agent': self.user_agent}
            try:
                response = requests.get(url, headers=headers, timeout=5)
                if response.status_code != 200:
                    print(f"[\033[31mError\033[0m] fetching URLs from {url}: {response.status_code}")
                    return []
                soup = BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a', href=True)
                urls = [urljoin(url, link['href']) for link in links]
                return urls
            except Exception as e:
                print(f"[\033[31mError\033[0m] fetching URLs from {url}: {e}")
                return []

        def _check_reflected_xss(self, url):
            headers = {'User-Agent': self.user_agent}
            try:
                response = requests.get(url, headers=headers, timeout=5)
                if response.status_code != 200:
                    print(f"[\033[32m+\033[0m] checking reflected XSS in {url}: {response.status_code}")
                    return
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
                                response = requests.get(modified_url, headers=headers, timeout=5)
                                if payload in response.text:
                                    self.vulnerable_urls.add(form_url)
                                    print(f"Reflected XSS found in {form_url} with payload: {payload}")
                                    if output_s == True:
                                        # Write vulnerable URL to the output file
                                        with open("vulnerable_urls.txt", 'a') as output_file:
                                            output_file.write(f"{form_url}\n")
                                    else:
                                        slowprint("You can read this article to learn more about this vulnerability and how to fix it:")
                                        print("https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)")
            except Exception as e:
                print(f"[\033[32m+\033[0m] checking reflected XSS in {url}: {e}")

        def crawl_and_scan(self):
                urls_to_scan = [self.base_url]
                while urls_to_scan:
                    current_url = urls_to_scan.pop(0)
                    if current_url in self.visited_urls:
                        continue
                    self.visited_urls.add(current_url)
                    print(f"[\033[32m+\033[0m] Scanning {current_url} for reflected XSS...")
                    self._check_reflected_xss(current_url)
                    urls_to_scan.extend(self._get_all_urls(current_url))
                    time.sleep(1)




# xss dom scanner
class DOMXSSScanner:
    def __init__(self, base_url, payloads,output_s):
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
            print(f"[\033[31mError\033[0m] fetching URLs from {url}: {e}")
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
                        if output_s == True:
                            # Write vulnerable URL to the output file
                            with open("vulnerable_urls.txt", 'a') as output_file:
                                output_file.write(f"{form_url}\n")
                        else:
                            slowprint("You can read this article to learn more about this vulnerability and how to fix it:")
                            print("https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html")
        except Exception as e:
            print(f"[\033[32m+\033[0m] checking DOM XSS in {url}: {e}")

    def crawl_and_scan(self):
        urls_to_scan = [self.base_url]
        while urls_to_scan:
            current_url = urls_to_scan.pop(0)
            if current_url in self.visited_urls:
                continue
            self.visited_urls.add(current_url)
            print(f"[\033[32m+\033[0m] Scanning {current_url} for DOM-based XSS...")
            self._check_dom_xss(current_url)
            urls_to_scan.extend(self._get_all_urls(current_url))

# xss blind scanner
class BlindXSSScanner:
    def __init__(self, base_url, payloads,output_s):
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
            print(f"[\033[31mError\033[0m] fetching URLs from {url}: {e}")
            return []

    def _check_blind_xss(self, url):
        try:
            for payload in self.payloads:
                response = requests.post(url, data={"input": payload})
                if payload in response.text:
                    self.vulnerable_urls.add(url)
                    print(f"Blind XSS found in {url} with payload: {payload}")
                    if output_s == True:
                        # Write vulnerable URL to the output file
                        with open("vulnerable_urls.txt", 'a') as output_file:
                            output_file.write(f"{form_url}\n")
                    else:
                        slowprint("You can read this article to learn more about this vulnerability and how to fix it:")
                        print("linkre")
        except Exception as e:
            print(f"[\033[32m+\033[0m] checking Blind XSS in {url}: {e}")

    def crawl_and_scan(self):
        urls_to_scan = [self.base_url]
        while urls_to_scan:
            current_url = urls_to_scan.pop(0)
            if current_url in self.visited_urls:
                continue
            self.visited_urls.add(current_url)
            print(f"[\033[32m+\033[0m] Scanning {current_url} for Blind XSS...")
            self._check_blind_xss(current_url)
            urls_to_scan.extend(self._get_all_urls(current_url))



def update():
    response = requests.get('https://www.github.com/mrsi13nt/black-candle/configs/config.py')
    if __version__ in response.text :
        pass
    else:
        print("\nthere is new version, want to update ? (Y/N)\n")
        up = input(">> ").upper
        if up == "Y":
            subprocess.run("ds",shell=True)
        elif up == "N":
            pass
        else:
            slowprint("wrong answer")
            sys.exit(2)
            


def check_file_existence(file_path):
    return os.path.exists(file_path)
