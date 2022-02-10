# Imports
from bs4 import BeautifulSoup
import requests

# Variables
page1 = "https://greenakku.de/selfPV:::1.html"
page2 = "https://sonnstrom.com/collections/balkonkraftwerke-balkonmodule-mini-solaranlage/products/balkonkraftwerk-750w"
page3 = ""

# Functions
def scraping_greenakku(homepage):
    soup = BeautifulSoup(requests.get(homepage).content, "html.parser")
    result1 = soup.find_all("span", class_="new_price")
    result2 = soup.find_all(class_="pname")

    for i in range(0, len(result1)):
        extract_text = (result2[i].text.strip())
        extract = (result1[i].text.strip())
        print(extract_text)
        print(extract[:-4])

def scraping_homepage2(homepage):
    soup = BeautifulSoup(requests.get(homepage).content, "html.parser")
    result = soup.find_all("h1", class_="product-single_title")
    print(result[:])


# Run snipplets
if __name__ == '__main__':
    #scraping_greenakku(page1)
    scraping_homepage2(page2)