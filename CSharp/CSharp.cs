/*
><><><><><><><><><><><><><><><><><><><><><><><><><><><
>													 
>              Developer :  Emre Berber
>		Filename :  CSharp.cs
>		   Other :  emreberber.com 
>
><><><><><><><><><><><><><><><><><><><><><><><><><><><
*/


using System;


namespace CSharp  // Program.cs dosyasında dahil edeğemiz alan
{
    public class RastgeleSayi
    {
        private Random rnd = new Random();
        private int mSayi;

        public int Sayi { get { return mSayi; } }
        
        public RastgeleSayi()
        {
            mSayi = rnd.Next(0, 100);
        }

        public void Degistir()
        {
            mSayi = rnd.Next(0, 100);
        }
    }
}
