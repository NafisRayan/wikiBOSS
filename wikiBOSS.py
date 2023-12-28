import wikipediaapi
import requests
from bs4 import BeautifulSoup

def get_wikipedia_data_api(topic, language='en'):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    
    headers = {'User-Agent': user_agent}
    wiki_wiki = wikipediaapi.Wikipedia(language, headers=headers)
    page_py = wiki_wiki.page(topic)

    if not page_py.exists():
        print(f"Page '{topic}' does not exist.")
        return None

    print("Title:", page_py.title)
    print("Text (API):", page_py.text)  # Displaying the first 60 characters of the text

    return page_py.text

def scrape_wikipedia_web(topic):
    base_url = "https://en.wikipedia.org/wiki/"
    url = base_url + topic.replace(" ", "_")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('div', {'id': 'mw-content-text'})

    if content:
        print("Text (Web Scraping):", content.get_text())


topic_to_search = 0
# Example usage
while topic_to_search != 'bye':
    topic_to_search = input('Enter your prompt: ')
    wikipedia_data_api = get_wikipedia_data_api(topic_to_search)

    if wikipedia_data_api is None:
        print("Trying web scraping...")
        scrape_wikipedia_web(topic_to_search)
