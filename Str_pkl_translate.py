"""
Pkl till txt inmata "anvregB_test.txt" eller "BibliotekB_test.txt"
Txt till pkl inmata "anvregB.txt" eller "BibliotekB.txt"
"""

from datetime import datetime, date, timedelta
from BokB import Bok  # klassen "Bok" importeras
from AnvB import Anv
import pickle

def read_file(filnamn):  # Läser in filen
    fil_lista = []
    fil = open(filnamn, "r")
    fil_rader = fil.read().splitlines()

    for rad in fil_rader:
        if filnamn == "BibliotekB.txt":
            rad_som_lista = rad.split(",")
            bok = Bok(rad_som_lista[0], rad_som_lista[1], rad_som_lista[2], rad_som_lista[3], rad_som_lista[4])
            fil_lista.append(bok)
        elif filnamn == "anvregB.txt":
            rad_som_lista = rad.split(",")
            anv = Anv(rad_som_lista[0], rad_som_lista[1], rad_som_lista[2], rad_som_lista[3], rad_som_lista[4],
                      rad_som_lista[5])
            fil_lista.append(anv)

    fil.close()
    return fil_lista

def write_file(lista_med_objekt, filnamn):  # Skriver in ändringar programmet gjort i filen
    try:
        fil = open(filnamn, "w")
        for bok in lista_med_objekt:
            fil.write(bok.str_for_file())
        fil.close()
    except:
        print("Ett oväntat problem har uppstått")

def str_to_date(lista):
    for bok in lista:
        if bok.status != "Availible":
            bok.status = datetime.strptime(bok.status, '%Y-%m-%d').date()
    return lista


def write(fil, listaAvA):
    filp = open(fil, "wb")
    pickle.dump(listaAvA, filp)
    filp.close()


def load(fil):
    filp = open(fil, "rb")
    utlista = pickle.load(filp)
    filp.close()
    return utlista

def trans_to_pkl(fil):
    lista = read_file(fil)
    if fil == "BibliotekB.txt":
        lista2 = str_to_date(lista)
        write("BibliotekB_test.txt",lista2)
        franFil=load("BibliotekB_test.txt")
    else:
        write("anvregB_test.txt",lista)
        franFil = load("anvregB_test.txt")

def trans_to_txt(fil):
    lista = load(fil)
    print(type(lista[0]))
    if isinstance(lista[0],Bok):
        write_file(lista, "BibliotekB.txt")
    elif isinstance(lista[0], Anv):
        write_file(lista,"anvregB.txt")

trans_to_txt("anvregB_test.txt")
trans_to_txt("BibliotekB_test.txt")

