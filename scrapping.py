import imp
import requests
from bs4 import BeautifulSoup as bs

user_name = 'Emmanuel Owdero'  #input("Enter your username")
url = "https://github.com/" + user_name #input("Enter the site of the URL")
results = requests.get(url)

soup = bs(results.content,"html.parser")
profile_pic = soup.find('img',{'alt':'Avatar'})['src']
print(profile_pic)





















