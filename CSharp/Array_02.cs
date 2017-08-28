/*
><><><><><><><><><><><><><><><><><><><><><><><><><><><
>													 
>              Developer :  Emre Berber
>		Filename :  Array_02.cs
>		   Other :  emreberber.com 
>
><><><><><><><><><><><><><><><><><><><><><><><><><><><
*/


using System;


namespace Array_02
{
    class Program
    {
        static void Main(string[] args)
        {

            // Düzensiz Diziler
            int[][] array = new int[3][];
            array[0] = new int[3];
            array[1] = new int[4];
            array[2] = new int[2];

            Console.WriteLine(array.GetLength(0));  // array dizisinin eleman sayısı
            Console.WriteLine(array[1].GetLength(0));   // array dizisinin 1.indisindeki eleman sayısı

            // Dizileri Kopyalama
            int[] array1 = { 1, 2, 3, 4 };
            int[] array2 = new int[10];

            array1.CopyTo(array2, 3);   // 3:Dizinin son indisi

            // Dizileri Sıralama
            int[] array3 = { 1, 8, 5, 6, 2 };
            Array.Sort(array3);

            string[] array4 = { "Emre", "Hasan", "Yakup" };
            Array.Sort(array4); // String türünden dizileri harf önceliğine göre sıralar

            // Dizilerde Arama
            // BinarySearch(Array,Aranan);
            // BinarySearch(Array,baslangıc,uzunluk,Aranan);
            // BinarySearch sıralanmış dizilerde arama yapabilir.

            int val=Array.BinarySearch(array4, "Yakup");
            Console.WriteLine(val); // Eger bulunursa indexi döndürür,bulunmazsa negatif sayı döndürür.

            // Clear
            Array.Clear(array3, 1, 2);  // 1.elemandan itibaren 2 elemanı sıfırlar.

            // Reverse
            Array.Reverse(array2);  // Diziyi ter çervirme
            Array.Reverse(array2, 1, 2);    // 1.elemandan itibaren ilk 2 elemanı ters çevirir.


            Console.ReadKey();
        }
    }
}
