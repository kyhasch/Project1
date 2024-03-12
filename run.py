import os
from module2 import downloader
from module3 import scraper
"""
manages the dowloading and processing of article data
for Soc as it clearly separates different areas based on concerns
"""

def main():
    # Check if the 'Data/raw' directory exists
    raw_data_dir = 'Data/raw'
    if not os.path.exists(raw_data_dir):
        os.makedirs(raw_data_dir)

    # Check if the 'Processed' directory exists
    processed_dir = 'Processed'
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)

    # Read URLs from the raw data file
    raw_data_file = 'raw/raw_data_file.txt'
    with open(raw_data_file, 'r') as file:
        urls = file.readlines()

    # Download and process articles
    for i, url in enumerate(urls, start=1):
        url = url.strip()
        if not url:
            continue
        print(f"Processing article {i}...")
        article_content = downloader.download_article(url)
        if article_content:
            # Save the raw article content
            raw_article_file = os.path.join(raw_data_dir, f"article_{i}.txt")
            with open(raw_article_file, 'w', encoding='utf-8') as f:
                f.write(article_content)

            # Process the article content
            processed_article = scraper.process_article(article_content)
            if processed_article:
                # Save the processed article content
                processed_article_file = os.path.join(processed_dir, f"article_{i}.txt")
                with open(processed_article_file, 'w', encoding='utf-8') as f:
                    f.write(processed_article)

    print("Articles processing complete.")

if __name__ == "__main__":
    main()
