from bs4 import BeautifulSoup
import requests
import re

gpu = input("What GPU do you want to search for? ")

url = f"https://www.newegg.com/p/pl?d={gpu}&N=4131"

page = requests.get(url).text

doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong


print(page_text)

