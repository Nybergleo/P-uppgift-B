

import pickle
from datetime import datetime,date, timedelta


from BokB import Bok  # klassen "Bok" importeras
from AnvB import Anv



# Allmänna funktioner

def write(fil, listaAvA):
    filp = open(fil, "wb")
    pickle.dump(listaAvA, filp)
    filp.close()


def load(fil):
    filp = open(fil, "rb")
    utlista = pickle.load(filp)
    filp.close()
    return utlista

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


def return_book(bibliotek, bok):
    if bibliotek[bok].return_bok() == True:  # Om boken är utlämnad returneras den.
        write("BibliotekB_test.txt",bibliotek)
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
        new_bok = Bok(input("Skriv in bokens titel: "), input("Skriv in bokens författare"), "Availible", "N/A",0)
        bibliotek.append(new_bok)
        print(f"boken {new_bok.name} är nu inlagd")
        write("BibliotekB_test.txt",bibliotek)
    else:
        print("Ogiltigt alternativ")
        gen_menu(anv)

def add_social(userregister): # bara siffror i personnr
   social = input("Socialsecurity number formated YYMMDDXXX: ")
   try:
       int(social)
       if len(social) != 10:
           retry = input("The format should be YYMMDDXXXX, try again or press 'E' to exit: ")
           if retry == "E":
               return
           return add_social(userregister)
       for a in userregister:
           if social == a.social:
                choice = input("The given social security number is already registered. To register a different"
                               " social security number press 'S', press anything else to exit")
                if choice == "S":
                    return add_social(userregister)
                else:
                    return
       return social
   except:
       print("Your social security number should be writen numericly YYMMDDXXXX")
       add_social(userregister)

def add_usr_auth():
    user_auth = input("Vilken typ av användare önskas läggas till? A för Administratör eller U för User: ")
    if user_auth != "U" and user_auth != "A":
        return add_usr_auth()
    return user_auth

def add_usr_password():
    pass1 = input("Input password: ")
    pass2 = input("Repeat your password: ")
    if pass1 != pass2:
        print("The passwords do not match, please try again.")
        return add_usr_password()
    else:
        return pass1

def add_usr(userregister, anv):
    if anv.check_auth() == True:
        soc = add_social(userregister)
        if soc == None:
            return
        new_us = Anv(input("Ange ditt förnamn: "), input("Ange din mail: "),soc, add_usr_password(),add_usr_auth(),0)
        print(new_us)
        userregister.append(new_us)
        list_sort(userregister)
        write("anvregB_test.txt",userregister)
        print(new_us.name,"is now added to the register")
    else:
        print("Action does not exist")
        gen_menu(anv)


def remove_book(bibliotek,anv):  # tar bort en bok.

    if anv.status == "A":
        bok = search_bok(bibliotek)
        if bok == None:
            return
        bibliotek.remove(bibliotek[bok])
        write("BibliotekB_test.txt",bibliotek)
    else:
        print("Action does not exist")
        gen_menu(anv)

def remv_usr(anvreg,anv,library):
    if anv.check_auth() == True:
        rem_anv_ele = search_usr(anvreg,anv)
        if rem_anv_ele == None:
            return
        elif anv.social != anvreg[rem_anv_ele].social:
            for book in library:
                if book.user == anvreg[rem_anv_ele].name:
                    return_book(library,book)
            print(f"{anvreg[rem_anv_ele].name} är nu borttagen.")
            anvreg.remove(anvreg[rem_anv_ele])
            write("anvregB_test.txt",anvreg)
        elif anv_auth.social == anvreg[rem_anv_ele].social:
            print("Du kan inte ta bort dig själv!")
    else:
        print("Ogiltigt alternativ")
        gen_menu(anv)

def search_usr(anvreg,användare):
    try:
        if användare.check_auth() == True:
            sear_us = input("What user are you searching?: ")
            for users in range(len(anvreg)):
                if sear_us == anvreg[users].name:
                    return users  # Returnerar elementet boken är i listan
                elif sear_us == "E":
                    return
            print("The user you are searching does not exist, try again or press 'E' to exit")
            return search_usr(anvreg,användare)
        print("Ej gilltigt alternativ")
        gen_menu()
    except:
        print("Ett oväntat fel har uppstått")


def list_borrowed_books(library,userreg,us):
    if us.check_auth()==True:
        bor_bok = []
        borrower = userreg[search_usr(userreg,us)].name
        for bok in library:
            if bok.user == borrower:
                bor_bok.append(bok)
        return bor_bok
    else:
        print("Action does not exist")
        gen_menu(anv)


def book_debt_calc(library):
    for bok in library:
        if isinstance(bok.status,date):
            if int((bok.status - date.today()).days) < 0:
                days_lt = int((bok.status - date.today()).days)
                wks_late = int(days_lt)//7
                bok.debt_calc(wks_late)
                write("BibliotekB_test.txt",library)

def usr_debt(usrreg,library):
    for usr in usrreg:
        us_debt = 0
        for bok in library:
            if usr.name == bok.user:
                us_debt += bok.debt
        usr.debt_calc(us_debt)
        write("anvregB_test.txt",usrreg)

def books_bor_by_usr(usrreg,library):

    for usr in usrreg:
        print(usr.name,usr.social)
        for bok in library:
            if usr.name == bok.user:
                if bok.debt != 0:
                    print(bok, "***")
        usr.debt_calc(us_debt)
        write("anvregB_test.txt",usrreg)












def main():
    bibliotek = load("BibliotekB_test.txt")
    anvreg = load("anvregB_test.txt")
    anvreg = list_sort(anvreg)
    bibliotek = list_sort(bibliotek)
    action = 1
    #anv = log_in(anvreg)
    anv = anvreg[3]  # Tillfällig grej för att slippa logga in
    print("Välkommen till Biblioteket!")
    gen_menu(anv)
    while action != "S":
        book_debt_calc(bibliotek)
        usr_debt(anvreg,bibliotek)
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
            borrow(bibliotek,bok,anv)
        elif action == "Å":
            bok = search_bok(bibliotek)
            if bok == None:
                continue
            return_book(bibliotek,bok)
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
    #write_file(bibliotek, "BibliotekB.txt")
bibliotek = load("BibliotekB_test.txt")
for books in bibliotek:
    print(str(books))
