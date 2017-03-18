import pafy
import os
import youtube_dl
import baglanti

#Hüseyin Serkan Özaydin
def guncelle():
    playlistler = ["https://www.youtube.com/watch?v=QjRYopBRUIc&list=PLXWpn_yYkUxe4bzNK3PD4S4U70yX70_zm",
                   "https://www.youtube.com/watch?v=DRONV_7UL8A&list=PLXWpn_yYkUxfBgVbaqsoP46f9o7TccBbj",
                   "https://www.youtube.com/watch?v=-8qifzv_F4Q&list=PLXWpn_yYkUxdBloYt8SEbkQljoDQpeobp"]

    for link in playlistler:

        playlist = pafy.get_playlist(str(link))
        videos = playlist['items']
        directory = "./" + playlist['title']

        if not os.path.exists(directory):
            os.makedirs(directory)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        os.chdir(directory)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        os.chdir("..")
        baglanti.veriGonder("Çıktı","Mp3 dosyaları güncelleniyor")
    baglanti.veriGonder("Komut","Boş")
    baglanti.veriGonder("Çıktı", "Mp3 dosyaları güncellendi")
