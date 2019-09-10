# LATIHAN 1
# Initialisasi Variabel dan Tipe Data
a = 1
b = 4.5
c = 'kata'
d = ['usia',30]
e = ('usia',30)
f = {'usia' : 30, 'pekerjaan' : 'mahasiswa'}
# Contoh Output Program
print('Latihan 1 \n')
print (type(a)) # tipe data integer
print ("\tNilai bilangan bulat a adalah", a,"\n")# easy style
print (type(b)) # tipe data float
print ("\tNilai bilangan decimal b adalah %f" %(b),'\n') # old style 
print (type(c)) # tipe data string
print ("\tKata dari c adalah {}".format(c),"\n") # new style
print (type(d)) # tipe data List
print ("\tDaftar dari d adalah ", d,"\n")
print (type(e)) # tipe data Tuple
print ("\tDaftar tetap dari e adalah ", e,"\n")
print (type(f)) # tipe data Dictionary
print ("\tKomponen dari f adalah ", f,"\n")