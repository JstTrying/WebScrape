import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse
import pandas as pd

def scrape_headings(url):
    try:
        # Check if the URL has a scheme (http/https), and add one if missing
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            url = urlunparse(('http',) + parsed_url[1:])

        # Send an HTTP GET request to the specified URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all the heading elements (h1, h2, h3, etc.)
            headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

            # Extract and print the text from the headings and put to csv
            heading_list = [heading.text for heading in headings]
            df = pd.DataFrame(heading_list)
            df.to_csv('output.csv')

        else:
            print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


# To check if to do another search for URL
def main_start():

    if __name__ == "__main__":
        url = input("Enter the URL: ")
        scrape_headings(url)
        # df = pd.DataFrame(scrape_headings(url))
        search_again = input("Do you want to search again? y/n:").lower()
        if search_again == 'y':
            # df.to_csv('output.csv')
            main_start()
        else:
            # df.to_csv('output.csv')
            exit()


main_start()

