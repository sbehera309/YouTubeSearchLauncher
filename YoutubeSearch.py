import urllib.request
import urllib.parse
import re
import webbrowser

##Opens video page by the URL structure of YOUTUBE instead of its API.
##

query_string = urllib.parse.urlencode({"search_query" : "hold me"})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
print("http://www.youtube.com/watch?v=" + search_results[0])
new = 2
url = "http://www.youtube.com/watch?v=" + search_results[0])
webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url, new=new)
