import copy
from datetime import datetime,date, timedelta  # Tidstillägg för lånande av böcker

from BokB import Bok  # klassen "Bok" importeras
from AnvB import Anv


# Allmänna funktioner
def read_file(filnamn):  # Läser in filen
    try:
        fil_lista = []
        fil = open(filnamn, "r")
        fil_rader = fil.read().splitlines()

        for rad in fil_rader:
            if filnamn == "BibliotekB.txt":
                rad_som_lista = rad.split(",")
                bok = Bok(rad_som_lista[0], rad_som_lista[1], rad_som_lista[2],rad_som_lista[3],rad_som_lista[4])
                fil_lista.append(bok)
            elif filnamn == "anvregB.txt":
                rad_som_lista = rad.split(",")
                anv = Anv(rad_som_lista[0],rad_som_lista[1],rad_som_lista[2],rad_som_lista[3],rad_som_lista[4],rad_som_lista[5])
                fil_lista.append(anv)

        fil.close()
        return fil_lista
    except:
        print("Ett oväntat problem har uppstått")
        return None

def list_sort(lst):
    sort_list = []
    if isinstance(lst[0],Bok):
        lst.sort(key=lambda x: x.author, reverse=False)
        sort_list = sorted(lst, key=lambda x: x.author, reverse=False)
    elif isinstance(lst[0],Anv):
        lst.sort(key=lambda x: x.name, reverse=False)
        sort_list = sorted(lst, key=lambda x: x.name, reverse=False)
    return sort_list

def write_file(lista_med_objekt, filnamn):  # Skriver in ändringar programmet gjort i filen
    try:
        fil = open(filnamn, "w")
        for bok in lista_med_objekt:
            fil.write(bok.str_for_file())
        fil.close()
    except:
        print("Ett oväntat problem har uppstått")

def search_bok(boklista):  # Söker bok och returnerar elevmentet för den boken i listan
    try:
        sök_bok = input("Vilken bok söker du?: ")
        for bok in range(len(boklista)):
            if sök_bok == boklista[bok].name:
                return bok# Returnerar elementet boken är i listan
            elif sök_bok == "A":
                return
        print("boken du angivit finns ej, försök igen eller tryck 'A' för att avsluta")
        return search_bok(boklista)
    except:
        print("Ett oväntat fel har uppstått")

def list_all(bibliotek):  # skriver ut alla element i biblan enligt ___str___ Bok klassen
    for bok in range(len(bibliotek)):
        print(bibliotek[bok])

def search_author(boklista):  # appendar böcker som matchar anginven författare och skriver därefter ut dessa böcker.
    try:
        ele_author = []
        inp_author = input("Vilken författare söker du?: ")
        if inp_author != "A":
            for bok in range(len(boklista)):
                if inp_author == boklista[bok].author:
                    ele_author.append(bok)
        else:
            return
        if ele_author != []:
            for ele in ele_author:
                print(f"{inp_author}: {boklista[ele].name} ({boklista[ele].status})")
        else:
            print("Ingen bok av den angivna författaren hittades, försök igen eller tryck 'A' för att avsluta")
            return search_author(boklista)

    except:
        print("Ett oväntat fel har uppstått.")



def borrow(bibliotek,bok,anv):
    borrow_time = date.today() + timedelta(days=28)
    if bibliotek[bok].borrow(borrow_time,anv) == True:  # Checkar om boken är utlånad, om inte lånas den ut i 21 dagar
        print(f"{bibliotek[bok].name} är nu utlånad. Returneras senast {bibliotek[bok].status}.")
    else:  # Boken är utlånad, Senaste returdatum skickas ut.
        print(f"Boken är utlånad. boken returneras {bibliotek[bok].status}")


def return_bok(bibliotek, bok):
    if bibliotek[bok].return_bok() == True:  # Om boken är utlämnad returneras den.
        write_file(bibliotek)
        print(f"{bibliotek[bok].name} är nu återlämnad.")
    else:  # Boken är redan hemma och kan inte returneras.
        print(f"Boken är Tillgänglig och kan därför inte returneras.")

def gen_menu(användare):
    if användare.check_auth() == True:
        print("\tT söka på Titel\n\tF söka på Författare.\n\tL Låna bok.\n\tÅ Återlämna bok.\n\tN lägga in Ny bok.\n\tB ta Bort bok.\n\tA lista Alla böcker.\n\t1 lägg till användare.\n\t2 ta bort användare\n\t3 Sök användare\n\tS Sluta.")
    elif användare.check_auth() == False:
        print("\tT söka på Titel\n\tF söka på Författare.\n\tL Låna bok.\n\tÅ Återlämna bok.\n\tA lista Alla böcker.\n\tS Sluta.")





def log_in(anvregister):
        try:
            anv_ele = len(anvregister) + 1
            anv = input("Input Username: ")
            password = input("Input Password: ")
            for i in range(len(anvregister)):
                if anv == anvregister[i].name :  # or anv == anvregister[i].mail or anv == anvregister[i].social:
                    anv_ele = i  # användaren skriv som till elementet
            if anv == anvregister[anv_ele].name and password == anvregister[anv_ele].password:
                return anvregister[anv_ele]
            print("Antingen Användarnamn eller lösenord är fel! Var god försök igen.")
            return log_in(anvregister)
        except IndexError:
            print("Antingen Användarnamn eller lösenord är fel! Var god försök igen.")
            return log_in(anvregister)
        except:
            print("Ett oväntat fel har uppstått")

#ADMIN FUNKTIONER

def add_bok(bibliotek,anv):  # Tillägg av ny bok.
    if anv.status == "A":
        new_bok = Bok(input("Skriv in bokens titel: "), input("Skriv in bokens författare"), "Availible")
        bibliotek.append(new_bok)
        print(f"boken {new_bok.name} är nu inlagd")
        write_file(bibliotek,"BibliotekB.txt")
    else:
        print("Ogiltigt alternativ")
        gen_menu(anv)

def add_social(userregister): # bara siffror i personnr
   social = input("Skriv person nr här: ")
   try:
       int(social)
       if len(social) != 10:
           print("Person nr ska skrivas i formatet ÅÅMMDDXXXX var god försök igen. Försök igen")
           add_social()
       for a in userregister:
           if social == a.social:
                print("Det angivna personnumret är redan registrerat för ett konto")
                return
       return social
   except:
       print("Person nr ska skrivas i formatet ÅÅMMDDXXXX var god försök igen. Försök igen")
       add_social(userregister)


def add_usr_auth():
    user_auth = input("Vilken typ av användare önskas läggas till? A för Administratör eller U för User: ")
    if user_auth != "U" and user_auth != "A":
        return add_usr_auth()
    return user_auth

def add_icke_spec(typ):
    import re
    input_str = input(f"Skriv {typ} här: ")
    if not re.match("^[a-zA-Z@£€.!0-9]*$", input_str):
        print("En otillåten symbol har använts!")
        return add_icke_spec(typ)
    return input_str

def add_usr(userregister,anv):
    if anv.check_auth() == True:
        name = add_icke_spec("namn")
        mail = add_icke_spec("mail")
        social = add_social(userregister)
        password = add_icke_spec("lösenord")
        auth = add_usr_auth()
        new_us = Anv(name,mail,social,password,auth,0)
        userregister.append(new_us)
        list_sort(userregister)
        write_file(userregister, "anvregB.txt")
        print(name,"är nu tillagd i användarregistret")
    else:
        print("Ogilitgt alternativ, var god försök igen!")
        gen_menu(anv)

def remove_book(bibliotek,anv):  # tar bort en bok.

    if anv.status == "A":
        bok = search_bok()
        if bok == None:
            return
        bibliotek.remove(bibliotek[bok])
        write_file(bibliotek,"BibliotekB.txt")
    else:
        print("Ogiltigt alternativ")
        gen_menu(anv)

def remv_usr(anvreg,anv):
    if anv.check_auth() == True:
        rem_anv_ele = search_usr(anvreg,anv)
        if anv.social != anvreg[rem_anv_ele].social:
            print(f"{anvreg[rem_anv_ele].name} är nu borttagen.")
            anvreg.remove(anvreg[rem_anv_ele])
            write_file(anvreg,"anvregB.txt")
        elif anv_auth.social == anvreg[rem_anv_ele].social:
            print("Du kan inte ta bort dig själv!")
    else:
        print("Ogiltigt alternativ")
        gen_menu(anv)

def search_usr(anvreg,användare):
    try:
        if användare.check_auth() == True:
            sear_us = input("Vilken användare söker du?: ")
            for users in range(len(anvreg)):
                if sear_us == anvreg[users].name:
                    return users  # Returnerar elementet boken är i listan
                elif sear_us == "A":
                    return
            print("Användaren du angivit finns ej, försök igen eller tryck 'A' för att avsluta")
            return search_usr(anvreg,användare)
        print("Ej gilltigt alternativ")
        gen_menu()
    except:
        print("Ett oväntat fel har uppstått")








def main():
    bibliotek = read_file("BibliotekB.txt")
    anvreg = read_file("anvregB.txt")
    anvreg = list_sort(anvreg)
    bibliotek = list_sort(bibliotek)
    action = 1
    anv = log_in(anvreg)
    print(anv.status)
    print("Välkommen till Biblioteket!")
    gen_menu(anv)
    print(type(anvreg))
    while action != "S":
        action = input("Vad vill du göra?: ")
        if action == "T":
            bok = search_bok(bibliotek)  # returnerar elementet boken är i biblioteket
            if bok == None:
                continue
            print(bibliotek[bok])
        elif action == "F":
            search_author(bibliotek)
        elif action == "L":
            bok = search_bok(bibliotek)
            if bok == None:
                continue
            borrow(bibliotek,bok)
        elif action == "Å":
            bok = search_bok(bibliotek)
            if bok == None:
                continue
            return_bok(bibliotek,bok)
        elif action == "N":
            add_bok(bibliotek,anv)
        elif action == "B":
            remove_book(bibliotek,anv)
        elif action == "A":
            list_all(bibliotek)
        elif action == "1":
            add_usr(anvreg,anv)
        elif action == "2":
            remv_usr(anvreg,anv)
        elif action == "3":
            print("finns ej")
        elif action == "S":
            print("Tack för idag, alla dina ändringar har blivit sparade!")
        else:
             gen_menu(anv)
    write_file(bibliotek, "BibliotekB.txt")

main()


"""
bibliotek = read_file("BibliotekB.txt")
anvreg = read_file("anvregB.txt")
print(bibliotek)
print(anvreg)"""