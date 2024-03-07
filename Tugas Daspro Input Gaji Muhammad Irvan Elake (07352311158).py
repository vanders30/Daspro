welcome = '''
==========================================================
=======================Selamat Datang=====================
=========================Di Cek Gaji======================
==========================================================
'''
print (welcome)
print ("Silahkan Isi Data Dibawah Ini Untuk Menentukan Gaji Anda")
nama = str (input ("Masukan Nama Anda : "))
hari_kerja = int(input ("Masukan Hari Kerja Anda Dalam 1 Bulan : "))
hari_kerja_perbulan = int (30)
hari_lembur_perhari = int (input ("Masukan Hari Lembur Anda Dalam 1 Bulan : "))
gaji_pokok = 2000000
uang_lembur_perhari = 150000
print ("Nama Karyawan",nama)

total_gaji = int ((hari_kerja/hari_kerja_perbulan)*gaji_pokok+(hari_lembur_perhari*uang_lembur_perhari))
print ("Gaji Anda Bulan Ini Rp. {:,}".format (total_gaji))