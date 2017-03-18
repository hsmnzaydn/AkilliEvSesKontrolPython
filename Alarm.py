#Hüseyin Serkan Özaydin
import datetime
import baglanti
import sesdosyasi_islemleri
import time
def AlarmVarmi(sayac):
   tarih=datetime.datetime.now()
   tarih_gun =tarih.strftime("%A")
   tarih_saat=tarih.hour
   tarih_dakika=tarih.minute



   if(baglanti.AlarmGetir(tarih_gun)=="bos"):
    print("bos")
   else:
        zaman=baglanti.AlarmGetir(tarih_gun).split(" ")



        if (int(zaman[0]) == tarih_saat and int(zaman[1])==tarih_dakika):
            while sayac==1:
                print()
                sesdosyasi_islemleri.AlarmCal()
                if baglanti.veriGetir("Komut")=="alarm kapat" or baglanti.veriGetir("Komut")=="alarm durdur":
                    break
                time.sleep(2)
                if baglanti.veriGetir("Komut")=="alarm kapat" or baglanti.veriGetir("Komut")=="alarm durdur":
                    break









