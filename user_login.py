print("""
*************************

Kullanıcı Girişi Programına Hoşgeldiniz

*************************
""")

sys_istifadeci_adi = "akbar"
sys_parol = "123456"

istifadeci_adi = input("Istifaedci adi:")
parol = input("Parol:")

if (istifadeci_adi == sys_istifadeci_adi and sys_parol != parol):
    print("Incorrect password")
elif (istifadeci_adi != sys_istifadeci_adi and sys_parol == parol):
    print("Incorrect username")
elif (istifadeci_adi != sys_istifadeci_adi and parol != sys_parol):
    print("Incorrect username and password")
else: 
    print("Succesfully logged into the system")