# BOLUM 6

ad = 'Emre'
print(ad[2])
print(len('Emre Berber'))
print("Hasan \"bugün okul yok\" dedi")

cevap = 'Dün akşam oynanan maçta  \
 3 gol atıldı.'

print(cevap)

cumle1 = "Bugün okula \ngitmedim"
print(cumle1)
cumle2 = "Haftasonu arkadaşlarla tenis \toynayacağız"
print(cumle2)


dersSaati = '8:15'
print("Dersim sabah saat",dersSaati,'de baslıyor')
print("Dersim sabah saat %s'de baslıyor" %dersSaati)

print("Her sabah %d'de kalkarım" %7)
print("Otobüs kalkış saati %s , varış ise %s'dir.Mola kalkıştan %s saat sonradır" %('12:00' , '21:00' , '4'))

print("Dersim sabah {0}'da başlıyor {1}'da bitiyor.".format('8:00','10:00'))

print("emre berber".upper())  # EMRE BERBER
print("EMRE BERBER".lower())  # emre berber
print('ön' in 'Okulun önünde bekliyorum')  # True
print("Okulun önünde bekliyorum".find('ön'))  # 7 : indexi geri döndürdü
print("Okulun önünde bekliyorum".find('arka'))  # -1 : bulamadığı için geriye -1 değerini döndürür
print('inebolu'.endswith('bolu'))  # True
print('Çanakkale'.startswith('Çan'))  # True

print("Melike beim tatlı kızımdır".split())  # ['Melike', 'beim', 'tatlı', 'kızımdır']
email = "brbr.emre@gmail.com"
[kullanici,alan]=email.split('@')
print("Kullanıcı Adı : {0} \nSifre : {1}".format(kullanici,alan))
print('@'.join(['brbr.emre','gmail.com']))  # brbr.emre@gmail.com
print('Beyaz atlı prens'.replace(' ','_'))  # Beyaz_atlı_prens

print('    Cümlenin önünde boşluk, sonunda satır sonu \n'.strip())  # Cümlenin önünde boşluk, sonunda satır sonu

s = '1967'
print(s.isnumeric())  # True
s = 'Emre61'
print(s.isnumeric())  # False
pi = '3.14'
print(s.isnumeric())  # False : noktayı karakter olarak algılıyor

# Dosya İşlemleri
    # belgeler.yazbel.com/python-istihza/temel_dosya_islemleri.html

tahsilat_dosyasi = open("tahsilat_dosyası.txt", "w")  # Dosyamızı w(yazma) kipinde oluşturduk
# open("C:\aylar\nisan\toplam masraf\masraf.txt", "w") şeklinde yazarsan kaçış dizeleri hataya sebep olur
# open(r"C:\aylar\nisan\toplam masraf\masraf.txt", "w") ya bu şekilde yazarsın
# open("C:\\aylar\\nisan\\toplam masraf\\masraf.txt", "w") ya da bu şekilde

tahsilat_dosyasi.write("Berberler Ltd Şti 14.500 TL \n")
tahsilat_dosyasi.write("Kozan Grup 18.950 TL \n")
tahsilat_dosyasi.write("Yıldız Ticaret 9.950 TL")
tahsilat_dosyasi.close()
# w ile açtığımız dosyayı sonradan tekrar w ile açarsak içindeki her şeyi siler ve boş dosya açar !

thd = open("tahsilat_dosyası.txt","r")  # Okuma kipinde açtık.Okumada r'yi yazmasak da olur.
print(thd.read())  # Dosyanın tamamını yazdırır
print(thd.readline())  # İlk satırı yazdırır.Fakat yazdırmadı :)
print(thd.readlines())

with open("tahsilat_dosyası.txt", "r") as dosya:
    print(dosya.read())  # with ile dosya.close yazmamıza gerek kalmıyor

thd.seek(0)  # Tekrar baştan okumaya sarmak için
print(thd.read())

f = open("tahsilat_dosyası.txt", "a")  # a kipi ile dosyanın içindekileri silmeden güncelleme yapabiliyoruz
with open("tahsilat_dosyası.txt", "a") as f:  # Bu yöntem ile sonuna ekleme yapabiliyoruz
    f.write("\nSelin Özden\t: 0212 222 22 22")

f = open("tahsilat_dosyası.txt", "r+")  # Hem okuma hem de yazma kipinde açtık
f.seek(0)  # En başa sardık
f.write("Emre Berber \t: 230 580 70 70 \n")  # Dosyanın en başına ekleme yapabilmiş olduk
veri=f.readlines()
veri.insert(2,"Hasan X : 0555 55 55 00 \n")
f.seek(0)
f.writelines(veri)  # Dosyanın 2.indexine veri ekledik


# Tüpler
# Diziler gibidir sadece sonradan üzerinde değişiklik yapılamaz

degerler = ('12:50', 7, 4)
print(degerler[1])
# degerler[2]=5  : Hata verir.

(kalkis, varis , mola) = ('12:50', '22:05', 6)
print(varis)
mola=3  # Böyle tanımlamada yeni değer atayabiliriz
print(mola)

sifir, bir, iki = '0',1,2
print(bir)

eposta = 'brbr.emre@gmail.com'
(kullaniciAdi, alanAdi) = eposta.split('@')
print(kullaniciAdi + ' ve ' + alanAdi)

def toplam(*sayilar):  # Böylece fonksiyona parametre sınırlaması getirmemiş olduk
    top=0
    for i in sayilar:
        top += i
    return top

print(toplam(1,3,5,7))  # 16

# Fonksiyonun birden fazla deger döndürmesi :
def enBuyukenKucuk(*sayilar):
    return max(sayilar), min(sayilar)

print(enBuyukenKucuk(1,8,5,6))  # (8, 1)


# Sözlükler
sozluk = [
    ('adhere', 'yapışmak'),
    ('bald', 'dazlak, kel')
]


def bul(kelime):
    for k in sozluk:
        if k[0] == kelime:
            return k[1]

print(bul('adhere'))  # yapışmak
# Ancak bunu listelerle yapmak zahmetli ve kullanımı zormuş

newsozluk = {
    'adhere' : 'yapışmak',
    'bald' : 'dazlak , kel'
}

print(newsozluk['bald'])  # dazlak, , kel
print(newsozluk)  # {'adhere': 'yapışmak', 'bald': 'dazlak , kel'}

# Sözlüğe daha sonradan ikili deger ekleyebiliriz :
newsozluk['page'] = 'sayfa'
print(newsozluk)  # {'adhere': 'yapışmak', 'bald': 'dazlak , kel', 'page': 'sayfa'}

for i in newsozluk:
    print(i)

print('page' in newsozluk)  # True
print('computer' in newsozluk)  # False

# İstatistikler
cumle = "Hatasiz kul olmaz"
s = {}

for i in cumle:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1

print('Cumledeki harflerin sayısı : ')
# Sözlüğü sıralanmıs bastıralım :
for i in sorted(s):
    print(i,'-->', s[i])


l = newsozluk.keys()  # Sözlüklerin anahtarlarını bir liste olarak keys() ile alabiliriz
for i in l:
    print(i)

print(sorted(newsozluk.keys()))  # ['adhere', 'bald', 'page']
for a in sorted(newsozluk.keys()):
    print(a, ' : ', newsozluk[a])

print(newsozluk.values())  # Sözlükteki anahtarlara ait degerleri dinamik liste ile verir
print(newsozluk.items())  # Sözlüğün elemanlarını liste olarak döndürür.Listenin elemanları (anahtar, deger) şeklinde tüpdür.
for i in newsozluk.items():
    print(i[0], ' : ', i[1])

print(newsozluk.get('page'))  # sayfa
print(newsozluk.get('title', 'Sözlükte bulunamadı'))  # Sözlükte bulunamadı
newsozluk.pop('bald')  # Sözlük elemanı siler ve sildiği degeri de döndürür

myName = 'Emre Berber'
del myName
# print(myName)  : Hata verir.Çünkü del ile nesneyi bellekten sildik

copyDic = newsozluk.copy()  # Sözlüğün kopyasını aldık

musteri = {'ad': 'Emre', 'soyad': 'Berber', 'tel':'0505061'}
guncel_bilgi = {'tel':'999999', 'adres':'Trabzon'}

musteri.update(guncel_bilgi)
print(musteri)  # {'ad': 'Emre', 'soyad': 'Berber', 'tel': '999999', 'adres': 'Trabzon'}