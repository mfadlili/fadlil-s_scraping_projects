import requests
from bs4 import BeautifulSoup

def ambil_data():
    try : 
        data = requests.get('https://www.bmkg.go.id/')
    except :
        return
    if data.status_code == 200: 
        try :
            soup = BeautifulSoup(data.text, 'html.parser')
            dict_result = {}
            dict_result['Pukul'] = soup.find('span', {'class':'waktu'}).string.split(',')[1]
            dict_result['Tanggal'] = soup.find('span', {'class':'waktu'}).string.split(',')[0]
            count = 0
            for i in soup.find('ul', {'class':'list-unstyled'}).findChildren('li'):
                if count==1:
                    dict_result["Magnitudo"] = i.text
                elif count==2:
                    dict_result["Kedalaman"] = i.text
                elif count==3:
                    dict_result["Lintang"] = i.text.split("-")[0]
                    dict_result["Bujur"] = i.text.split("-")[1]
                elif count==4:
                    dict_result["Lokasi"] = i.text
                elif count==5:
                    dict_result["Terdampak"] = i.text
                count += 1    
            return(dict_result)
        except :
            return 
    else:
        return

def baca_hasil(result):
    try:
        print(f"Tanggal : {result['Tanggal']}")
        print(f"Pukul : {result['Pukul']}")
        print(f"Lokasi : {result['Lokasi']}")
        print(f"Magnitudo : {result['Magnitudo']}")
        print(f"Lintang : {result['Lintang']}")
        print(f"Bujur : {result['Bujur']}")
        print(f"Kedalaman : {result['Kedalaman']}")
        print(f"Terdampak : {result['Terdampak']}")
    except:
        print('Scraping gagal dilakukan.')
