import sqlite3

db = sqlite3.connect('veresiye.db')

yetki = db.cursor()

yetki.execute("CREATE TABLE IF NOT EXISTS kisiler(isim,borç)")

while True:

    print("***VERESİYE DEFTERİNE HOŞGELDİNİZ***")

    sor = input("1-BORÇLU EKLE\n2-BORÇLULARI GÖR\n")

    if sor == "1":

        borçlu_isim = input("LÜTFEN BORÇLUNUN İSMİNİ GİRİNİZ: ")
        borçlu_miktarı = input("LÜTFEN BORÇ MİKTARINI GİRİNİZ: ")
        yetki.execute(f"INSERT INTO kisiler VALUES('{borçlu_isim}','{borçlu_miktarı}')")
        db.commit()
        print(f"işlem tamamlandı,borçlu kişinin adı:{borçlu_isim}")
        input("DEVAM EDİLSİN Mİ ?")


    elif sor == "2":

        yetki.execute("SELECT * FROM kisiler")
        yazdır = yetki.fetchall()
        say = 1
        for i in yazdır:
            print("********************BORÇLU BİLGİSİ********************")
            print(f"{say}:BORÇLU KİŞİNİN ADI:{i[0]}\nBORÇ MİKTARI: {i[1]}\n")
            say += 1
        input("DEVAM EDİLSİN Mİ ?")


