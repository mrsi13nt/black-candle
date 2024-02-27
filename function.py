import time
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from config import errors_msgs,boolean_based_payloads,time_based_payloads,union_select_payloads,headers
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
            if ['?','='] in url: #check if url have parameter
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
            if ['?','='] in url: #check if url have parameter
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
            if ['?','='] in url: #check if url have parameter
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
            if ['?','='] in url: #check if url have parameter
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
        # Handle SSL certificate verification error as needed

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
            # Handle SSL certificate verification error as needed

def check_file_existence(file_path):
    return os.path.exists(file_path)

def level_one():
    print("level 1")

def level_two():
    print("level 1")

def level_three():
    print("level 3")
