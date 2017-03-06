import RPi.GPIO as GPIO
import baglanti
acik_mi="false"
def LedYak():
        global acik_mi
        GPIO.output(12, GPIO.HIGH)
        acik_mi="true"
        baglanti.veriGonder("Çıktı","Işık yakıldı")
        baglanti.veriGonder("Komut","bos")

def LedKapat():  # Led kapatmak için kullanacağız
    global acik_mi
    if acik_mi=="true":
        GPIO.output(12, GPIO.LOW)
        baglanti.veriGonder("Çıktı","Işık söndü")
        return


GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

GPIO.cleanup()
