#!/bin/python3
import requests
from bs4 import BeautifulSoup as bs

def grab_content():        
        url = "http://index-of.es/Cracking"
        #url = "http://192.168.1.4:8000/sql"
        headers = {
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Upgrade-Insecure-Requests":"1"
                }

        links = [url]

        for link in links:
                if(not link.endswith("/")):
                        req = requests.get(url + "/" + link, headers = headers)
                        print("GET {} {}".format(url + link, req.status_code))
                        links.pop()
                        content = req.text
                        if(link.endswith('.pdf') or link.endswith('.chm')):
                                f = open(link, 'wb')
                                f.write(req._content)
                                f.close()
                                print("saving a file ...")
                        else:
                                parsed_html = bs(content, features="lxml")
                                anchor_tags = parsed_html.body.findAll("a")
                                #getting all the links
                                for a in anchor_tags:
                                        links.append(a.attrs['href'])
                                        print('{} found a link adding it ...'.format(a.attrs['href']))

grab_content()
