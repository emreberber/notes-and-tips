/*
><><><><><><><><><><><><><><><><><><><><><><><><><><><
>													 
>              Developer :  Emre Berber
>		Filename :  OOP_CLass.cs
>		   Other :  emreberber.com 
>
><><><><><><><><><><><><><><><><><><><><><><><><><><><
*/


using System;
using CSharp;  // Sınıf kütüphanesi kullanma   


    class MainMetodu
    {
        static void Main()
        {
        RastgeleSayi r = new RastgeleSayi();  // RastgeleSayi sınıfından r nesnesini oluşturduk
        Console.WriteLine(r.Sayi);

        r.Degistir();
        Console.WriteLine(r.Sayi);

        Console.ReadKey();
        }
    }

