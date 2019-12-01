import requests
from bs4 import BeautifulSoup

def scrap_snapdeal(query):
  url = "https://www.snapdeal.com/search"
  params = {
    "keyword": query
  }
  r = requests.get(url, params = params)

  soup = BeautifulSoup(r.content)
  products = soup.findAll('div', attrs = {"class": "product-tuple-listing"})

  result = []
  for product in products:
    p = {}
    img = product.find('img')
    if 'src' in img.attrs:
        p['img'] = img.attrs['src']
    else:
        p['img'] = img.attrs['data-src']
    
    title = product.find('p', attrs={"class": "product-title"})
    p['title'] = title.text
    
    price = product.find('span', attrs={"class": "product-price"})
    p['price'] = price.text
    
    result.append(p)
  
  return result
