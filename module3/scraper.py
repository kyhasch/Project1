from bs4 import BeautifulSoup
import requests

def process_article(article_content):
    """
    Processes the raw article content to extract and return only the main body of the article.
    follows SRP as it is only responsible for one thing
    """
    try:
        soup = BeautifulSoup(article_content, 'html.parser')
        main_content = soup.find('div', class_='article-body')  # Adjust this according to the HTML structure of the target site
        if main_content:
            return main_content.get_text(separator='\n')  # Return the text content of the article
        else:
            print(f"No main content found")
    except Exception as e:
        print(f"An error occurred while processing article content: {e}")
    return None
