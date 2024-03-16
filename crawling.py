import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse

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

if __name__ == '__main__':
    start_url = 'https://overthewire.org/wargames/natas/'  # Specify the starting URL here
    crawl_js_files(start_url)
