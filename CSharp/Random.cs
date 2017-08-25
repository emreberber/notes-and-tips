/*
><><><><><><><><><><><><><><><><><><><><><><><><><><><
>													 
>              Developer :  Emre Berber
>		Filename :  Random.cs
>		   Other :  emreberber.com 
>
><><><><><><><><><><><><><><><><><><><><><><><><><><><
*/


using System;


namespace Random_
{
    class Program
    {
        static void Main(string[] args)
        {

            Random Rnd = new Random();

            int rnd1 = Rnd.Next(7, 70);    //  7 ile 70 arası
            int rnd2 = Rnd.Next(61);    //  0 ile 61 arası
            int rnd3 = Rnd.Next();  //  int türünden pozitif
            double rnd4 = Rnd.NextDouble(); //  0.0 ile 1 arası double

        }
    }
}
