import bs4
import requests
import webbrowser

response = requests.get('https://es.wikipedia.org/wiki/An%C3%A1lisis_de_componentes_principales')

soup = bs4.BeautifulSoup(response.text, 'html.parser')

links = soup.select('a')

links = [link.attrs.get('href') for link in links]

#delete none object in links
del links[0]

links = [link for link in links if (link.startswith('http') and '.pdf' in link)] 

for i in range(len(links)):
	webbrowser.open(links[i])

