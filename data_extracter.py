from bs4 import BeautifulSoup

with open("places.html", encoding="utf-8") as file: ##nem ez lenne a hivatalos de csak így nyitja meg anélkül hogy az encoding miatt sír, look into why the built in encoding switch doesn't work!
    soup = BeautifulSoup(file, "html.parser")

div = soup.find("div", class_="col-12 col-sm-12 col-md-9 col-xl-7") ##ide kell majd a find_all() hogy az összes ilyen div meglegyen
name = div.find("h3", class_="job-listing-title").get_text(strip=True) 

print(soup)