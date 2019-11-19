'''Use this to import all of the laws in the website locally'''
from bs4 import BeautifulSoup
import requests

num = 0
success=0

def gen_link(start_num):
    start_num += 1
    final_num = start_num + 49
    return f"http://www.chanrobles.com/RepublicActs.{start_num}-{final_num}.html"


# Generate Links
# Get R.A. 1-9500
for i in range(1, 2):
    if i in range(1, 151):
        link = f"http://www.chanrobles.com/RepublicActNo.{i}.html#.Xc05lVkzbeQ"
    elif i in range(151, 9501):
        link = f" http://www.chanrobles.com/republicacts/republicactno{i}.html"
    try:
        # driver.get(link)
        site = requests.get(link).text
        html_site = BeautifulSoup(site, "html.parser")
        parse = html_site.find("div", class_="post").find_all(
            'p')  # finds all paragraph (list object) in div class="post" not yet perfect but workable
        list = [str.text for str in parse]
        list.pop(0)  # removes first index which to let the first loop read the republic act
    except:
        continue
    # removes errors, we can't do anything about those errors anyway
    try:
        if "click" in list[0].lower():
            continue
        else:
            with open("R.A. List\\"+list[0],"w") as file:
                for line in list:
                    file.write(line + "\n")

            #for line in list:
            #    success+=1
            #    print(success)


    except:
        continue
print(success)