# ogrenci bilgilerini iceren sınıf
class studentClass:
    def __init__(self, nameofStudent, surnameofStudent, classofStudent):
        self.nameofStudent = nameofStudent
        self.surnameofStudent = surnameofStudent
        self.classofStudent = classofStudent

    def showInformation(self):
        print(""" 
              nameofStudent : {}
              surnameofStudent : {}
              ogrenciSinif : {}
              """.format(self.nameofStudent, self.surnameofStudent, self.classofStudent))

# net sayisini hesaplar, net sayisi ile total puanı da hesaplar
class questions:
    @staticmethod
    def NetSayisi(correct, wrong):
        wrongplus = int(wrong /4)
        totalNet = correct - wrongplus
        print("""
            numberofCorrectAnswer : {}
            numberofwrongAnswer : {}
            numberofogrenciNet : {}
            """.format(correct, wrong, totalNet))
        return totalNet

    @staticmethod
    def calculate(totalNet):
        totalPoints = totalNet * 2
        print(""" 
              ogrencitotalPointsi : {}
              """.format(totalPoints))

studentName = input("Ogrenci ismi giriniz:")
studentSurname = input("Ogrenci soyismi giriniz:")
studentClassLocal = input("Ogrenci sinifini giriniz:")

# toplam 50 soru mu kontrolü
while True:
    correctAnswer = int(input("Ogrenci doğru sayısını giriniz:"))
    wrongAnswer = int(input("Ogrenci yanlış sayısını giriniz:"))

    if(correctAnswer + wrongAnswer != 50):
        print("Lutfen yanlis ve doğru toplamı 50 olacak şekilde doğru yanlis sayısını giriniz.")
    else:
        break

studentOutput = studentClass(studentName, studentSurname, studentClassLocal)
studentOutput.showInformation()

questionOutputs = questions()
totalNets = questionOutputs.NetSayisi(correctAnswer, wrongAnswer)
questionOutputs.calculate(totalNets)