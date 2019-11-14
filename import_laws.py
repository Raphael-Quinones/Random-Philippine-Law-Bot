'''Use this to import all of the laws in the website locally'''
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

def gen_link(start_num):
    start_num += 1
    final_num = start_num + 49
    return f"http://www.chanrobles.com/RepublicActs.{start_num}-{final_num}.html"


# Access the list of laws using chrome
#driver = webdriver.Chrome("/home/raphael/chromedriver")

# Get R.A. 1-9500
for i in range(3000,4000):
    if i in range(1, 151):
        link = f"http://www.chanrobles.com/RepublicActNo.{i}.html#.Xc05lVkzbeQ"
    elif i in range(151, 9501):
        link = f" http://www.chanrobles.com/republicacts/republicactno{i}.html"
    #driver.get(link)
    site = requests.get(link).text
    html_site = BeautifulSoup(site,"html.parser")
    parse = html_site.find("div",class_="post").find_all('p')
    for str in parse:
        print(str.text)