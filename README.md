# Web Scraping Tool to Find GPU Prices on Newegg.com

This code uses BeautifulSoup and Requests libraries to perform web scraping on Newegg.com to find prices for GPUs (Graphics Processing Units).

## Usage

When you run the program, it prompts the user to input the GPU's name as the search term.

After entering the search term, the program accesses Newegg.com and scrapes all pages for that search term to find GPU prices. The program then outputs the name of the GPU, its price, and a link to the product page.

## Requirements

The code requires the following libraries to be installed:

- BeautifulSoup
- Requests

You can install them using the following commands:
```
pip install beautifulsoup4
pip install requests
```

## How it works

The code performs the following steps:

1. Takes the search term as input from the user.
2. Creates a URL for the search term on Newegg.com.
3. Scrapes the webpage using BeautifulSoup.
4. Finds the total number of pages for that search term.
5. Iterates over each page, scraping the items and prices for the given search term.
6. Stores the data in a dictionary with the item name, price, and link.
7. Sorts the dictionary by price in ascending order.
8. Prints the results.

## Disclaimer

This code is for educational purposes only. Web scraping can be a violation of a website's terms of service or even illegal in some cases. Please use it responsibly and at your own risk.
