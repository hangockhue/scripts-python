from selenium import webdriver
from bs4 import BeautifulSoup
import csv

driver = webdriver.Chrome('/home/ngockhue/Downloads/chromedriver')
driver.get('https://thegioididong.com/dtdd#i:6')
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

articals = soup.find_all('ul', class_='homeproduct')


def star_mobile(product):
    one_star = len(product.find_all('i', class_='icontgdd-ystar'))
    part_star = len(product.find_all('i', class_='icontgdd-hstar'))
    return one_star + part_star / 2

csv_file = open('product.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product', 'Price', 'Rating'])

for artical in articals:
    for product in artical.find_all('li'):
        print('Product:' + product.a.h3.string)
        print('Price:' + product.div.string)
        print('Rating' + str(star_mobile(product)))
        csv_writer.writerow(
            [product.a.h3.string, product.div.string, star_mobile(product)])
