import baglanti
import sesdosyasi_islemleri
import konusma
import Alarm
import time
import os
import havadurumu
#import Led_kontrolleri
import mp3_dosyalarini_guncelle

#Hüseyin Serkan Özaydin
alarm_sayac="null"
ses_seviyesi=baglanti.sesGetir("Ses")
while True:
    try:
        istek=baglanti.veriGetir("Komut")




        if istek=="mp3 çal":
            konusma.konus("Hangi müzik türünü çalmak istersiniz")
        if istek=="rock":
            sesdosyasi_islemleri.sesKontrol(ses_seviyesi)
            sesdosyasi_islemleri.baslat("rock")
        if istek=="pop":
            sesdosyasi_islemleri.sesKontrol(ses_seviyesi)
            sesdosyasi_islemleri.baslat("pop")
        if istek=="damar":
            sesdosyasi_islemleri.sesKontrol(ses_seviyesi)
            sesdosyasi_islemleri.baslat("damar")
        if istek=="mp3 durdur":
            sesdosyasi_islemleri.durdur()
        if istek=="mp3 beklet":
            sesdosyasi_islemleri.pause()
        if istek=="mp3 devam et":
            sesdosyasi_islemleri.unpause()
        if istek=="mp3 ileri":
            sesdosyasi_islemleri.next_muzik()
        if istek=="mp3 geri":
            sesdosyasi_islemleri.previous_muzik()
        if istek=="alarm aç":
            alarm_sayac=1
        if istek=="alarm kapat":
            alarm_sayac=0
            sesdosyasi_islemleri.alarmKapat()
        if istek=="alarm durdur":#Alarmı durdur
            sesdosyasi_islemleri.alarmKapat()
            havadurumu.havadurumu()
            time.sleep(50)
        if istek=="mp3 güncelle":
            mp3_dosyalarini_guncelle.guncelle()
        if istek=="ses degistir":
            sesdosyasi_islemleri.sesKontrol(baglanti.sesGetir("Ses"))
        if istek=="evden çıkıyorum":
            sesdosyasi_islemleri.pause()
            konusma.konus("Hoşçakalın")
        if istek=="eve geldim":
            sesdosyasi_islemleri.unpause()
            konusma.konus("Hoşgeldiniz")

       # if istek=="ışık yak":
        #    Led_kontrolleri.LedYak()
        #if istek=="ışık söndür":
         #   Led_kontrolleri.LedKapat()

        Alarm.AlarmVarmi(alarm_sayac)











        sesdosyasi_islemleri.devamediyormu()
    except:
        os.system("$> ps -ef | grep python")
        os.system("python main.py")

     #   print("Sistem kapandı tekrar acılıyor")
