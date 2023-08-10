from bs4 import BeautifulSoup
import requests
import re


def scrape_newegg_products(search_term):
    items_found = {}

    #Request url data
    url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    #Page number
    page_text = doc.find(class_="list-tool-pagination-text").strong
    
    #Split the page text to just print out the max page number
    pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

    #Loop through all of the pages to find all results for search
    for page in range(1, pages+1):
        url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131&page={page}"
        page = requests.get(url).text
        doc = BeautifulSoup(page, "html.parser")
        div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")

    #Grabbing the text from the product
    items = div.find_all(text=re.compile(search_term))

    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue

        
        link = parent['href']
        next_parent = item.find_parent(class_="item-container")

        #Check if srtong tag exists before accessing the text
        try:
            price = next_parent.find(class_="price-current").strong.string
            items_found[item] = {"price": int(price.replace(",", "")), "link": link}
        except:
            pass

    return items_found