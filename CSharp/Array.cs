/*
><><><><><><><><><><><><><><><><><><><><><><><><><><><
>													 
>              Developer :  Emre Berber
>		Filename :  Array.cs
>		   Other :  emreberber.com 
>
><><><><><><><><><><><><><><><><><><><><><><><><><><><
*/


using System;


namespace Array
{
    class Program
    {
        static void Main(string[] args)
        {
            //Dizi Tanımlama
            int[] array = new int[10];
            //new anahtar kelimesi ile tanımlandığı için dizinin her elemanına
            //temel veri türleri için varsayılan değer , ilk değer olarak verileceğini göstermekte.
            //Örnegin int için varsayılan deger 0 (sıfır) 'dır.

            array[2] = 7;
            string[] S_array = { "one", "two", "three" };

            //Dinamik dizi oluşturma
            int val = 20;
            int[] D_array = new int[val];

            //Birden fazla dizinin tanımlanması
            int[] array1 = new int[10], array2 = new int[10];

            //Birden fazla dizi bildirimi
            int[] dizi3, dizi4;

            //Foreach döngüsü ile dizinin elemanlarını sadece okuyabiliriz.
            int[] F_array = { 1, 2, 3, 4, 5 };
            foreach (int elt in F_array)
                Console.WriteLine(elt);
                //elt=3; gibi yazma işlemleri kullanamayız.

            
            Console.ReadKey();
        }
    }
}
