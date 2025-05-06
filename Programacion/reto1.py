#1 Realiza las siguientes operaciones siguiendo las reglas de precedencia
if __name__=="__main__": 
    w = 3
    x = 5
    y = 7
    z = 9
    a = x =z
    print(f"/nx es igual a z",a )
    b = w >= y
    print(f"/nw >= y= ",b )
    c = w == x < y < z
    print (f'w = x < y < z',c)
    d= (w == x ) == ( y > z )
    print(f'( w = x ) == ( y > z )',d)
    e= x != ( w < z < y ) == 1
    print(f'x != ( w < z < y ) == 1',e)
    f = w * y >= w * z
    print(f' w * y >= w * z',f)
    g=y + w* z / w!= z + w - y * x
    print(f'y + w* z / w!= z + w - y * x',g)
    h=( y + w ) * z / w == y * x - 20 / 4
    print(f'( y + w ) * z / w == y * x - 20 / 4',h)
    i=w * y >= w * z == ( y + w ) * z > 0
    print(f'w * y >= w * z == ( y + w ) * z > 0',i)
    j= x > z * (  w+ y )!= w <= x
    print(f'x > z * (  w+ y )!= w <= x',j)
   
#2 Escriba las condiciones lógicas correspondientes utilizando los símbolos adecuados.
aa= (x>y)and(f<2)or(g==4)
print(f'El  reultado es: ',aa)
bb= x<0<(3*a)
print(f'El  reultado es: ',bb)
p=20
cc = (p>y) or (p>x) or (p>z)
print(f'El  reultado es: ',cc)
dd= a!= b and c !=g and c !=h and c!=j
print(f'El  reultado es: ',dd)
ee= 1<=a<=8 and (b<1 or b>8)
print(f'El  reultado es: ',ee)
ff= (a and b >=0) or (a and b >=0 )
print(f'El  reultado es: ',ff)
gg= a == 0 or b==0
print(f'El  reultado es: ',gg) 
