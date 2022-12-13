


"""
def add_social(userregister): # bara siffror i personnr
   social = input("Välj lösenord")
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
       add_user()

def add_usr_auth():
    user_auth = input("Vilken användar typ önskas läggas till? A för Administratör eller U för User")
    if user_auth != "U" or user_auth != "A":
        return add_usr_auth()
    return user_auth

def add_name_pass(typ):
    print(f"Skriv {typ} här: ", end='')
    inp = input()
    if inp.isalnum() == False:
        print("Nu blev det tokigt")
        return add_name_mail_pass(typ)
    return inp

def add_icke_spec(typ):
    import re
    input_str = input(f"Skriv {typ} här: ")
    if not re.match("^[a-zA-Z@£€.!0-9]*$", input_str):
        print("En otillåten symbol har använts!")
        return add_mail(typ)
    return input_str

def add_usr(userregister,anv):
    name = add_name_mail_pass()
    mail = add_name_mail_pass()
    social = add_social(userregister)
    password = add_name_mail_pass()
    auth = add_usr_auth()
    new_us = Anv(name,mail,social,password,auth,0)
    userregister.append(new_usr)
    list_sort(userregister)
    write_file(userregister, "anvregB.txt")


def add_usr(userregister,anv):  # Tillägg av ny användare, KOLLA PÅ PERSSONNUMMER KN BLI KNAS
    print(userregister)
    old_reg = copy.deepcopy(userregister)
    print(old_reg)
    if anv.check_auth() == True:
        auth = input("Vilken typ av användare önskas skapas? 'A' för admin och 'U'för vanlig användare: ")
        if auth == "E":
            return
        elif auth != "A" and auth != "U":
            print("Inkorrekt användartyp, var god försök igen. Skriv 'E' för att avsluta")
            return add_usr(userregister,anv)
        social = input("Ange Person nr: ")
        if social == "E":
            return
        try:
            int(social)
            for a in userregister:
                if social == a.social:
                    print("Ditt person nr är redan registrerat!")
                    return
            if len(social) != 10:
                print("Person nr ska skrivas i formatet ÅÅMMDDXXXX var god försök igen. Försök igen eller 'E' för att avsluta, try")
                add_user(userregister,anv)
        except:
            print("Person nr ska skrivas i formatet ÅÅMMDDXXXX var god försök igen. Försök igen, except")
            add_usr(userregister,anv)

        new_usr = Anv(input("Nya användarens namn: "),input("Nya användarens mail: "),social,input("Ange lösenord: "),auth,0)
        userregister.append(new_usr)
        list_sort(userregister)
        write_file(userregister,"anvregB.txt")
        if read_file("anvregB.txt") != None:
            print(f"Användaren {new_usr.name} är nu inlagd")
        else:
            print("Din inmatning är inkorrekt, var god kontollera att inget ',' är med i någon input. Användarregistret är oförändrat")
            print(old_reg)
            print(userregister)
            write_file(old_reg,"anvregB.txt")
            add_usr(userregister,anv)



add_mail("namn")
"""
from datetime import date, datetime, timedelta
from BokB import Bok

bok = Bok("Pippi Langstrump","Astrid Lindgren","2022-12-01","N/A",0)




str_datum = "2022-12-12"

returdatum  = datetime.strptime(str_datum, '%Y-%m-%d').date()
print(date.today()-timedelta(days=11))
= timedelta_series.dt.days
print(type(returdatum))
print(returdatum)
def debt_calc_book(book):
    returdatum = datetime.strptime(book.status, '%Y-%m-%d').date()
    print(returdatum - date.today())
    """if days= > returdatum - date.today():
        datetime.date(book.status) - date.today()"""

debt_calc_book(bok)