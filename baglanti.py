import pyrebase




def baglan():
  config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "storageBucket": ""

  }

  firebase = pyrebase.initialize_app(config)
  return firebase.database()



def veriGetir(child):
  db=baglan()
  return db.child(child).get().val().lower()

def veriGonder(child,degisken):
  db=baglan()
  db.child(child).set(degisken)
def sesGetir(child):
  db=baglan()
  volume=db.child(child).get().val()
  if(volume== 1):
    return 1.0
  if (volume == 9):
    return 0.9
  if (volume == 8):
    return 0.8
  if (volume == 7):
    return 0.7
  if (volume == 6):
    return 0.6
  if (volume == 5):
    return 0.5
  if (volume == 4):
    return 0.4
  if (volume == 3):
    return 0.3
  if (volume == 2):
    return 0.2
  if (volume == 1):
    return 0.2
  if (volume == 0):
    return 0.0




def AlarmGetir(gun):
  db=baglan()
  return db.child("Alarm").child(gun).get().val()
