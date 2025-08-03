import requests
import os
import time
from bs4 import BeautifulSoup
import json


class AnswerScraping():
    def __init__(self,urlquestion="https://stackoverflow.com/questions/1"):
        print(urlquestion)
        global last
        last=int(open("last","r").read())
        print(last)
        
        global data
        with open('data.json') as json_file:
             data = json.load(json_file)
        n=urlquestion.split("/")[4]
             
        op=open('last','w')
        op.write(str(n))
        op.close()
        if len(data)%5==0:
                    
           jj=open("data.json","w")
           json.dump(data,jj)
           jj.close()
           print("data upgraded","|| data length:",len(data))
           print("total questions:",len(data))
        
        r=requests.get(urlquestion)
        soup=BeautifulSoup(r.content, 'html.parser')
        l=soup.find_all("title")
        print(l)
        m=soup.find_all("div", {"class": "s-prose js-post-body"})
        title=l[0].text
        if m==[]:
           pass
        else:
             answer=m[1].text
             if "Page not found - Stack Overflow" in title:
                pass
             else:
                  title=title.replace(" - Stack Overflow","")
                  
                  data.update({title:answer})
                  print(str(n),"Done")
                  
                       
                  
        
        time.sleep(5)


