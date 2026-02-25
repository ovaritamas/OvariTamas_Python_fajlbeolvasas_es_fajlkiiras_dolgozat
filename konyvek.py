"""
Olvasd be a konyvek.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány könyv szerepel a fájlban?
2. Melyik könyvnek van a legtöbb oldala?
3. Melyik könyvnek van a legkevesebb oldala?
4. Melyik szerző írt a legtöbb könyvet?
5. Átlagosan hány oldalasak a könyvek?

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik kiadó adott ki a legtöbb könyvet?

A megoldott feladatokat a kiirt_adatok nevű mappában hozd létre statisztika.txt néven!
"""


print("1. A beolvasott fájlban összesen ____ könyv szerepel.")
print("2. A legtöbb oldalas könyv: ____")
print("3. A legkevesebb oldalas könyv: ____")
print("4. A legtöbb könyvet író szerző: ____")
print("5. Az átlagos oldalszám: ____")
print("***A legtöbb könyvet kiadó kiadó: ____"),


import os

mappa = "kiirt_adatok"
kimeneti_fajl = os.path.join(mappa, "statisztika.txt")

konyvek = []

with open('beolvasando_adatok/konyvek.txt',"r", encoding="utf-8") as f:
    sorok = f.readlines()

    for sor in sorok[1:]: 
        adat = [item.strip() for item in sor.strip().split(";")]
        
        if len(adat) >= 4:
            konyvek.append({
                "szerzo": adat[0],
                "cim": adat[1],
                "oldal": int(adat[2]),
                "kiado": adat[3]
            })

osszes_konyv = len(konyvek)
legnagyobb = max(konyvek, key=lambda x: x["oldal"])
legkisebb = min(konyvek, key=lambda x: x["oldal"])
atlag_oldal = sum(k["oldal"] for k in konyvek) / osszes_konyv

szerzok = {}
kiadok = {}
for k in konyvek:
    szerzok[k["szerzo"]] = szerzok.get(k["szerzo"], 0) + 1
    kiadok[k["kiado"]] = kiadok.get(k["kiado"], 0) + 1

legaktivabb_szerzo = max(szerzok, key=szerzok.get)
legaktivabb_kiado = max(kiadok, key=kiadok.get)
