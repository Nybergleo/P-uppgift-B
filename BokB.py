class Bok:  #Klassen för Bok
    def __init__(self, name, author, status, lånetagare,debt):  #Skapar klassens object
        self.name = name
        self.author = author
        self.status = status
        self.lane = lånetagare
        self.debt = debt


    def borrow(self,timedelta,user):  # Metoden för att ändra kanal T = tillgänglig, U = utlånad
        if self.status == "Availible":
            self.status = timedelta
            self.lane = user
            return True
        else:
            return False

    def return_bok(self,user):
        if self.status != "Availible":
            self.status = "Availible"
            self.lane = user
            return True
        else:
            return False
    def debt_calc(self,wks_late):
        if wks_late != 0:
            self.debt = wks_late*10

    def __str__(self):  # Returnerar en sträng av objekten i terminalen
        return f"Boktitel: {self.name}\nFörfattare: {self.author}\nReturdatum/Status: {self.status}\n"

    def str_for_file(self):  # Returnerar
        return f"{self.name},{self.author},{self.status},{self.lane},{self.debt}\n"

