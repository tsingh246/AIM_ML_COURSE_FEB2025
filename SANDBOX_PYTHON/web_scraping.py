import requests
from bs4 import BeautifulSoup
import numpy as np
from IPython.core.display import clear_output

images = []

for i in ddf['link']:
  r = requests.get(i)
  soup = BeautifulSoup(r.content, "html.parser")
  try:
    image_url = page_html.find('div', class_='poster').img['src']
  except:
    image_url = np.nan
  images.append(image_url)
  print(image_url)
  clear_output(wait=True)