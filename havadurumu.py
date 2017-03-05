from bs4 import BeautifulSoup
import requests
from gtts import gTTS
import sesdosyasi_islemleri
import time


def havadurumu():
    source = requests.get('http://www.mynet.com/havadurumu/asya/turkiye/istanbul')
    soup = BeautifulSoup(source.text, 'html.parser')
    sicaklik = soup.findAll('span', attrs={'class': 'hvDay'})
    sicaklik2 = soup.findAll('span', attrs={'class': 'hvMood'})
    sicaklik3=soup.findAll('span', attrs={'class': 'hvDeg1'})
    sayac=0


    for gun in sicaklik:
        print(gun.text)
        break
    for durum in sicaklik2:
        print(durum.text)
        break
    for sicaklik_durumu in sicaklik3:
        print(sicaklik_durumu.text)
        break
    if durum.text=="Karla Karışık Yağmur" or durum.text=="Kar":
        tavsiye="Lütfen kalın giyinin"
        sayac=1
    if durum.text=="Yağışlı" or durum.text=="Hafif Yağmur":
        tavsiye="Lütfen yanınıza şemsiye alın"
        sayac=1
    if sayac==1:
        tts = gTTS(text="İyi günler Serkan Bey.Bugün günlerden" + gun.text + "Dışarıda" + durum.text+"var"+"Hava sıcaklığı"+sicaklik_durumu.text+tavsiye,lang='tr')
    else:
        tts = gTTS(text="İyi günler Serkan Bey.Bugün günlerden" + gun.text + " hava" + durum.text+"ve"+" Hava sıcaklığı"+sicaklik_durumu.text,lang='tr')
    tts.save("sistem.mp3")
    sesdosyasi_islemleri.konusma()
    time.sleep(10)


