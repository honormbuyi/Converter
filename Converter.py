
choix = "0"
while not choix == "1000":
    print()
    print()
    print("CONVERTISSEZ")
    print()
    print("Choissisez une option : ")
    print()
    print("1 - USD - FC")
    print("2 - FC - USD")
    print("3 - Taux d'echange")
    print("4 - Paramètre")
    print()
    choix = input("Votre choix est : ")

    if choix > "4":
                print("OUPS: vous devez choisir une option")
    try:
        choix4 = int(choix)
       
    except:
        print()
        print("OUPS: vous devez choisir une option")

    
    if choix == "1" :
        
        print()
        chx1 = input("Entrez le montant : ")   
        try:
            error = int(chx1)
        except:
            print()
            print("OUPS: vous devez rentrer un montant")
        else:
            conversion = int(chx1) * 2900

            print()
            print(f" {str(chx1)} USD = {str(conversion)} FC ")
    

    if choix == "2" :
        
        print()
        chx1 = input("Entrez le montant : ")   
        try:
            error = int(chx1)
        except:
            print()
            print("OUPS: vous devez rentrer un montant")
        else:
            conversion = int(chx1) / 2900

            print()
            print(f" {str(chx1)} FC = {str(conversion)} USD ")


    
    if choix == "3" :
         
         print()
         print("1 USD = 2900 FC")
         print()


    
    if choix == "4" :
        print()
        print("1 - Modifier le taux d'echange")
        print("2 - Quitter")
        print()
        choose = input("Votre choix est : ")

        if choose > "2":
                    print("OUPS: vous devez choisir une option")
        try:
            choix4 = int(choose)
        
        except:
            print()
            print("OUPS: vous devez choisir une option")



        if choose == "1" :
            print()
            print("Taux d'echange actuel : 1 USD = 2900 FC ")
            chx1 = input("Voulez-vous modifier 1 USD par : ")
        try:
            choix4 = int(chx1)
        
        except:
            print()
            print("OUPS: vous devez un montant en nombre")

        else :
            print()
            print("Le taux d'echange a été modifier avec succés")

            tx = chx1
            choix = "0"
            while not choix == "1000":
                print()
                print()
                print("C'est parti !")
                print()
                print("Choissisez une option : ")
                print()
                print("1 - USD - FC")
                print("2 - FC - USD")
                print("3 - Taux d'echange")
                print("4 - Restaurer")
                print()
                choix = input("Votre choix est : ")

                if choix > "4":
                            print("OUPS: vous devez choisir une option")
                try:
                    choix4 = int(choix)
                
                except:
                    print()
                    print("OUPS: vous devez choisir une option")

                
                if choix == "1" :
                    
                    print()
                    chx1 = input("Entrez le montant : ")   
                    try:
                        error = int(chx1)
                    except:
                        print()
                        print("OUPS: vous devez rentrer un montant")
                    else:
                        conversion = int(chx1) * int(tx)

                        print()
                        print(f" {str(chx1)} USD = {str(conversion)} FC ")
                

                if choix == "2" :
                    
                    print()
                    chx1 = input("Entrez le montant : ")   
                    try:
                        error = int(chx1)
                    except:
                        print()
                        print("OUPS: vous devez rentrer un montant")
                    else:
                        conversion = int(chx1) / int(tx)

                        print()
                        print(f" {str(chx1)} FC = {str(conversion)} USD ")


                
                if choix == "3" :
                    
                    print()
                    print(f"1 USD = {tx} FC")
                    print()
                
                if choix == "4" :
                     break
                   



        if choose == "1" :
              
             break               
                        
                




                    
                    
