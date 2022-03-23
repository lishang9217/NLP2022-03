# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 02:12:14 2022

@author: lisha
"""

import requests
from bs4 import BeautifulSoup


def ptt_scraping(url):
    articles = []
    r = requests.get(url=URL, cookies={"over18":"1"})
    soup = BeautifulSoup(r.text, "lxml")
    tag_divs = soup.find_all("div", class_="r-ent")
    for tag in tag_divs:
        if tag.find("a"):
            href = tag.find("a")["href"]
            title = tag.find("a").text
            
            r2=requests.get(url="http://ptt.cc"+href, cookies={"over18":"1"})
            soup2 = BeautifulSoup(r2.text, "lxml")
            
            meta_spans = soup2.find_all("span", class_="article-meta-value")
            
            if (meta_spans != []):
                date_span = meta_spans[-1]
                
            
            articles.append({"title":title, "href":href, "text":soup2.text, "date": date_span.text})
    return articles

import jieba.posseg 
import time

target_date = "Mar 11" #Feb 14

for i in range(3545,3551):
    URL = "http://ptt.cc/bbs/creditcard/index%d.html" % i #Lifeismoney
    print("URL", URL)

    articles = ptt_scraping(url=URL)
    for article in articles:    
        
        filename = article["href"].split("/")[-1]
        print("full-href", URL[:13] + article["href"])

        with open(file="creditcard/"+target_date+"/"+filename+".txt", mode="w", encoding="utf8") as file1:
            tagged_words = jieba.posseg.cut(article["text"])
            words = [word for word, pos in tagged_words if pos not in ["m"]]
            file1.write(article["date"]+"\n")
            file1.write(" ".join(words))
            print(article["date"], " ".join(words).strip()[:22])
            
    time.sleep(3)