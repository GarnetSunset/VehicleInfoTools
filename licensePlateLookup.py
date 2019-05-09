def lookup(plate,state):

	import requests
	import time
	from bs4 import BeautifulSoup

	
	
	cookies = {
		'abtest': '1',
		'ref': 'www.google.com',
	}

	headers = {
		'Connection': 'keep-alive',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'Referer': 'https://www.google.com/',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'en-US,en;q=0.9',
	}

        doesitpass=False
        data = []
	
	params = (
		('plate', plate),
		('state', state),
	)

	response = requests.get('https://www.faxvin.com/license-plate-lookup/decoding', headers=headers, params=params, cookies=cookies)
	print("Waiting for a response...")
	time.sleep(10)
	#Caching a result
	response = requests.get('https://www.faxvin.com/license-plate-lookup/result', headers=headers, params=params, cookies=cookies)
	soup = BeautifulSoup(response.text, 'lxml')
	try:
		table = soup.find_all('table')[0]
		doesitpass=True
	except:
		print("The lookup has failed, are you sure your plate is correct?")
	if(doesitpass):
		rows = table.findAll('tr')
		lists = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]
		for i in lists:
                        data += i
		return data
