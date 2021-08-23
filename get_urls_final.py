#pip install python-csv collections-extended urllib3 pandas beautifulsoup4 requests regex lxml
import requests
from bs4 import BeautifulSoup
import pandas as pd 
from pandas import DataFrame
import re
import requests.exceptions
from urllib.parse import urlsplit
from urllib.parse import urlparse
from collections import deque
import csv

web_crawl = 'top_cv'
if web_crawl =='top_cv':
	content_job = ['div','content-tab']
	content_job_id = ['div', 'col-job-left']
	job_title_class = ['h1', 'job-title text-highlight bold']
	company_title_class = ['div', 'company-title']
	job_deadline_class = ['div','job-deadline']
	location_class = ['div','text-dark-gray']

def crawlTopCV(response, url, save_file):
	try:
		soup = BeautifulSoup(response.content, "html.parser")
	except:
		return
	try:
		body = soup.find(content_job_id[0], id=content_job_id[1])
		h2s = body.find_all('h2')
		content_tab = body.find_all(content_job[0], content_job[1])
		content_texts = ""

		count = 0
		for h2 in h2s:
			content_texts += h2.text + '\n'
			contents = (content_tab[count].findChildren("p", recursive=False))
			for content in contents:
				content_texts += content.text + '\n'
			count+=1

		if content == "":
			print("no content found!")
			return
	except:
		print('content error!')
		return
	try:
		related_works = body.find_all('span')
		related_texts = ""
		for work in related_works:
			a_tags = work.find_all('a', recursive=False)
			for a in a_tags:
				related_texts += a.text + "\n"
	except:
		related_texts = None
	
	try:
		job_title = soup.find(job_title_class[0], job_title_class[1]).text
	except:
		job_title = None

	try:
		company_title = soup.find(company_title_class[0], company_title_class[1]).text
	except:
		company_title = None

	try:
		job_deadline = soup.find(job_deadline_class[0], job_deadline_class[1]).text
	except:
		job_deadline = None

	try:
		location = soup.find(location_class[0], location_class[1]).text
	except:
		location = None
	
	try:
		with open(save_file, mode='a', encoding='utf-8', newline='') as file:
			writer = csv.writer(file, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			writer.writerow([job_title, company_title,job_deadline, location, content_texts, related_texts, url])
		print('done')
	except:
		return

def craw_url(base_url, save_file):

    # a queue of urls to be crawled next
    # a set of urls that we have already processed 
    try:
      with open(save_file, mode='r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        urls = [row[-1]for row in reader]
        processed_urls = set(urls)
        new_urls = deque(urls+[base_url])
    except:
      new_urls = deque([base_url])
      processed_urls = set()
    # a set of domains inside the target website
    local_urls = set()
    # a set of domains outside the target website
    foreign_urls = set()
    # a set of broken urls
    broken_urls = set()
    print(len(processed_urls))
    print(len(new_urls))
    # process urls one by one until we exhaust the queue
    while len(new_urls):  
      # move url from the queue to processed url set    
      url = new_urls.popleft()
      # print the current url    
      try:    
        response = requests.get(url)
      except:
        print("no response")   
        # add broken urls to it’s own set, then continue    
        continue
      # print the current url 
      print("Processing %s" % url)
      if url not in processed_urls:
        if web_crawl == 'top_cv':
          crawlTopCV(response, url, save_file)
      else:
        print('already crawled')
      processed_urls.add(url)
      # extract base url to resolve relative links
      parts = urlsplit(url)
      base = "{0.netloc}".format(parts)
      strip_base = base.replace("www.", "")
      base_url = "{0.scheme}://{0.netloc}".format(parts)
      path = url[:url.rfind('/')+1] if '/' in parts.path else url
      soup = BeautifulSoup(response.text, "lxml")
      for link in soup.find_all('a'):    
        # extract link url from the anchor 
        anchor = link.attrs["href"] if "href" in link.attrs else ''
        if anchor.startswith('/'):        
          local_link = base_url + anchor        
          #local_urls.add(local_link)    
        elif strip_base in anchor: 
          local_link = anchor       
          #local_urls.add(anchor)    
        elif not anchor.startswith('http'):        
          local_link = path + anchor        
          #local_urls.add(local_link)   

        local_urls.add(local_link)
        if not local_link in new_urls and not local_link in processed_urls:        
          new_urls.append(local_link)

if __name__ == '__main__':
    #base_url = 'https://vnexpress.net/'
    #base_url = 'https://zingnews.vn/'
    #base_url = 'https://dantri.com.vn/'
    base_url = 'https://www.topcv.vn/'

    #save_file = 'hanoimoi.csv'
    #save_file = 'zingnews.csv'
    save_file = 'topcv.csv'
	
    with open(save_file, mode='a', encoding='utf-8', newline='') as file:
      writer = csv.writer(file, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      writer.writerow(['job_title','company_name','job_deadline','location','content','type_of_job','url'])
    craw_url(base_url, save_file)