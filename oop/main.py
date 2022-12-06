from Pojistenec import *
list_pojistenych = []
while True:
    print("---------")
    print("Evidence pojistenych")
    print("---------\n")
    print("Vyberte si akci:\n")
    print("1 - Pridat noveho\n2 - Vypsat vsechny\n3 - Vyhledat\n4 - Konec")
    prikaz = str(input())
    match prikaz:
        case '4':
            break
        case "1":
            a = input("Zadejte jmeno\n")
            b = input("Zadejte prijmeni\n")
            c = input("Zadejte vek\n")
            d = input("Zadejte telefonni cislo\n")
            e = Pojistenec(a,b,c,d)
            list_pojistenych.append(e)
            print("Data byla ulozena")
            input("Press Enter to continue...")
        case "2":
            for i in list_pojistenych:
                print(i)
            input("Press Enter to continue...")
        case "3":
            cislo = input("Vyhledejte telefonni cislo\n")
            for i in list_pojistenych:
                a = i.split("\t")
                if a[3] == cislo:
                    print(i)
                    break
                else:
                    continue
            input("Press Enter to continue...")
        case _:
            print("Tohle neni validni moznost")
            input("Press Enter to continue...")
            
            
                
                
        
            
    