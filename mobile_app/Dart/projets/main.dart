
import 'dart:io';


int plusMoins(int nombre, int result)
{
    if(nombre > result)
        print("Le nombre est trop grand\n");
    if(nombre > result)
        print("Le nombre est trop petit\n");


    return 0;   
}

class Fraction
{
    int m_nume, m_deno;

    Fraction(this.m_nume, this.m_deno)
    {
        if (this.m_deno == 0)
        {
            erreur();
        }
    }
    
    Fraction.simple(this.m_deno) : this.m_nume = 1;

    // operation mathematique :
    Fraction operator+(Fraction frac2)
    {
        this.m_deno = this.m_deno + frac2.m_deno;
        this.m_nume = this.m_nume + frac2.m_nume;

        return this;
    }

    Fraction operator-(Fraction frac2)
    {
        

        int deno = this.m_deno - frac2.m_deno;
        int nume = this.m_nume - frac2.m_nume;

        if(deno == 0 )
        {
            print("aucun changement\n");
            nume = this.m_nume;
            deno = this.m_deno;
        }


        return new Fraction(nume, deno);
    }

    
    Fraction operator*(Fraction frac2)
    {
        int deno = this.m_deno * frac2.m_deno;
        int nume = this.m_nume * frac2.m_nume;

        return new Fraction(nume, deno);
    }

    Fraction operator/(Fraction frac2)
    {
        int tmp = frac2.m_deno;
        frac2.m_deno = frac2.m_nume;
        frac2.m_nume = tmp;
        
        return  this * frac2;
    }


    // comparaison
    bool operator>(Fraction frac2) => this.realvalue > frac2.realvalue;
    bool operator<(Fraction frac2) => this.realvalue < frac2.realvalue;
    bool operator>=(Fraction frac2) => this.realvalue >= frac2.realvalue;
    bool operator<=(Fraction frac2) => this.realvalue <= frac2.realvalue;
    //bool operator==(Fraction frac2) => this.realvalue == frac2.realvalue;
    //
    /* bool operator==(Fraction rect)
    {
        if (rect.realvalue > this.realvalue)
        {
            return true;
        }

        return false;
    }*/


    // methodes :
    double get realvalue => (m_deno/m_nume);

    void erreur()
    {
        while (this.m_deno == 0){
            print("le deno vaut ${this.m_deno}");
                int? output = int.tryParse(stdin.readLineSync()!);
                if (output != null){
                    this.m_deno = output;
                }

        }
    }

    void affichage()
    {
        print("${this.m_nume} / ${this.m_deno}");
    }

    // fin Class
}

void mainPlusMoins()
{
        int result = 100;
    int i;
    bool used = false;
    int compteur = 0;
  // read terminal

    int nombre = 0;
    List<int> taper = [];


    while (nombre != result){
        print("Entrer un nombre entre 0 et 100\n");
        try{
            nombre = int.parse(stdin.readLineSync()!);
        }
        catch(e)
        {
            print(e);
        }        
        for (i = 0; i < taper.length; i++)
        {
            if (taper[i] == nombre)
                used = true;
        }
        if (used){
            print("already used number : restart\n");
            used = false;
        }
        else
        {
            result = 0;
            taper.add(nombre);
            plusMoins(nombre, result);
        }
        if (compteur == 3)
            break;
        compteur++;
    }
}

int main() 
{
    Fraction prem = new Fraction(4, 3);
    Fraction sec = new Fraction(2, 5);

    prem.affichage();
    sec.affichage();

    (prem + sec).affichage();
//    print ( "produit = ${(prem * sec).affichage()}")

    return 0;
}
