# coding:utf-8
from bs4 import BeautifulSoup
import re
import requests
from time import sleep
import bibtexparser
import json


# URLを指定して、HTMLを取得する
url = ""
# urlの例
# url = "https://aclanthology.org/events/rocling-2021/"

html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
# print(url.split("/")[-2])

# bibファイルへのリンクを取得する
bib_links = soup.find_all("a", {"href": lambda x: x.endswith(".bib")})
# print(bib_links)

papers = []
base_url = "https://aclanthology.org"  # 適切な基本URLに変更してください

for bib_link in bib_links:
    # print(bib_link["href"])
    if "full" in bib_link.text.lower():
        print(bib_link.text.lower())
        continue

    # フルURLに変換
    full_url = base_url + bib_link["href"]

    # ファイルのダウンロード
    response = requests.get(full_url)
    bib_database = bibtexparser.loads(response.text)
    # print(bib_database.entries)
    papers.extend(bib_database.entries)

    # print(papers)
    sleep(1)

with open(url.split("/")[-2] + ".json", "w") as f:
    json.dump(papers, f, indent=4)
