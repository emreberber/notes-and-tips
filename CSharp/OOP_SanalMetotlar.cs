/*
><><><><><><><><><><><><><><><><><><><><><><><><><><><
>													 
>              Developer :  Emre Berber
>		Filename :  OOP_SanalMetotlar.cs
>		   Other :  emreberber.com 
>
><><><><><><><><><><><><><><><><><><><><><><><><><><><
*/


using System;


class Sekil
{
    public double Boy;
    public double En;

    public Sekil(double boy , double en)
    {
        this.Boy = boy;
        this.En = en;
    }

    virtual public double Alan()
    {
        return 0;
    }
}

class Dortgen : Sekil
{
    public Dortgen(int boy , int en):base(boy , en)
    {

    }

    public override double Alan()
    {
        return En * Boy;
    }
}

class Ucgen : Sekil
{
    public Ucgen(int boy , int en):base(boy , en)
    {

    }

    override public double Alan()
    {
        return En * Boy / 2;
    }
}

class MainMetodu
{
    public static void AlanBul(Sekil sekil)
    {
        Console.WriteLine("Seklin Alanı : " + sekil.Alan());
    }

    static void Main(string[] args)
    {
        Ucgen ucgen = new Ucgen(10, 50);
        AlanBul(ucgen);

        Dortgen dortgen = new Dortgen(10, 50);
        AlanBul(dortgen);

        Sekil sekil = new Sekil(10, 50);
        AlanBul(sekil);

        Console.ReadKey();
    }
}

