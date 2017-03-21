from gtts import gTTS
import sesdosyasi_islemleri
import baglanti
#Hüseyin Serkan Özaydin

def konus(soylenecek_soz):
    tts = gTTS(text=soylenecek_soz, lang='tr')
    tts.save("sistem.mp3")
    sesdosyasi_islemleri.konusma()
    baglanti.veriGonder("Komut","bos")
    baglanti.veriGonder("Çıktı",soylenecek_soz)


