data_mahasiswa = {'Ivan': '123456','Rizal': '234567','Amir': '345678','Gatsu': '456789','Ilham': '567890'
                  ,'Agung': '678901','Nabil': '789012','Salwan': '890123','Rido': '901234','Agil': '101234'}

welcome = '''
==================================================================================
================== Selamat Datang Di Virtual Class UNKHAIR =======================
========================= Silahkan Login =========================================
==================================================================================
'''


print (welcome)



username = input ("Masukan Username Anda : ")
password = input ("Masukan Password Anda : ")

if username in data_mahasiswa and data_mahasiswa[username] == password :
    print ("Anda Berhasil Login Ke Virtual Class")
else :
    print ("Login Gagal. Username Atau Password Anda Salah")