from bs4 import BeautifulSoup
import urllib.request

if __name__ == "__main__":
	idx = 1
	for i in range(27):
		req = urllib.request.Request("https://www.tlj.co.kr:7008/store/search.asp?sido=%BC%AD%BF%EF%C6%AF%BA%B0%BD%C3&gugun=&keyword=&page="+str(i+1));
		data = urllib.request.urlopen(req).read()
		bs = BeautifulSoup(data, 'html.parser')

		l = bs.find_all('tr')
		file = open("parseddata.txt", "w")
		for s in l:
			try:
				if str(s.get_text()):
					print(s.get('data-lat'), ", ", s.get('data-lng'))
					print("%d : %s" % (idx, str(s.get_text())))
					file.write("%d : %s" % (idx, str(s.get_text())))
					with open("tours.txt", "a") as myfile:
						myfile.write("%s, %s" % (s.get('data-lat'), s.get('data-lng')))
						myfile.write("%d : %s" % (idx, str(s.get_text())))
			except UnicodeEncodeError:
				print("Errror : %d" % (idx))
			finally:
				idx += 1
