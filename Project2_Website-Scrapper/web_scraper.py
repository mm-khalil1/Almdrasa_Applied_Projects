# Code to scraping books.toscrape.com website

## Pseudo code:
# get website
# get requirements: title and rating
# title can be found in h3 under li class after "title="
# rating can be found in p class under li class after "star-rating "

import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    list_items = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

    books = []
    for lst in list_items:
        h3_element = str(lst.find('h3'))
        title_start_index = h3_element.find("title=") + 7
        title_end_index = h3_element.find('"')
        title = h3_element[title_start_index : title_end_index]
        
        rating_begin = str(lst).split("star-rating ")[1]
        rating = rating_begin[ : rating_begin.find('">')]
        
        book = {'title': title, 'rating': rating}
        books.append(book)
    
    for book in books:
        print(f"Book Title: {book['title']}. \nStar Rating: {book['rating']}\n")
