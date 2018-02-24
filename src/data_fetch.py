import json
import requests
import time

import Query_Id as QId

# Fetches all the data of all the post

def infinteScrolling(query_hash, id, after):
  main_url = 'https://www.instagram.com'
  scroll_link = '/graphql/query/?'

  parameters = 'query_hash=' +str(query_hash)+ '&variables={"id":"' +str(id)+ '","first":12,"after":"' +str(after)+ '"}'
  page = ""
  var = 40
  while(1):
    page = requests.get(main_url + scroll_link + parameters, headers = {'User-agent': 'try ;__;'})
    if(page.status_code == 200):
      page = page.json()
      return page
    
    elif(page.status_code == 429):
      time.sleep(var)
      var += 10
      

def getShortcodes(query_hash, id, after):
  
  shortcodes = []
  
  while(1):
    page = infinteScrolling(query_hash, id, after)

    for i in range(len(page['data']['user']['edge_owner_to_timeline_media']['edges'])):
      shortcode = page['data']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['shortcode']
      likes = page['data']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_preview_like']['count']
      comments = page['data']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_to_comment']['count']
      display_url = page['data']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['display_url']
      is_video = page['data']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['is_video']
      typename = page['data']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['__typename']

      info = {}
      info['shortcode'] = shortcode
      info['likes'] = likes
      info['comments'] = comments
      info['display-url'] = display_url
      info['is-video'] = is_video
      info['typename'] = typename
      shortcodes.append(info)
    

    if page['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']:
      after = page['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
    else:
      break

  return shortcodes


def getPostInfo(handle):
  main_url = 'https://www.instagram.com'
  scroll_link = '/graphql/query/?'

  profileP_json = requests.get(main_url + handle + '/?__a=1').json()
  profile_id = profileP_json['user']['id']
  end_cursor = profileP_json['user']['media']['page_info']['end_cursor']
  profile_query_id = QId.getQueryId(main_url+handle)
  
  post_info = []
  shortcodes = []
  
  for i in range(len(profileP_json['graphql']['user']['edge_owner_to_timeline_media']['edges'])):
    shortcode = profileP_json['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['shortcode']
    likes = profileP_json['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_liked_by']['count']
    comments = profileP_json['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_to_comment']['count']
    display_url = profileP_json['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['display_url']
    is_video = profileP_json['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['is_video']
    typename = profileP_json['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['__typename']

    info = {}
    info['shortcode'] = shortcode
    info['likes'] = likes
    info['comments'] = comments
    info['display-url'] = display_url
    info['is-video'] = is_video
    info['typename'] = typename
    shortcodes.append(info)

  #this function will gather all the shortcodes that comes after the scrolling
  temp_shortcodes = getShortcodes(profile_query_id, profile_id, end_cursor)

  shortcodes += temp_shortcodes
  return shortcodes
