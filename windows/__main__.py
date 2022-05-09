from pyrogram.errors import (
    SessionPasswordNeeded, FloodWait,
    PhoneNumberInvalid, ApiIdInvalid,
)
from pyrogram import Client as PyrogramClient
from time import sleep
from windows import *
from . import console
import sys
userbot=None
mainuserbot=None

dosya=""
api_id=""
api_hash=""

calinacakgrup=""

Clients= []
def hesaplariolustur ():
    dizin = soru("Hesapların olduğu dosyanın dizini:")
    with open(dizin,"r") as file:
        dosya = file.read()
        dosya = dosya.split("\n")
    for i in file:
        ii = i.split("|")
        
        stringsession=""
        try:
            api_id = ii[0]
            api_hash= ii[1]
            stringsession = ii[2]
        except IndexError:
            hata("Hesapların olduğu dosya biçimi hatalı ! Lütfen hesapları tek satırda bir hesap olmak üzere şu formatta kaydedin:\nFormat: api_id|api_hash|string\nÖrnek:1636343|6sasn776askdghd3728|1JKgxqaıuq74294762hjcgajdgddeqhdqkhqdkdkkw=")
        try:
            mainmi= bool(ii[3])
        except IndexError:
            mainmi = None
        except Exception:
            mainmi = None
        
        if mainmi == True & mainuserbot==None:
            try:
                mainuserbot = PyrogramClient(
                stringsession,
                api_id,
                api_hash,
                device_model='Mac',
                system_version=' | Powered by @cerceyn',
                app_version=str('| 1.0'),
                in_memory=False)
                bilgi(api_hash + " için main client oluşturuldu !")
            except FloodWait as e:
                hata(api_hash + f" için main client oluşturulamadı ! 🛑 Floodwait: {e.x}")
            except ApiIdInvalid:
                hata(api_hash + f" için main client oluşturulamadı ! 🛑 Api Id veya Hash Hatalı!")


        try:
            userbot = PyrogramClient(
            stringsession,
            api_id,
            api_hash,
            device_model='Mac',
            system_version=' | Powered by @cerceyn',
            app_version=str('| 1.0'),
            in_memory=False)
            Clients.append(userbot)
            bilgi(api_hash + " için client oluşturuldu !")
        except FloodWait as e:
            noadded(api_hash + f" için client oluşturulamadı ! 🛑 Floodwait: {e.x}")
        except ApiIdInvalid:
            noadded(api_hash + f" için client oluşturulamadı ! 🛑 Api Id veya Hash Hatalı!")

hesapno=0
def hesaplarabaglan():
    global hesapno    
    for userbotstart in Clients:
        api_hash = dosya[hesapno].split("|")[1]
        try:
            userbotstart.connect()
            bilgi(api_hash + "oturuma giriş yapıldı !")
        except ConnectionError:
            userbotstart.disconnect()
            userbotstart.connect()
            bilgi(api_hash + "oturuma giriş yapıldı !")
        except Exception as e:
            noadded(api_hash + f"oturuma giriş yapılamadı ! 🛑 {str(e)}")
    
    hesapno+=1
    #    return userbot

def islemler(userbot):
#    if not calinacakgrup.startswith("@") and not calinacakgrup.startswith("http") and not calinacakgrup.startswith("t.me"):
#        calinacakgrup = "@" + calinacakgrup
    
    hedefgrup = soru("Çalınan Üyeleri Hangi Gruba Çekeyim: (Grubun kullanıcı adı) ")
#    if not hedefgrup.startswith("@") and not hedefgrup.startswith("http") and not hedefgrup.startswith("t.me"):
#        hedefgrup = "@" + hedefgrup
    count2=None
    try:
        count2 = mainuserbot.get_chat_members_count(hedefgrup)
        bilgi(f"Çalacağım grubun ({calinacakgrup}) üye sayısı {count} kişi ! ")
    except Exception as e:
        hata(e)
    sleep(5)
    for i in range(25):
        console.print("\n")
    logo()
    calinamayan=0
    calinan=0
    try:
        bilgi("Hesap koruması nedeniyle her 8 saniyede bir üye çekme isteğinde bulunacak..")
        for member in mainuserbot.iter_chat_members(calinacakgrup):
            try:
                if member.user.is_bot:
                    passed("{} bot olduğu için geçiliyor!".format(member.user.username))
                    continue
                mainuserbot.add_chat_members(hedefgrup, member.user.id)
                basarili("{} gruba başarıyla eklendi!".format(member.user.first_name))
                calinan= calinan + 1
            except Exception as e:
                noadded("{} gruba eklenemedi! Hata:{}".format(member.user.first_name,str(e)))
                calinamayan = calinamayan + 1
            sleep(8)
        console.clear()
        logo()
        basarili(f"İşlem Tamamlandı ! {hedefgrup} ögesine {calinacakgrup} ögesinden toplam {calinan} üye eklendi! ")
        userbot.stop()
        hata("Güle Güle !")
    except Exception as e:
        hata(e)

if __name__ == "__main__":
    for i in range(25):
        console.print("\n")
    logo()

    hesaplariolustur()
    global calinacakgrup
    hesaplarabaglan()
    onemli("Üye çalacağım grupta bulunmam ve çaldığım üyeleri eklediğim grupta yönetici olmam gerekir..")
    calinacakgrup = soru("Üye Çalınacak Grubun kullanıcı adı: (Hangi gruptan üyeleri çekeyim) ")
    try:
        count = mainuserbot.get_chat_members_count(calinacakgrup)
        bilgi(f"{calinacakgrup} ögesinde {count} kişi bulundu! ")
    except Exception as e:
        hata(e)
    a = True
    while a:
        try:
            islemler(userbot)
        except Exception as e:
            onemli(e)
        finally:
            cevap= soru("Kod tekrar yürütülsün mü? (y/n)")
            if cevap == "n":
                a = False
                userbot.stop()
                hata("Güle Güle !")
            else:
                continue
        

    






