"""
Author      : Sambhaji Shedole
Created At  : 09 July 2019
Description : This is sample flask application with sample API
              to get current data like product name and price from amazon url.
Dependancies: "https://www.amazon.in/s?k=%3Ccoke%3E"
"""


#from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import bs4


import urllib.request
#import  pandas as pd
import html5lib
from flask import Flask, request, jsonify
import json

webs = Flask(__name__)
webs.config["DEBUG"] = True

@webs.errorhandler(404)
def page_not_found(e):
    return jsonify({ "status": "404","data" : "Page Not Found!" })


url = "https://www.amazon.in/s?k=%3Ccoke%3E"
r = requests.get(url)
r.text
#print(r.content)
soup = bs4.BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
products = []
for div in soup.find_all('div', {'class':'a-section a-spacing-medium'}): # to find main div class to find product name and price
    productNameAll = div.find('span', {'class':'a-size-medium a-color-base a-text-normal'}) # to find product name from span
    priceAll = div.find('span', {'class':'a-price-whole'}) # to find price of specific product from span class
    productName = 'Blank' # initiliziting varibles
    priceOfProduct = '0'
    if(productNameAll != None): # check wheather given varible value is not null
        productName = productNameAll.text
        #print(productName)
    if(priceAll != None):
        priceOfProduct = priceAll.text
        #print(priceOfProduct)
    #print(productName)

    productDetails = {  # create Json format to given product list
        productNameAll : productName,
        priceAll : float(priceOfProduct.replace(',', ''))
    }
    products.append(productDetails) # use to append all product details like product name and price

print(products) # final list of product save in product list


@webs.route('/api/v1/resources/products/all', methods=['GET'])
def get_product_details(): # providing list to json by using jsonify function
    results = {
                'status' : '200',
                'ProductDetails': products
            }
    return jsonify(results)

if __name__ == "__main__":
    webs.run(host="0.0.0.0", port=8080)