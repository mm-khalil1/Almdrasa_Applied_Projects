# Created by ChatGPT

import requests
from bs4 import BeautifulSoup

# Example URL of the website to scrape
url = "https://books.toscrape.com"

# Send an HTTP request to the URL and get the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content with BeautifulSoup using 'html.parser'
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <li> elements with the specified class
list_items = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

# Create a list to store book information as dictionaries
books = []

# Extract and store title and star rating for each book
for li in list_items:
    # Extract title from <h3> element
    h3_element = li.find('h3')
    title = h3_element.a['title'] if h3_element and h3_element.a else 'Title Not Found'
    
    # Extract star rating from <p> element with class 'star-rating'
    star_rating_element = li.find('p', class_='star-rating')
    star_rating = star_rating_element['class'][1] if star_rating_element else 'Star Rating Not Found'
    
    # Store book information in a dictionary
    book_info = {'title': title, 'star_rating': star_rating}
    
    # Add the dictionary to the list of books
    books.append(book_info)

# Print the stored book information
for book in books:
    print(f"Title: {book['title']}, Star Rating: {book['star_rating']}")
