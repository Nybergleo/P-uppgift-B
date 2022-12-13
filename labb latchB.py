from datetime import date,timedelta    #TID
t = date.today() + timedelta(days=21)
t2 = date.today()
tdiff = -(date.today() - t)
print(t)
print(t2)
print(tdiff)
"""
def read_file(filnamn):   # B- nivå read file
    fil_lista = []
    fil = open(filnamn, "r")
    fil_rader = fil.read().splitlines()

    for rad in fil_rader:
        rad_som_lista = rad.split(",")
        if filnamn == "Användare.txt":
            anv = (rad_som_lista[0], rad_som_lista[1], rad_som_lista[2], rad_som_lista[3])
            fil_lista.append(anv)
        else:
            bok = (rad_som_lista[0], rad_som_lista[1], rad_som_lista[2], rad_som_lista[3])
            fil_lista.append(bok)


    fil.close()
    return fil_lista

def inlogg(anvregister):   #INlogg använd skiss

   while True:
    anv_ele = "z"
    anv = input("Input Username: ")
    password = input("Input Password: ")
    try:

        for i in range(0,len(anvregister)):
            if anv == anvregister[i][0]:
                anv_ele = i  #användaren skriv som till elementet
        if anv == anvregister[anv_ele][0] and anvregister[anv_ele][2] == password:
            print(anvregister[anv_ele])
            return False
    except:
        print("Antingen lösenord eller Användarnamn är fel. Försök igen")
"""

låneskuld fakta:
    oftast är lånetiden 3 veckor

    försening 10 kr per exemplar och påbörjad vecka
    Förseningsavgiften kan högst bli 100 kr per exemplar.


Admin funktioner
    Lägga till användare
        viktigt kolla på så folk skriver in rätt format

    Ta bort användare

    Lista på alla anvädare med lånade böcker samt vilka böcker det är
        utgångna lånedatum ska MARKERAS

    En lista med BARA användare med SENA BÖCKER
        Sammanlagd skuld samt vilka böcker ska visas


Gustav,Gusry@kth.se,0210302436,snorre,A,0
Henning,hennish@kth.se,0410322436,lol,U,0
Leo,leony@kth.se,0310302436,Kuk,A,0
Viktor,vich@kth.se,0210302736,Balle,U,0
Wictor,wict@kth.se,323242554,Snopp,U,0
Lisa,lisalo@kth.se,0303032456,BBC,A,0

