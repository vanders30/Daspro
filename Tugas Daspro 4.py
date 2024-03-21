x = int (input ("Masukan Bilangan : "))

Bil_oktal = oct(x) [2:]
Bil_hexa = hex(x) [2:]
Bil_desimal = x
Bil_bin = "{:08b}" .format(x)

print ("Bilangan biner :", Bil_bin)
print ("Bilangan oktal dari", x ,"adalah", Bil_oktal )
print ("Bilangan hexadesimal dari",x,"adalah", Bil_hexa)
print ("Bilangan desimal dari",x, "adalah", Bil_desimal)
