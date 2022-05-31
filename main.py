from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
articles = soup.find_all(name="a", class_="titlelink")  # получить ссылку
article_texts = []
article_links = []
for article_tag in articles:
   text = article_tag.getText()
   article_texts.append(text)        # все заголовки получить текст
   link = article_tag.get("href")
   article_links.append(link)     # все ссылки получить

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_number = max(article_upvotes)           #находим максимальное число
largest_index = article_upvotes.index(largest_number)       #индекс максимального числа
print(largest_index)
print(article_texts[largest_index])
print(article_links[largest_index])
# print(article_upvotes)
# print(int(article_upvotes[0]))






#----------------------------------- Teaching ---------------------------------------#
# import lxml    soup = BeautifulSoup(contens, 'lxml.parser')
#
# with open("website.html") as file:
#    contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.string)
# print(soup.title.name)
# print(soup.prettify())
# print(soup.find_all(name="a"))
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

#
# heading = soup.find(name="h1", id="name")
# print(heading)

# company_url = soup.select_one(selector="#name")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)