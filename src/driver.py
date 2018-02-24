import sys
import display_graph as dgr
import data_fetch as df
import download_post as dp
import validate_account as va

def main():
  handle = input("Enter the profile name: ")
  handle = '/'+handle

  if va.validate_profile(handle):
  	sys.exit(0)

  shortcodes = df.getPostInfo(handle)

  dp.downloadPost(shortcodes, handle)
  
  dgr.plotBargraph(shortcodes, handle)

if (__name__ == "__main__"):
  main()
