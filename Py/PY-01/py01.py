import keyword

print(keyword.kwlist)  # Ayrılmış kelimelerin listesi

print(1970)
print(type("hello"))
print(type(3.14))
adres = "NY Times"
print(adres)

x = 5 + 2
x += 1
print(x)

pi = 3.14
yaricap = 2
cevre = 2 * pi * yaricap
print('Dairenin Cevresi : ', cevre)

print('kirmizi ' + 'kalem')  # kirmizi kalem
print('9' + '9')  # 99
print(3 * 'Python')  # PythonPythonPython

x = '3'
y = 4 * x
print(y)  # 3333
y = int(x) * 4
print(y)  # 12

s = 5
t = str(s)
print(type(t))  # Str
print(2 * t)  # 55


# İşlevler

def f():
    """Gelen Sayıya 5 ekler"""


f()
print(f)  # <function f at 0x03A942B8>


def f(x):
    print("X parametresinin aldığı deger : ", x)


f(3)


def f(x):
    """Gelen  sayıya 5 ekler"""
    x += 5
    print(x)


f(7)


def f(x):
    """5 Ekler"""
    return x+5


print(f(3))

help(f)
# help(int)

# Fonksiyon icinde kullanilan degiskenler yereldir.Dısarıda kullanılamaz


def carp(x, y):
    return x*y


print(carp(3, 4))
print(carp('emre', 2),)  # emreemre


def bolum(bolen, bolunen):
    print(bolunen/bolen)


bolum(2,16)  # 8.0
bolum(bolen=2, bolunen=16)  # 8.0

print("Python", "cok", "güzel", "gelsene")
print("Python", "cok", "güzel", "gelsene", sep='*')


def kokal(sayi, derece=2):  # derece belirtilmezse 2 al
    kok = sayi**(1/derece)
    print(kok)


kokal(16)  # derece=2
kokal(81, 4)  # derece=4 cıktı=3


# Input
print('Bir sayı giriniz : ')
# girilen = input()
# print('Girilen : ', girilen)

# gir = input('Deger gir : ')
# print('Deger : ', gir)

# Girilen deger string oldugu icin biz mesela float(gir) şeklinde türünü istediğimiz gibi değiştirmeliyiz.

y = 20


def namespace(x):
    return y+x  # Fonksiyon dısındaki y degiskenine erisbildik


print(namespace(10))


def deneme():
    global y
    print(y)
    y = 90
    print(y*3)


deneme()  # 270
print(y)  # y'yi global tanımladığımız için yeni değeri 90 oldu.


def toplama(a, b):
    return a+b


def ortalama(a, b):
    return toplama(a, b)/2


print(ortalama(10, 4))  # 7.0


# Birden fazla deger döndürme


def cember(r):
    c = 2*3.14*r
    a = 3.14*(r**2)
    return c, a


print(cember(4))  # (25.12 , 50.24) nesnesi geri döner

cevre, alan = cember(4)  # İlk dönen değer cevre , ikinci dönen ise alana atanır
print(cevre)  # 25.12
print(alan)  # 50.24


# Koşul

girdi = int(input("Bir sayı giriniz : "))
if girdi == 0:
    print("Sıfır Girdiniz")
elif girdi > 0:
    print("Pozitif")
else:
    print("Negatif")


i = 0
while i <= 5:
    print(i)
    i += 1
# else : i -= 1  şeklinde while-else yazılabilir

# Listeler

ogrenciler = []
print(type(ogrenciler))  # <class 'list'>

ogrenciler.append("Emre Berber")
ogrenciler.append("Semih Günal")
ogrenciler.append("Emre Aktürk")

print(ogrenciler[0])  # Emre Berber
ogrenciler[2] = "Hasancan Özdoğan"
print(ogrenciler[2])  # Listenin 2.elemanını Hasancan Özdoğan olarak değiştirdik
print(ogrenciler)  # ['Emre Berber', 'Semih Günal', 'Hasancan Özdoğan']

print(len(ogrenciler))  # 3

kuruyemisler = ['fındık', 'fıstık', 'badem']
kuruyemisler.append('ceviz')
print(kuruyemisler)
print(kuruyemisler[-1])  # ceviz
print(kuruyemisler[-2])  # badem
kuruyemisler[-1] = 'iğde'
print(kuruyemisler[-1])  # Listenin -1.elemanını değiştirdik

print('fındık' in kuruyemisler)  # True
print('ceviz' in kuruyemisler)  # False

for i in range(5):
    print(i)

print(kuruyemisler.pop())  # son elemanı siler ve geri döndürür
kuruyemisler.remove('fındık')  # fındık elemanını listeden çıkrarır
print(kuruyemisler.count('fıstık'))  # Listedeki 'fıstık' sayısını verir
print(kuruyemisler.index('fıstık'))  # fıstık elemanının indexi : 0 verir
kuruyemisler.reverse()  # Listeyi tersine çevirir
print(kuruyemisler)
print(sorted(kuruyemisler))  # Listeyi sıralar !Listenin tüm elemanlarının aynı türde olması şart

kuruyemisler.insert(1, 'ceviz')
print(kuruyemisler)  # 1.indexe 'ceviz' elemanını ekler

kuruyemisler.extend(ogrenciler)  # Kuruyemisler listesinin sonuna ogrenciler listesini ekler
print(kuruyemisler)

print(kuruyemisler[1:3])  # 1.indisden basla 3.indise kadar
print(kuruyemisler[:4])  # En bastan 4.indise kadar
print(kuruyemisler[3:])  # 3.indisden sona kadar


pcler = []
pcler.append(['Toshiba', 'Lenovo'])
pcler.append(['HP', 'Dell'])
print(pcler)
print(pcler[0])
print(pcler[0][1])






