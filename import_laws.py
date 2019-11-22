'''Use this to import all of the laws in the website locally'''
from bs4 import BeautifulSoup
import requests

num = 0
success = 0


def clean_title2(i, title):
    # len("Republic Act. No. 1") is 18
    # len("Republic Act. No. 21") is 19
    # and so on...
    length = len(str(i))
    if length == 1:
        new_title = title[:18]
    elif length == 2:
        new_title = title[:19]
    elif length == 3:
        new_title = title[:20]
    return new_title


# Generate Links
# Get R.A. 1-9500
for i in range(1, 100):
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
        # Cleanse first line (title); removes dates
        list[0] = clean_title2(i, list[0])

    except:
        continue
        # removes errors, we can't do anything about those errors anyway
    try:
        # click string exists when R.A. isn't there
        if "click" in list[0].lower():
            continue
        else:
            with open(list[0], "w") as file:
                for line in list:
                    file.write(line + "\n")

    except:
        continue
print(success)
