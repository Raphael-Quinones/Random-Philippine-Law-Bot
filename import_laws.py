'''Use this to import all of the laws in the website locally'''
from selenium import webdriver
def gen_link(start_num):
    start_num+=1
    final_num=start_num+49
    return f"http://www.chanrobles.com/RepublicActs.{start_num}-{final_num}.html"
#Access the list of laws using chrome
driver = webdriver.Chrome("/home/raphael/chromedriver")
#url = "http://www.chanrobles.com/RepublicActsmain.html"
#driver.get(url)
start_num=0
final_num=0
while start_num <= 9451: #used for R.A. 1 to 9451 because their intervals are 49
    start_num=final_num+1
    final_num=start_num+49
    link = f"http://www.chanrobles.com/RepublicActs.{start_num}-{final_num}.html"
    driver.get(link)





