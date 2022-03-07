#!/bin/python3
import requests
import sys
from urllib.parse import unquote
from bs4 import BeautifulSoup as bs

# URI = "https://cloud.piracy.wiki/KnightLiteKing/[AnimeKuro] Family Guy [x265 10-bit HEVC] [KLK]/[AnimeKuro] Family Guy Season 15 [480p] [KLK]"

URI = 'https://pauladaunt.com/books/'

"""
        Signature: 
                String -> String
        Purpose:
                Take a String URL and Sends an HTTP Request to that URL and parse the returned html
                and return a string representation of that html page
"""

def grab_html(url):
        res = requests.get(url)
        return res.text

def download_file(url, content):
        parsed_html = bs(content, features="lxml")
        anchor_tags = parsed_html.body.findAll("a")

        for a in anchor_tags:
                if(a.attrs['href'].endswith('.mp4')):
                        print("downloading {0}".format(a.attrs['href']))
                        req = requests.get(url + "/" + a.attrs['href'])
                        f = open(a.attrs['href'], 'wb')
                        f.write(req.content)
                        f.close()
                else:
                        print("Skipping {0} ...".format(a.attrs['href']))


def main():
        try:
                if(len(sys.argv) != 2):
                        print("Usage: {0} <URL>".format(sys.argv[0]))
                        exit(-1)

                url = unquote(sys.argv[1])
                # grabing html
                print("Scanning the Html Page ...")
                content = grab_html(url)

                # downloading the files
                print("Starting to Download the files ...")
                download_file(url, content)
        except Exception:
                print("error occured")
        except KeyboardInterrupt:
                print("Bye Bye ya Monsef")

main()