/*
><><><><><><><><><><><><><><><><><><><><><><><><><><><
>													 
>              Developer :  Emre Berber
>		Filename :  OOP_Inheritance.cs
>		   Other :  emreberber.com 
>
><><><><><><><><><><><><><><><><><><><><><><><><><><><
*/


using System;

class Memeli  // Base Class
{
    public double Boy;
    public double Agirlik;

    public Memeli(double boy  ,double agirlik)
    {
        this.Boy = boy;
        this.Agirlik = agirlik;
    }

    public void OzellikGoster()
    {
        Console.WriteLine("Boy : " + Boy);
        Console.WriteLine("Agırlik : " + Agirlik);
    }
}

class Kedi : Memeli  // Derived Class
{
    public string Turu;

    public Kedi(string turu , int boy , int agirlik):base(boy , agirlik)
    {
        this.Turu = turu;
    }

    public void TurGoster()
    {
        Console.WriteLine(Turu + " Kedisi");
    }
}

// Kalıtım yoluyla sadece public ve protected elemanlar aktarılır.
// Base Class'da protected olarak tanımlanan elemanlar sadece kendi sınıfından türetilen sınıflardan erişilebilir

class MainMetodu
{
    static void Main(string[] args)
    {
        Kedi kedi1 = new Kedi("Van",5,10);

        // Boy ve Agirlik public tanımlandıgı icin buradan erisebiliyoruz
        // kedi1.Agirlik = 5;
        // kedi1.Boy = 10;
        // kedi1.Turu = "Van";

        kedi1.OzellikGoster();
        kedi1.TurGoster();

        Console.WriteLine("\n===============\n");

        Memeli memeli = new Memeli(6, 11);
        memeli.OzellikGoster();

        Console.ReadKey();
    }
}

