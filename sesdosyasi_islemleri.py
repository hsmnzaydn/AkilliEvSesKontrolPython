import pygame
import os
import baglanti
#Hüseyin Serkan Özaydin

muziklist="null"



globvar=1
mp3_durum="null"
mp3_turu="null"
alarm_durumu="null"
next_muzik_deger=0



def baslat(tur):
    pygame.init()
    global mp3_durum,mp3_turu,muziklist
    if tur=="pop" or tur=="rock" or tur=="damar":
        if tur=="pop":
            muziklist=os.listdir("./pop")
            mp3_turu = "pop/"
            pygame.mixer.music.load("pop/"+str(muziklist[0]))
        if tur=="rock":
            muziklist=os.listdir("./rock")
            mp3_turu = "rock/"
            pygame.mixer.music.load("rock/"+str(muziklist[0]))
        if tur=="damar":
            muziklist = os.listdir("./damar")
            mp3_turu = "damar/"
            pygame.mixer.music.load("damar/"+str(muziklist[0]))
    else:
        pygame.mixer.music.load(tur)
    mp3_durum="MP3 başladı"
    pygame.mixer.music.play()
    baglanti.veriGonder("Komut", "bos")
    baglanti.veriGonder("Çıktı",muziklist[0]+" çalınıyor")


def durdur():
    global mp3_durum
    if mp3_durum=="MP3 başladı":
        pygame.mixer.music.stop()
        baglanti.veriGonder("Çıktı","Mp3 durduruldu")
        baglanti.veriGonder("Komut", "bos")
        mp3_durum="Durdu"

def pause():
    global mp3_durum
    if mp3_durum == "MP3 başladı":
        baglanti.veriGonder("Çıktı","Mp3 bekletiliyor")
        baglanti.veriGonder("Komut", "bos")
        pygame.mixer.music.pause()
        mp3_durum="Pause edildi"
def sesKontrol(ses_degeri):
    global mp3_durum
    if mp3_durum=="MP3 başladı":
        pygame.mixer.music.set_volume(ses_degeri)
        baglanti.veriGonder("Komut","bos")

def unpause():
    global mp3_durum
    if mp3_durum == "Pause edildi":
        baglanti.veriGonder("Çıktı", "Mp3 devam ettiriliyor")
        baglanti.veriGonder("Komut", "bos")
        pygame.mixer.music.unpause()
        mp3_durum="MP3 başladı"
def next_muzik():
    global globvar,mp3_durum,next_muzik_deger
    if mp3_durum=="MP3 başladı":
        baslat(mp3_turu+str(muziklist[globvar]))
        baglanti.veriGonder("Komut","bos")
        baglanti.veriGonder("Çıktı", muziklist[globvar] + " çalınıyor")
        globvar += 1
        next_muzik_deger=globvar
        print(globvar)
        baglanti.veriGonder("Komut", "bos")
        if (globvar == len(muziklist)):
            globvar = 0
def previous_muzik():
    global globvar, mp3_durum,next_muzik_deger
    if mp3_durum == "MP3 başladı":
        globvar = next_muzik_deger-1
        baslat(mp3_turu + str(muziklist[globvar-1]))
        baglanti.veriGonder("Komut", "bos")
        baglanti.veriGonder("Çıktı", muziklist[globvar-1] + " çalınıyor")

        print(globvar)
        baglanti.veriGonder("Komut", "bos")


def devamediyormu():
    global globvar,mp3_durum,mp3_turu,muziklist
    if  mp3_durum=="MP3 başladı" and pygame.mixer.music.get_busy() == False and globvar < len(muziklist):
        baslat(mp3_turu+str(muziklist[globvar]))
        mp3_durum="MP3 başladı"
        baglanti.veriGonder("Çıktı", muziklist[globvar] + " çalınıyor")
        globvar += 1
        if(globvar==len(muziklist)):
            globvar=0
def konusma():
    global mp3_durum
    pygame.init()
    mp3_durum="Konuşma başladı"
    pygame.mixer.music.load("sistem.mp3")
    pygame.mixer.music.play()
def AlarmCal():
    global alarm_durumu
    pygame.init()
    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play()
    alarm_durumu="Alarm başladı"

def alarmKapat():
    global alarm_durumu
    if alarm_durumu=="Alarm başladı":
        pygame.mixer.music.stop()
        baglanti.veriGonder("Çıktı", "Alarm Kapatıldı")
        baglanti.veriGonder("Komut", "bos")




