
// Javascript 101

var name1 = "Emre " + "Berber <br>";
document.write(name1);

var name2="Emre ";
name2 += "Merhaba <br>";
document.write(name2);

kisiler=new Array("Emre","Hasan","Yakup","Fatih","Umut");
delete kisiler[3];
document.write(kisiler[3]);  // undefined
document.write(kisiler[4]);  // Umut

document.write("<br>");

var x = 0 in kisiler;
document.write(x);  // true
var y =  "Emre" in kisiler;
document.write(y);  // true vermesi lazım ama false yazıyor :/


kisi = {isim : "Semih" , soyisim:"Yılmaz" , yas:25};
var z="isim" in kisi;
document.write(z);  // true

if(kisiler instanceof Array)
    document.write("<br> OK.");


// HTML:input[yas]
function fonk(nesne)
{
    if(nesne.value<18)
        alert("Resit Degil");
    if(nesne.value>=18)
        alert("Resit");
}


// Typeof Operatörü

var a="Emre";
document.write(typeof(a));  // string
var b=10;
document.write(typeof(b));  // number

uyeler=Array("a","b");
document.write(typeof(uyeler));  // object

for(bilgi in kisi)
{
    document.write(kisi[bilgi]+"<br>");  // Semih Yılmaz
}


// Hata Yönetimi

var c=10;
try
{
    k/c;
}
catch(err)
{
    document.write("Hata : "+err.message);
}

// Array
var meyveler=new Array();  // Boş bir dizi tanımladık
meyveler[0]="Elma";

// 2.Yöntem
var meyveler2=new Array("Elma","Karpuz","Şeftali");

// 3.Yöntem
var meyveler3=[];
meyveler=["Elma","Karpuz","Şeftali"];

var dizi= new Array(3);  // Dizi boyutunu belirleme

document.write("<br>"+meyveler2.length);  // Dizinin Boyutu : 3

var dizi1=Array("A","B","C");
var dizi2=Array("D","E","F");
document.write("<br>"+dizi1.concat(dizi2));  // Dizileri birleştirir

document.write("<br>"+dizi1.join('-'));  // A-B-C

document.write("<br>"+dizi1.shift());  // Dizinin ilk elemanını verir ve o elemanı siler
document.write("<br>"+dizi1);  // B,C

document.write("<br>"+dizi2.pop());  // Son elemanı döndürür ve dizi içinden siler
document.write("<br>"+dizi2);  // D,E

dizi1.push("X","Y","Z");  // Dizinin sonuna ekler
document.write("<br>"+dizi1);

dizi2.unshift("W","Q");  // Dizinin başına bir veya birden fazla eleman ekleme
document.write("<br>"+dizi2);

dizi1.reverse();  // Dizi elemanlarını tersine çevirir
document.write("<br>"+dizi1);

var dizi3=Array("Elma","Ordu",141,"Trabzon","Sivas");
document.write("<br>"+dizi3.sort());  // Dizi elemanlarını alfabetik sıralar

var dizi4=Array("A","B","C","D","E");
document.write("<br>"+dizi4.slice(1,3));  // B,C :1.indexden basla 3.indexe kadar
document.write("<br>"+dizi4.slice(2));  // C,D,E :2.indexden basla dizinin sonuna kadar 
document.write("<br>"+dizi4.slice(1,-2));  // B,C :1. indexden basla son 2 elemanı alma

var silinenler=dizi4.splice(1,3,"X","Y","Z");  // 1.indexden basla 3 elemanı al X,Y,Z ile değiştirdi ve silinenlere atadı
document.write("<br> Yeni Dizi : "+dizi4);  // A,X,Y,Z,E
document.write("<br> Silinenler : "+silinenler);  // B,C,D


function kontrol_et(dizi)
{
    if(isNaN(dizi))
        return  true;
    else 
        return false;
}
var dizi5 = Array("A","B","C","D","E");
if(dizi5.every(kontrol_et))  // every ile dizinin tüm elemanlarının belirli niteliğe sahip olup olmadıklarını kontrol ediyoruz
    document.write("<br> Dizi Harflelrden olusmus");
else
    document.write("Dizi rakamlardan olusmus");

document.write(dizi5.indexOf("B"));  // Değerin indexini verir.

// Functions

var k_alan = function(kenar) {
    return kenar*kenar;
}

document.write("<br>Kenar 3 Alan : ",k_alan(3));

document.write("<br>"+escape("Dur ! Yolcu !"));  // Dur%20%21%20Yolcu%20%21
document.write("<br>"+unescape("Dur%20%21%20Yolcu%20%21"));  // Dur ! Yolcu !

document.write("<br>"+parseFloat("61Trabzon"));  // 61 : String veriyi floata çevirir.Başka parse fonkları da mevcut

// Nesne oluşturma ve Özellik Ekleme
function ogrenci(x,y,z) {
    this.isim=x;
    this.yas=y;
    this.sehir=z;
}

var ogr_1 = new ogrenci("Emre Berber", 20 , "Trabzon");
document.write("<br> ogr_1 : "+ogr_1.isim);  // Emre Berber
ogr_1.isim="Yunus Emre Berber";
document.write("<br> new name is "+ogr_1.isim);  // Nesnenin özelliğini değiştirebildik
ogr_1.kilo=71;  // Nesnemize daha sonradan yeni özellik ekleyip değerini atadık
document.write("<br> ogr_1 kilo : "+ogr_1.kilo); // 71

function ortalama(vize, final) {
    this.vize=vize;
    this.final=final;
    this.ortalama = function() {
        return (this.vize+this.final)/2;
    }
}

var orti_1 = new ortalama(45,80);
document.write("<br> Orti : "+orti_1.ortalama());  // 62.5

var name = "Furkan";
document.write("<br> Char at : "+name.charAt(2));  // Furkan'ın 2.indexindeki char
document.write("<br>"+name.charCodeAt(4));  // 4.indisdeki karakter (a) 'nın ascii karşılığını verir (97)

var  p = "Yunus ";
var s = "Emre ";
var q = "Berber";
document.write("<br> Concat : "+p.concat(s,q));  // Yunus Emre Berber

document.write("<br> Ascii : "+String.fromCharCode(97,98,99,100));  // abcd

var go = "Linke git !"
document.write("<br>"+go.link("http://www.emreberber.com"));  // Link oluşturma

var rpl = "Windows 8";
document.write("<br>"+rpl.replace("8","10"));  // Windows 10

var src = "Bugün saat 10'da okula gideceğim";
document.write("<br>"+src.search("okul"));  // 17 : indexi geri döndürür
document.write("<br>"+src.slice(5,16));  // saat 10'da 

var formul = "Suyun Formülü : ";
var h = "2";
document.write("<br>"+formul+"H"+h.sub()+"O");  // Suyun Formülü : H2O  (2'yi alt simge halinde yazar)

document.write("<br>"+src.toLowerCase());  // bugün saat 10'da okula gideceğim
document.write("<br>"+src.toUpperCase());  // BUGÜN SAAT 10'DA OKULA GIDECEĞIM 

document.write("<br> Date() is : "+Date());  // Sat Oct 07 2017 21:43:35 GMT+0300 

var tarih = new Date();
document.write("<br> getDate() is : "+tarih.getDate());  // 7 : Ayın kaçı oldugunu verir
document.write("<br> getDay() is : "+tarih.getDay());  // 6 : Cumartesi
document.write("<br> Full Year is : "+tarih.getFullYear());  // 2017
document.write("<br> Get Moonth is : "+tarih.getMonth());  // 9 : Ekim

var datenow = new Date("May 16, 2017 23:15:17");
document.write("<br>"+datenow.toLocaleDateString());  // 16.05.2017 

document.write("<br> Hours : "+tarih.getHours());  // 21
document.write("<br> Minute : "+tarih.getMinutes());  // 52

document.write("<br> ScreenX is : "+window.screenX);  // -8
document.write("<br> ScreenY is : "+window.screenY);  // -8

function yazdir()
{
    window.print();
}

function asagi()
{
    window.scrollBy(20,-50);
}

function yukari()
{
    window.scrollBy(20,+150);
}


document.write("<br> Title : "+document.title);  // Document 
document.write("<br> URL : "+document.URL);  // file:///C:/Users/Emre/Desktop/Script/index.html 

function ekle()
{
    var input = document.createElement("input");
    input.value="Merhaba ben input";
    input.placeholder="Placeholder !!!";
}

document.write("<br> Width : "+screen.width);  // 1366
document.write("<br> Height : "+screen.height);  // 768

function ctrl(e)
{
    if(e.ctrlKey)
    document.write("Ctrl Tuşuna bastınız");
}

window.onkeydown=ctrl;

