def sekil_ciz(sekil_olustur,sekil_harf,karakterler,sutun):
    satir_saydirma=0
    for i in range(len(sekil_olustur)):
        sekil_gez=sekil_olustur[i]
        if i==0:
            print("  ",end="")
            for harf in range(sutun):
                print("    ",sekil_harf[harf],"   ",sep="",end="")
            print("")
        if i%2==0:
            for j in range(len(sekil_gez)):
                if j ==0:
                    print('  ',end='')
                if sekil_gez[j]==1:
                    print(" -------", end="")
                else:
                    print("        ", end="")
        else:
            for l in range(3):
                for k in range(sutun+1):
                    if l==1:
                        if k == 0:
                            print((i//2)+1," |   ",karakterler[satir_saydirma],"   ",sep='', end="")
                        elif sekil_gez[k] == 0:
                            print("   ",karakterler[satir_saydirma],"  ", end="")
                        elif sekil_gez[k] == 1:
                            print("|   ",karakterler[satir_saydirma], "   ", sep="", end="")
                        satir_saydirma += 1
                    else:
                        if k == 0:
                            print("  |       ", end="")
                        elif sekil_gez[k] == 0:
                            print("        ", end="")
                        elif sekil_gez[k] == 1:
                            print("|       ", end="")
                if l != 2:
                    print("")
        print("")
def kare_tanimlama(sekil_olustur,oyuncu_say,karakterler,sutun,oyuncu):
    kareler=[]
    for i in range(0,len(sekil_olustur)-2,2):
        a=sekil_olustur[i]
        for j in range(sutun):
            b=[sekil_olustur[i][j],sekil_olustur[i+1][j],sekil_olustur[i+1][j+1],sekil_olustur[i+2][j]]
            kareler.append(b)
        kareler.append("")
    n=0
    for u in range(len(kareler)):
        top = sum(kareler[u])
        if top==4:
            n=u
            if karakterler[n]==" ":
                karakterler[n] = oyuncu
            oyuncu_say+=2
    return karakterler, kareler, n, oyuncu_say
def hamle_yaptirma(hamle_liste,sekil_sayi,sekil_harf,hamle_satir,hamle_sutun):
    if hamle_liste[2] in ["D", "B"]: #DOĞU-BATI
        birinci_parametre_say = -1
        for x in sekil_sayi:
            birinci_parametre_say += 2
            if x == hamle_liste[0]:
                hamle_satir = birinci_parametre_say
        for y in sekil_harf:
            if y == hamle_liste[1]:
                hamle_sutun = sekil_harf.index(y)
        if hamle_liste[2] == "D":
            hamle_sutun += 1
    elif hamle_liste[2] in ["K", "G"]: #KUZEY-GÜNEY
        birinci_parametre_say = -2
        for x in sekil_sayi:
            birinci_parametre_say += 2
            if x == hamle_liste[0]:
                hamle_satir = birinci_parametre_say
        for y in sekil_harf:
            if y == hamle_liste[1]:
                hamle_sutun = sekil_harf.index(y)
        if hamle_liste[2] == "G":
            hamle_satir += 2
    return hamle_satir, hamle_sutun
def oyun():
    devam = "e"
    while devam in ["e", "E"]:
        sekil_sayi = ["1", "2", "3", "4", "5", "6", "7"]
        sekil_harf = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T"]
        yonler = ["K", "G", "D", "B"]
        sekil_olustur = []
        oyuncu_1 = input("1. oyuncuyu temsil etmek için bir karakter giriniz:")
        while len(oyuncu_1) != 1 or oyuncu_1==" ":
            oyuncu_1 = input("Lütfen bir tane ve boşluk olmayan karakter giriniz:")
        oyuncu_2 = input("2. oyuncuyu temsil etmek için bir karakter giriniz:")
        while len(oyuncu_2) != 1 or oyuncu_2==oyuncu_1 or oyuncu_2==" ":
            oyuncu_2 = input("Lütfen bir tane ve farklı karakter giriniz:")
        while True:
            try:
                satir = int(input("Oyun alanının satır sayısını giriniz (3-7):"))
                while satir < 3 or satir > 7:
                    satir = int(input("Lütfen aralığa uygun satır sayısı giriniz (3-7):"))
                break
            except ValueError:
                print("Lütfen girdiye uygun sayısal bir değer giriniz!")
        while True:
            try:
                sutun = int(input("Oyun alanının sütun sayısını giriniz (3-19):"))
                while sutun < 3 or sutun > 19:
                    sutun = int(input("Lütfen aralığa uygun sütun sayısı giriniz (3-19):"))
                break
            except:
                print("Lütfen girdiye uygun sayısal bir değer giriniz!")
        for sutunlar in range(satir * 2 + 1):
            sekil_olustur.append([0] * sutun)
        for satirlar in range(1, satir * 2 + 1, 2):
            sekil_olustur[satirlar].append(0)
            for satirlari_ciz in range(0, sutun + 1, sutun):
                sekil_olustur[satirlar][satirlari_ciz] = 1
        for sutunlari_ciz in range(0, (satir * 2 + 1) + 1, satir * 2):
            sekil_olustur[sutunlari_ciz] = [1] * sutun
        karakterler = [" "] * (satir * (sutun + 1))
        onceki_karakterler=0
        oyuncu = 0
        oyuncu_say = 1
        karakterler, kareler, n, oyuncu_say = kare_tanimlama(sekil_olustur, oyuncu_say, karakterler, sutun, oyuncu)
        sekil_ciz(sekil_olustur, sekil_harf, karakterler, sutun)
        while True:
            if (oyuncu_say - (len(karakterler) - karakterler.count(" "))) % 2 == 1:
                oyuncu = oyuncu_1
            else:
                oyuncu = oyuncu_2
            print("Oyuncu ", oyuncu, " lütfen hamlenizi giriniz (örn:1AD):", sep="", end="")
            hamle = input()
            hamle_liste = list(hamle)
            while len(hamle_liste)!=3:
                hamle = input("Lütfen üç karekterden oluşan bir hamle giriniz (örn:1AD):")
                hamle_liste = list(hamle)
            a = sekil_sayi[:satir]
            b = sekil_harf[:sutun]
            while (hamle_liste[0] not in a) or (hamle_liste[1] not in b) or (hamle_liste[2] not in yonler):
                hamle = input("Oyun alanı içinde değil! Hamlenizi tekrar giriniz:")
                hamle_liste = list(hamle)
            hamle_satir = hamle_sutun = 0
            hamle_yaptirma(hamle_liste, sekil_sayi, sekil_harf, hamle_satir, hamle_sutun)
            hamle_satir, hamle_sutun = hamle_yaptirma(hamle_liste, sekil_sayi, sekil_harf, hamle_satir, hamle_sutun)
            if hamle_liste[2] in ["B"] and sekil_olustur[hamle_satir][hamle_sutun] == 1:
                print("Girdiğiniz kenar daha önce çizilmiş!")
                continue
            if hamle_liste[2] in ["D"] and sekil_olustur[hamle_satir][hamle_sutun] == 1:
                print("Girdiğiniz kenar daha önce çizilmiş!")
                continue
            if hamle_liste[2] in ["K"] and sekil_olustur[hamle_satir][hamle_sutun] == 1:
                print("Girdiğiniz kenar daha önce çizilmiş!")
                continue
            if hamle_liste[2] in ["G"] and hamle_satir == satir * 2:
                print("Girdiğiniz kenar daha önce çizilmiş!")
                continue
            elif hamle_liste[2] in ["G"] and sekil_olustur[hamle_satir][hamle_sutun] == 1:
                print("Girdiğiniz kenar daha önce çizilmiş!")
                continue
            sekil_olustur[hamle_satir][hamle_sutun] = 1
            kare_tanimlama(sekil_olustur, oyuncu_say, karakterler, sutun, oyuncu)
            karakterler, kareler, n, oyuncu_say = kare_tanimlama(sekil_olustur, oyuncu_say, karakterler, sutun, oyuncu)
            sekil_ciz(sekil_olustur, sekil_harf, karakterler, sutun)
            oyuncu_say += 1
            if onceki_karakterler-karakterler.count(" ")==2:
                oyuncu_say+=1
            onceki_karakterler = karakterler.count(" ")
            if (len(karakterler) - karakterler.count(" ")) == satir * sutun:
                print("Oyuncu ", oyuncu_1, "'e ait karelerin sayısı:", karakterler.count(oyuncu_1), sep="")
                print("Oyuncu ", oyuncu_2, "'e ait karelerin sayısı:", karakterler.count(oyuncu_2), sep="")
                if karakterler.count(oyuncu_1) > karakterler.count(oyuncu_2):
                    print("Oyunu, oyuncu", oyuncu_1, "kazandı!")
                elif karakterler.count(oyuncu_2) > karakterler.count(oyuncu_1):
                    print("Oyunu, oyuncu", oyuncu_2, "kazandı!")
                else:
                    print("Oyun berabere.")
                break
        devam=input("Tekrar oynamak ister misiniz (E/H)? ")
        if devam in ["e","E"]:
            print()
            oyun()
        return sekil_olustur, sekil_harf, karakterler, hamle_liste, oyuncu_say, satir, sutun, sekil_sayi, \
               sekil_harf, hamle_satir, hamle_sutun, oyuncu
oyun()
