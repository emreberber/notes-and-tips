/*
><><><><><><><><><><><><><><><><><><><><><><><><><><><
>													 
>              Developer :  Emre Berber
>		Filename :  Matrix.cs
>		   Other :  emreberber.com 
>
><><><><><><><><><><><><><><><><><><><><><><><><><><><
*/


using System;


namespace Matrix
{
    class Program
    {
        static void Main(string[] args)
        {
            int[ , ] array = { { 1,2 } , { 3,4 } , { 5,6 } };
            // array[1,1]=4 olmuş olur.

            int[ , , ] array1 = { { { 1,2 },{ 3,4 } } , { { 5,6 }, { 7,8 } } }; // 3 Boyutlu

            int val = 3;
            int[,] dizi2 = new int[val, val];


        }
    }
}
