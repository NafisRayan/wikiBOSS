import wikipediaapi
import requests
from bs4 import BeautifulSoup

def get_wikipedia_data_api(topic, language='en'):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    
    headers = {'User-Agent': user_agent}
    try:
        wiki_wiki = wikipediaapi.Wikipedia(language, headers=headers)
        page_py = wiki_wiki.page(topic)

        if not page_py.exists():
            print(f"Page '{topic}' does not exist.")
            return None

        print("Title:", page_py.title)
        return page_py.text
    except Exception as e:
        print(f"Error fetching data from Wikipedia API: {e}")
        return None

def scrape_wikipedia_web(topic):
    base_url = "https://en.wikipedia.org/wiki/"
    url = base_url + topic.replace(" ", "_")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    
    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', {'id': 'mw-content-text'})

        if content:
            return content.get_text()
    except Exception as e:
        print(f"Error fetching data via web scraping: {e}")
        return None

def chatbot():
    print("Hello! I'm a Wikipedia-based chatbot. Ask me anything. Type 'bye' to exit.")
    
    while True:
        user_input = input('You: ')
        
        if user_input.lower() == 'bye':
            print("Goodbye!")
            break

        wikipedia_data_api = get_wikipedia_data_api(user_input)

        if wikipedia_data_api is not None:
            print("Chatbot:", wikipedia_data_api)
        else:
            print("Chatbot: I couldn't find information. Let me try web scraping...")
            web_data = scrape_wikipedia_web(user_input)
            if web_data:
                print("Chatbot (Web Scraping):", web_data)
            else:
                print("Chatbot: I'm sorry, I couldn't find information on that topic.")

chatbot()
