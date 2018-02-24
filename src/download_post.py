import json
import requests
import os
import wget

# Download all the posts(video, image(s))
# Store it in the ./insta_img directory

def downloadPost(shortcodes, handle):
  main_url = 'https://www.instagram.com'
  scroll_link = '/graphql/query/?'

  if not os.path.exists('./insta_img'):
    os.makedirs('./insta_img')
  if not os.path.exists('./insta_img'+handle):
    os.makedirs('./insta_img'+handle)

  for i in range(len(shortcodes)-1, -1, -1):
    if not shortcodes[i]['is-video']:
      if shortcodes[i]['typename'] != 'GraphSidecar':
        name = './insta_img'+handle + '/post' + str(len(shortcodes)-i) + '.jpg'
        wget.download(shortcodes[i]['display-url'], name)
      else:
        page = requests.get(main_url + '/p/' + shortcodes[i]['shortcode'] + '/?__a=1').json()
        for j in range(len(page['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'])):
          name = './insta_img'+handle + '/post' + str(len(shortcodes)-i) + '_' + str(j+1) + '.jpg'
          wget.download(page['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][j]['node']['display_url'], name)

    else:
      name = './insta_img'+handle + '/post' + str(len(shortcodes)-i) + '.mp4'
      page = requests.get(main_url + '/p/' + shortcodes[i]['shortcode'] + '/?__a=1').json()
      wget.download(page['graphql']['shortcode_media']['video_url'], name)
