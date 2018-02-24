import matplotlib.pyplot as plt


# Display the bar graph
# Showing likes of each post from older to newer post

def plotBargraph(shortcodes, handle):
  likes = []

  for like in shortcodes:
    likes.append(like['likes'])

  likes = likes[::-1]
  ind = list(range(len(likes)))

  plt.bar(ind, likes, edgecolor = 'black', linewidth = .5)
  plt.xlabel('Posts')
  plt.ylabel('Like Count')
  plt.title(handle)
  plt.show()
