#########################################################################

#PROJECT 1:  ID number last 2 digit verification V3.0

#Contact me  on ;

#instagram : -
#telegram  : -

#########################################################################

#Language :Turkish 

#TC kimlik numarası son 2 hane doğrulama python kodu 


#########################################################################
print("Last 2 number verification V3.0")
print("------------------------------------------------------")
dokuzhane=input("Tc kimlik numaranizin ilk 9 hanesini girin: ")

a =dokuzhane[0]
a=int(a)
b =dokuzhane[1]
b=int(b)
c =dokuzhane[2]
c=int(c)
d =dokuzhane[3]
d=int(d)
e =dokuzhane[4]
e=int(e)
f =dokuzhane[5]
f=int(f)
g =dokuzhane[6]
g=int(g)
h =dokuzhane[7]
h=int(h)
i =dokuzhane[8]
i=int(i)

tekler=(a + c + e + g + i)   
tekler = int(tekler)
Çiftler=(b + d + f + h)       
Çiftler = int(Çiftler)

x =(tekler * 7)
x = int(x)
y =(Çiftler * 9)
y = int(y)

qwe =(x+y)
z =(qwe % 10)
z =int(z)
print("10.rakam=" ,z) 




w=(a + b +c + d + e + f + g + h + i + z)
ğ=(w % 10)
print("11.rakam=" ,ğ)

print("Son 2 rakam=" ,z ,ğ )

print("Tc kimlik no nuz:")
print(a,b,c,d,e,f,g,h,i,z,ğ)
