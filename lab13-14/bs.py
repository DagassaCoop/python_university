import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import re

class Article:
    def __init__(self,title = None,company = None,description = None,price = None,location = None):
        self.title = title
        self.company = company
        self.description = description
        self.price =price
        self.location = location

    def __str__(self):
        return f'Article: {self.title}, {self.company}, {self.description}, {self.price}, {self.location}'

    def __repr__(self):
        return f'Article: {self.title}, {self.company}, {self.description}, {self.price}, {self.location}'

# URL = 'https://ua.jooble.org/SearchResult'
URL = 'https://ua.jooble.org/SearchResult?ukw=data%20scientist'
response = requests.get(URL)
soup =  bs(response.text,'lxml')


titles = soup.find_all('span', class_='_1b9db')
companies = soup.find_all('p', class_='e2601')
descriptions = soup.find_all('div', class_='_10840')
prices = soup.find_all('p', class_='a7943')
locations = soup.find_all('div', class_='caption d7cb2')

# data = {'Title': titles,'Company':companies,'Description':descriptions,'Price':prices,'Location':locations}

articles = []
firstSelectArticles = []
finishArticles = []

def articleInDataFrame(articles):
    titles = []
    companies = []
    descriptions = []
    prices = []
    locations = []
    for i in articles:
        titles.append(i.title)
        companies.append(i.company)
        descriptions.append(i.description)
        prices.append(i.price)
        locations.append(i.location)
    data = {'Title': titles,'Company':companies,'Price':prices,'Location':locations}
    return pd.DataFrame(data,columns=['Title','Company','Price','Location'])

def createArticlesArr(titles,compaties,descriptions,prices,locations):
    valueArr = [len(titles), len(companies), len(descriptions), len(prices), len(locations)]
    minRange = valueArr[0]
    for i in valueArr:
        if minRange > i:
            minRange = i
    for i in range(minRange):
        art = Article()
        art.title = titles[i].text
        art.company = compaties[i].text
        art.description = descriptions[i].text
        art.price = prices[i].text
        art.location = locations[i].text
        articles.append(art)

def init():
    for i in articles:
        index_price = i.price
        if re.search(r'-',index_price):
            minPrice = int(''.join(re.findall('\d',index_price.split('-')[0])))
            if minPrice > 1000:
                firstSelectArticles.append(i)
        else:
            minPrice = int(''.join(re.findall('\d',index_price)))
            if minPrice > 1000:
                firstSelectArticles.append(i)
    for i in firstSelectArticles:
        index_title = i.title
        if re.search(r'',index_title):
            finishArticles.append(i)
    dataFrame = articleInDataFrame(finishArticles)
    dataFrame.to_csv('res.csv',encoding='cp1251',index=False,header=True)
    print(dataFrame)



createArticlesArr(titles,companies,descriptions,prices,locations)
init()
# cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
#         'Price': [22000,25000,27000,35000]
#         }
#
# df = pd.DataFrame(cars, columns= ['Brand', 'Price'])
# df.to_csv('test.csv',index=False,header=True)
# print (df)

