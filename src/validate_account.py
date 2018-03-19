# Validate the account
# Only Fetch data for Public Account

import json
import requests

def validate_profile(handle):
	page = requests.get('https://www.instagram.com' + handle + '/?__a=1')

	if page.status_code != 200:
		print ("Invalid username")
		return True

	page = page.json()
	
	if page['graphql']['user']['is_private']:
		print ("This Account is Private")
		return True
	else:
		return False
