import requests
import re

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

if __name__ == "__main__":
    wordlist_file = "js_files.txt"  # Update with your wordlist file
    check_wordlist(wordlist_file)
