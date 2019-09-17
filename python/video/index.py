import requests
from bs4 import BeautifulSoup
import json
url = "https://youtubemp4.to/download_ajax/"
data = {
    "url": "https://www.youtube.com/watch?v=U6FggaFTQWw",
}
rq = requests.post(url = url, data=data)

print(rq.status_code)
#print(rq.text)
data = json.loads(rq.text)
soup = BeautifulSoup(data['result'], 'html.parser')
liens_first = soup.find(class_='results-primary')
titre = liens_first.find('h2').text
duree = liens_first.find('p').text
lientelechargement = liens_first.find("a",  attrs={'class':  "btn btn-red"})

autre_lien =  soup.find("div",  attrs={'id':  "results-other"})
compt_tbody = 0
#print(autre_lien)
tbo = soup.find_all("tr")
detect = 0
for tbody in tbo:
    tdinfo = tbody.find_all('td')
    print(len(tdinfo))
    if len(tdinfo) < 3:
        detect += 1
        print('Detect =================', detect)
    if detect == 1:
        print(30 * "=V=")
    if detect == 2:
        print(30 * "=V2=")
    if detect == 3:
        print(30 * "=AD=")
    if len(tdinfo) >= 3:
        
        print(tdinfo[0].text , " ", tdinfo[1].text, " ", tdinfo[2].text)
        # print()
        # print(tdinfo[1].text)
        compt_tbody += 1
print(compt_tbody)
#print(tdinfo[2])
# print(titre)  
# print(duree)
# print(lientelechargement.text, "\n" ,lientelechargement.get('href'))
# #print(liens_first)
# nb = 0
# for link in soup.find_all('a'):
#     print(link.get('href'))
#     print(34 * "--")

#     nb += 1

# print(nb)