print("""
****************************
Os Module
****************************
""")
import os
from datetime import datetime
# os.chdir("C:/Users/user/Desktop")

# for i in os.listdir():
#     print(i)


# print(os.getcwd())

# os.mkdir("Deneme1")

# os.makedirs("Denem2/Deneme3")

# os.removedirs("Denem2/Deneme3")

# os.rmdir("Deneme1")

# os.rename("test.txt","test2.txt")

# print(os.stat("test2.txt"))

# print(os.stat("test2.txt").st_mtime)

# print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime))

# print(os.walk("C:/Users/user/Desktop"))


for klasör_yolu, klasör_isimleri, dosya_isimler in os.walk("C:/Users/user/Desktop"):
   print("Klasör Yolu:", klasör_yolu)
   print("Klasör Isimleri:", klasör_isimleri)
   print("Dosya Isimler:", dosya_isimler)
   print("********************************")


for klasör_yolu, klasör_isimleri, dosya_isimler in os.walk("C:/Users/user/Desktop"):
    for  i in dosya_isimler:
        if (i.endswith(".jpg")):
            print(i)
