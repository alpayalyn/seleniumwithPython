class Person():
    def __init__(self):
        self.name = "Alpay"
        self.surname = "Alin"
        self.age = 24
        self.country = "Turkey"
        self.city = "Istanbul"
        self.skillList = []
        
    def addSkills(self):
        skill = input("Which skill you want to add?")
        self.skillList.append(skill)

    def personInformation(self):
        return self.name, self.surname, self.age, self.country, self.city, self.skillList

aboutPerson = Person()
while True:
    answer = input("Do you want to add skill into the skills list? Y / N")

    if(answer == "Y"):
        aboutPerson.addSkills()
        print(aboutPerson.personInformation())

    else:
        aboutPerson.personInformation()
        break