'''A web scraper I wrote for scraping and downloading data from a directory listing website.
My use case was to compare the urls files to a repository and download the files that were not included in the repository.
I have replaced some of private data like folder names or urls with placeholders in this script.'''

'''To know whether a website allows web scraping or not, you can look at the website’s “robots.txt” file. 
You can find this file by appending “/robots.txt” to the URL that you want to scrape. '''

import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

import re
import os
from pathlib import Path

#init session
'''creates a session-object that is better suited for making several requests to a same host than regular requests.get connection'''
session = requests.Session()

#add & mount an adapter with retry options to session
retry = Retry(connect = 3, backoff_factor = 0.5) 
'''connect: how many connection-related errors to retry on, 
backoff_factor: A backoff factor to apply between attempts. urllib3 will sleep for:
{backoff factor} * (2 ^ ({number of total retries} - 1))'''

adapter = HTTPAdapter(max_retries = retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

#result list
results = []

#folder list
'''I got this list of folders from the url when reading the req.text for the first time. 
It's possible to remodel the regex parsing presented below to get this list for any other website that's listing directories.'''

flist = ["0-9/", "a-c/", "compilations/", "d-f/", "g-i/", "j-l/", "m-o/", "p-r/", "s-u/", "v-z/"]

#get files
for endpoint in flist:
   url = f"https://www.insert_url_here/{endpoint}"
   req = session.get(url)
   txt = req.text
   #parse and add results to a list. findall returns a list so the contents of each folder will be stored inside a separate list
   p = r'href="(\w*)\.zip'
   res = re.findall(p, txt)
   results.append(res)

#get current repo
tpath = Path("E:/directory_name_here/subdirectory")
repo =  ([name for name in os.listdir(tpath)])

#download missing files
i = 0
for dir in results:
    for file in dir:

        #check if repository is missing the file
        if file not in repo:

            #download
            dlpath = Path(f"C:/downloads_folder/{file}")
            url = f"https://www.insert_url_here/{flist[i]}{file}.zip"
            req = session.get(url)

            print(f"Downloading file: {url}")

            with open(f"{dlpath}.zip", 'wb') as filename: #'b': binary mode for non-text files
                filename.write(req.content) 
    
    #move on to the next folder
    i += 1