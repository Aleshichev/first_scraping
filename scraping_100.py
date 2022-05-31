from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
text_html = response.text
# print(text_html)

soup = BeautifulSoup(text_html, "html.parser")

all_h3_list = soup.find_all(name="h3", class_="title")
# print(all_h3_list)
# text_h3_titels = []
# for title_text in all_h3_list:
#     text = title_text.getText()
#     text_h3_titels.append(text)
text_h3_titels = [title_text.getText() for title_text in all_h3_list]
titel = text_h3_titels[::-1]

with open('movies.txt', 'w', encoding='utf-8') as f:
    for x in titel:
        f.write(f"{x}\n")
