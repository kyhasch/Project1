import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def download_article(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find and extract the main content of the article
            main_content = soup.find('div', class_='article-body') # Adjust this according to the HTML structure of the target site
            if main_content:
                return main_content.get_text(separator='\n') # Return the text content of the article
            else:
                print(f"No main content found for {url}")
        else:
            print(f"Failed to fetch {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while processing {url}: {e}")
    return None

def save_article(content, index):
    filename = f"article_{index}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Article {index} saved as {filename}")

def main():
    file_path = input("Enter the path to the text file containing URLs: ").strip()
    if not os.path.isfile(file_path):
        print("Invalid file path.")
        return

    with open(file_path, 'r') as file:
        urls = file.readlines()

    for i, url in enumerate(urls, start=1):
        url = url.strip()
        if not url:
            continue
        print(f"Processing article {i}...")
        article_content = download_article(url)
        if article_content:
            save_article(article_content, i)
        print()

if __name__ == "__main__":
    main()