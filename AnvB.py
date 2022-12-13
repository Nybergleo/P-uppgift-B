class Anv:  #Klassen för Bok
    def __init__(self, name, mail,socialsecurity,password,status,debt):  #Skapar klassens object
        self.name = name
        self.mail = mail
        self.social = socialsecurity
        self.password = password
        self.status = status
        self.debt = int(debt)


    def check_auth(self):
        if self.status == "A":
            return True
        elif self.status == "U":
            return False




    def __str__(self):  # Returnerar en sträng av objekten i terminalen
        return f"namn: {self.name}\nMail: {self.mail}\nStatus: {self.status}\n"

    def str_for_file(self):  # Returnerar
        return f"{self.name},{self.mail},{self.social},{self.password},{self.status},{self.debt}\n"