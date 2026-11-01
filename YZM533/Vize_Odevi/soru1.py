
class ogrenci:
    def __init__(self):
        self.name = ""
        self.year_born = ""
        self.midterm_grade = ""
        self.final_grade = ""
        self.gpa = ""
        self.letter_grade = ""

def gpa_calculator(midterm, final):
    return (midterm * 0.4) + (final * 0.6)

def gpa_to_letter_grade(gpa):
    if gpa >= 90:
        return "AA"
    elif gpa >= 85:
        return "BA"
    elif gpa >= 80:
        return "BB"
    elif gpa >= 75:
        return "CB"
    elif gpa >= 70:
        return "CC"
    elif gpa >= 65:
        return "DC"
    elif gpa >= 60:
        return "DD"
    else:
        return "FF"

# Öğrencilerin olduğu objeler kümesi
students = []
while True:
    # Kaç öğrenci olduğu bilgisinin kullanıcıdan alınması
    num_students = int(input("Bilgileri girilecek öğrenci sayısını giriniz: "))

    # Öğrneci objelerinin oluşturulup students listesine eklenmesi
    for i in range(num_students):
        ogr = ogrenci()
        students.append(ogr)

    # Öğrenci bilgilerinin kullanıcıdan alınması
    for i in range(num_students):
        students[i].name = str(input(f"{i+1}. Öğrencinin Adı: "))
        students[i].year_born = int(input(f"{i+1}. Öğrencinin Doğduğu Yıl: "))
        # Not değerlerinin 0-100 arasında olduğunun doğrulanması
        while True:
            students[i].midterm_grade = float(input(f"{i+1}. Öğrencinin Vize Notu: "))
            if students[i].midterm_grade <= 100.0 and students[i].midterm_grade >= 0.0:
                break
            else:
                print("Lütfen 0 ile 100 arasında bir değer giriniz.")
        while True:
            students[i].final_grade = float(input(f"{i+1}. Öğrencinin Final Notu: "))
            if students[i].final_grade <= 100.0 and students[i].final_grade >= 0.0:
                break
            else:
                print("Lütfen 0 ile 100 arasında bir değer giriniz.")
        # Öğrencinin not ortalamasının ve harf notunun hesaplanması
        students[i].gpa = gpa_calculator(students[i].midterm_grade, students[i].final_grade)
        students[i].letter_grade = gpa_to_letter_grade(students[i].gpa)
        
    # Öğrenci bilgilerinin ekrana yazdırılması
    if num_students == 0:
        print("Hiçbir öğrenci bilgisi girilmedi.")
    elif num_students == 1:
        print("Adı: ", students[0].name)
        print("Doğum Yılı: ", students[0].year_born)
        print("Not Ortalaması: ", students[0].gpa)
        print("Harf Notu: ", students[0].letter_grade)   
    else:
        for i in range(num_students):
            print(f"{i+1}. Öğrenci:")
            print("Adı: ", students[i].name)
            print("Doğum Yılı: ", students[i].year_born)
            print("Not Ortalaması: ", students[i].gpa)
            print("Harf Notu: ", students[i].letter_grade)
            print("------------------------------------")

    choice = input("Baştan başlamak için Y, çıkmak için Q tuşuna basın... ")
    if choice.upper() == "Q":
        break
            