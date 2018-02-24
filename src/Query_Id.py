import requests
from lxml import html

main_url = 'https://www.instagram.com'
scroll_link = '/graphql/query/?'

# Gets the query_id of the profile
# which helps afterwards in infinte scrolling

def getQueryId(url):
  main_url = 'https://www.instagram.com'

  page = requests.get(url)
  data = html.fromstring(page.content)
  link = data.xpath("//head/link[@rel = 'preload']/@href")
  page = requests.get(main_url + link[0]).text
  ind = page.find('queryId')
  ind += 9
  ind = page.find('queryId', ind)
  ind += 9
  st_ind = ind
  lst_ind = page.find('"', ind)
  return page[st_ind:lst_ind]
