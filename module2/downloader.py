import requests

def download_article(url):
    """
    Downloads the content of the article from the given URL.
    follows SRP as it is only responsible for one thing
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while processing {url}: {e}")
    return None
