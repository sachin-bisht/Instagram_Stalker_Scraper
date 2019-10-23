# Instagram_stalker-scrapper-
Fetch data from any public Instagram profile

### This program download all the post of instagram profile(PUBLIC) and then shows the bar graph of likes of each post _(from older to newer posts)_

First of all, I want to say that this project helped me learn a lot of things about web scraping and many python libraries (some of them aren't used)

Now what this does is, it downloads all the posts(including videos) of any public Instagram account and save it in your current working directory.
And it also shows the bar graph (likes on every post) from older to newer posts.

When I started this project, I googled a lot of things(don't remember) and visited a lot of blogs. Thanks, everyone :)
But there is one blog that tells exactly how to scrape the AJAX part or infinite scrolling of Instagram account.

Infinite Scrolling - https://www.diggernaut.com/blog/how-to-scrape-pages-infinite-scroll-extracting-data-from-instagram/#comment-157

I recommend visiting this blog and google the term that you don't understand from the blog (like XHR and many more).

And one final advice - Go through the _requests_ library if you are programming with __python__.

_Requests Package_ - http://docs.python-requests.org/en/master/user/quickstart/

And if you are interested in plotting graph in python:

_Matplotlib_ - https://matplotlib.org/tutorials/introductory/sample_plots.html

Good Luck!

## Prerequisite:
_Python 3_

_pip(Python Package Index) :_

> $ sudo apt-get install python3-pip

_requests package :_

> $ sudo pip3 install requests

_lxml package :_

> $ sudo apt-get install libxml2-dev libxslt1-dev python-dev

> $ pip3 install lxml

_matplotlib package :_

> $ sudo pip3 install matplotlib

_wget package :_

> $ sudo pip3 install wget

## How to Run:
Run file driver.py in SRC folder
