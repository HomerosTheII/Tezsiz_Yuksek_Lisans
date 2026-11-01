global exit_choice

def menu():
    print("Yapmak istediğiniz işlemin numarasını giriniz:\n1- Girilen Sayının Tek mi Çift mi Olduğunu Bulma\n2- Girilen 3 Sayıyı Büyükten Küçüğe Sıralama\n3- Girilen Sayının Asal Sayı Olup Olmadığını Bulma\nÇıkmak için '-1' giriniz.\nSeçiminizi giriniz...")
    while True:
        try:
            choice = int(input())
        except ValueError:
            print("Lütfen geçerli bir değer giriniz.")
            continue


        if choice == 1:
            odd_even_checker()
            break
        elif choice == 2:
            number_sorter()
            break
        elif choice == 3:
            prime_number_checker()
            break
        elif choice == -1:
            global exit_choice
            exit_choice = True
            print("Programdan çıkılıyor...")
            break
        else:
            print("Lütfen geçerli bir sayı giriniz.")
            continue

def odd_even_checker():
    while True:
        try:
            num = int(input("Bir sayı giriniz: "))
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")
            continue
        if num % 2 == 0:
            print(f"{num} sayısı çifttir.")
            return
        else:
            print(f"{num} sayısı tektir.")
            return

def number_sorter():
    sorted_numbers = []
    i = 0
    while i != 3:
        try:
            num = float(input(f"{i+1}. sayıyı giriniz: "))
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")
            continue

        sorted_numbers.append(num)
        i += 1
        sorted_numbers.sort(reverse=True)
    print("Büyükten küçüğe sıralanmış sayılar: ", sorted_numbers)
    return

def prime_number_checker():
    while True:
        try:
            num = int(input("Bir sayı giriniz: "))
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")
            continue

        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    print(f"{num} sayısı asal değildir.")
                    return
            else:
                print(f"{num} sayısı asaldır.")
                return
        else:
            print(f"{num} sayısı asal değildir.")
            return

if __name__ == "__main__":
    while True:
        exit_choice = False
        print("--------------------------")
        menu()
        if exit_choice:
            break
        print("--------------------------")
        action = str(input("Tekrar menüyü görmek için 'Y', çıkmak için 'Q' tuşuna basın..."))
        if action.upper() == 'Q':
            print("Programdan çıkılıyor...")
            break
        elif action.upper() == 'Y':
            continue
        else:
            print("Geçersiz giriş. Lütfen 'Y' veya 'Q' tuşuna basınız.")

