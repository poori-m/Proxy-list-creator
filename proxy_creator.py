from bs4 import BeautifulSoup
import requests


def extrate_proxy():
	proxies=[]
	link = "https://www.sslproxies.org/"
	
	r=requests.get(link)
	s=BeautifulSoup(r.text,"html.parser")
	for i in s.find_all("tr")[ :100]:
		try:
			data=i.find_all("td")
			address=data[0].text
			port=data[1].text
			type_=data[4].text
			proxy=address+":"+port
			proxies.append(proxy)
		except:
				pass
	return proxies

proxy=extrate_proxy()
i=0
f=open("proxy.txt","w")
while i<len(proxy):
	f.write(str(proxy[i]))
	f.write("\n")
	i+=1
f.close()

print ("proxy list created!")
