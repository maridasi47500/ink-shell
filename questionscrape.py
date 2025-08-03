import pandas as pd
import requests
from bs4 import BeautifulSoup
import itertools
#answer human verification  first
from answerscraping import AnswerScraping
class ScrapeSomething():
    def __init__(self,aboutsomething="python"):
        self.something=aboutsomething
        self.scrape=AnswerScraping
        self.alllinks=[]

    def mylinks(self):
        if len(self.alllinks) == 0:
            print("êtes vous sûre d'avoir verifie que vous etes un robot")
            print("sinnon verifier ici https://stackoverflow.com/search?q=routes+flask+python")
        for x in self.alllinks:
            self.scrape(x)

    def custom_selector(self,tag):
    	# Return "span" tags with a class name of "target_span"
    	return tag.name == "a" and tag.has_attr("class") and tag.has_attr("href") and "/questions/" in tag.get("href") and tag.get("href")[-1] != "/"
    def href(self,soup):
        # get all href links from one page 
        href=[]
        #for i in soup.find_all("a",class_="question-hyperlink",href=True):
        for i in soup.find_all(self.custom_selector):
            href.append(i['href'])
        return href
    
    def clean_empty_hrefs(self,hrefs):
       # remove all empty lists
        list_hrefs=[]
        for i in hrefs:
            if i!=[]:
                list_hrefs.append(i)
        # merge all elemenets in one list
        herfs_list=[]
        for i in list_hrefs:
            for j in i:
                herfs_list.append(j)
        return herfs_list
    
    
    def add_prefix(self,herfs_list):
        # rearrage those links who do not have 'https://stackoverflow.com' prefix    
        new_href=[]
        prefix='https://stackoverflow.com'
        for h in herfs_list:
            if 'https' not in h:
                m=prefix+h+"answertab=votes#tab-top"
                new_href.append(m)
            else:
                new_href.append(h+"answertab=votes#tab-top")
        return new_href
    
    
    def single_page_scraper(self,url):
        req=requests.get(url=url)
        soup=BeautifulSoup(req.text,"html.parser")
        return soup
    def single_page_question_answer(self,url):
        page=single_page_scraper(url).find_all("div",class_="s-prose js-post-body",itemprop="text") # this class may vary by the time
        question=[i.find("p").get_text()for i in page][0]
        answer=[i.find("p").get_text() for i in page][1:3]
        
        return question,answer
    
    
    
    def questions_answers(self,start_page,end_page):
        soups=[]
        for page in range(start_page,end_page):
            print("https://stackoverflow.com/search?q="+self.something.replace(" ","+")+"&tab=votes&page={}&pagesize=15")
            req=requests.get(url=("https://stackoverflow.com/search?q="+self.something.replace(" ","+")+"&tab=votes&page={}&pagesize=15").format(page))
            soup=BeautifulSoup(req.text,"html.parser")
            soups.append(soup)
        
        print("Soups are ready!")
        # obtain all href
        hrefs=[]
        for soup in soups:
            print("soups:::::::")
            aa=self.href(soup)
            print(aa)
            hrefs.append(aa)
        herfs_list=self.clean_empty_hrefs(hrefs)
        new_hrefs_list=self.add_prefix(herfs_list)
        print("All hrefs are ready!", new_hrefs_list)
        self.alllinks=new_hrefs_list
        quesitons=[]
        answers=[]
        for url in new_hrefs_list:
            try:
                q,a=self.single_page_question_answer(url)
                quesitons.append(q)
                answers.append(a)
            except:
                pass
        print("quesitons and answers are ready!")
        
        new_answers=[]
        for i in range(len(answers)):
            try:
                new_answers.append(answers[i][0])
            except:
                new_answers.append(None)
        print("All most done!")
        new_q = []
        new_a = []
        merge_answer=list(itertools.chain.from_iterable(answers))
        print(merge_answer)
        for i in range(len(merge_answer) - 1):
            new_q.append(merge_answer[i])
            new_a.append(merge_answer[i+1])
                
        return quesitons+new_q, new_answers+new_a
#g=ScrapeSomething("routes ruby on rails") #english
#o=g.questions_answers(1,5)
#g.mylinks()

