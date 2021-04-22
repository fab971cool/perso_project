
import 'dart:io';

String affichage(String mot, String copy, [String? letter])
{
    if (letter != null)
    {
        for (int i = 0; i < mot.length; i++)
        {
            if (letter.compareTo(mot[i]) == 0){
                copy = copy.substring(0, i) + letter + copy.substring(i+1);
            }
            else
                print("${copy[i]}");
        }
        //print("\n");
    }
    else
    {
        print("${copy}");
        
    }

    return copy;
}

void main()
{
    String? mot = "test";
    String copy = "";
    

    int i, cpt = 0;
    bool noLetter = true;
    
    // Lecture personne
    for (i = 0; i < mot.length; i++){
        copy += '*';

    }
    print("${copy.length}");
    String? lettre = "e";
    while(true)
    {
        for (i = 0; i < mot.length; i++)
        {
            if (mot[i].compareTo(lettre![i]) == 0){
                noLetter = false;
                break;
            }
        }
        if (!noLetter)
            lettre = null;
            copy = affichage(mot, copy, lettre );
        if (cpt == 3)
            break;
        cpt++;
    }


}