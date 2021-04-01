import numpy as np
import io
from sympy import *
import sympy
import matplotlib.pyplot as plt
import math
s = io.BytesIO(open('input.txt', 'rb').read().replace(b',', b';').replace(b')', b' ').replace(b'(', b' ').replace(b'[',b' ').replace(b']', b' '))
data1 = np.genfromtxt(s, dtype=(float, float,float, float, float, float, float, float, float, float, float, float, float, float, float, float),delimiter=";")
Array=[]
g=9.81
G=6.7*(10**(-11))

x0 = 10
y0 = 10
V0x = 0
V0y = 0
m1 = 100
x1 = 20
y1 = 10
V1x = 0
V1y = 0
m2 = 300
x3 = 15
y3 = 0
V2x = 0
V2y = 0
m3 = 150
T=80

res_x=[]
res_y=[]
res_x2=[]
res_y2=[]
res_x3=[]
res_y3=[]
i=0.001
V00=sqrt((V0x**2)+(V0y**2))
V01=sqrt((V1x**2)+(V1y**2))
V02=sqrt((V2x**2)+(V2y**2))
a0=V00/T
a1=V01/T
a2=V02/T

x1c=0
y1c=0

x2c=0
y2c=0

Bit1=False
Bit2=False
Bit3=False
while i<=T:
    if(Bit1==False):
        x_r_1=x0+V0x*i+(a0*(i**2))/2
        y_r_1=y0+V0y*i+(a0*(i**2))/2
        res_x.append(x_r_1)
        res_y.append(y_r_1)
    
    if(Bit2==False):
        x_r_2=x1+V1x*i+(a1*(i**2))/2
        y_r_2=y1+V1y*i+(a1*(i**2))/2
        res_x2.append(x_r_2)
        res_y2.append(y_r_2)
    if(Bit3==False):
        x_r_3=x3+V2x*i+(a2*(i**2))/2
        y_r_3=y3+V2y*i+(a2*(i**2))/2
        res_x3.append(x_r_3)
        res_y3.append(y_r_3)
    
    if(x_r_1>=x_r_2 and y_r_1>=y_r_2 or x_r_1>=x_r_2 and y_r_1<=y_r_2 or x_r_1<=x_r_2 and y_r_1>=y_r_2 or x_r_1<=x_r_2 and y_r_1<=y_r_2 ):
        Beta=(x_r_1+x_r_2)/(y_r_1+y_r_2)
        Beta=np.arctan(int(Beta))
        V00=V00*np.cos(Beta)
        Bit2==True
        x1c=x_r_1
        y1c=y_r_1
        X1=True
    
    if(x_r_1>=x_r_3 and y_r_1>=y_r_3 or x_r_1>=x_r_3 and y_r_1<=y_r_3 or x_r_1<=x_r_3 and y_r_1>=y_r_3 or x_r_1<=x_r_3 and y_r_1<=y_r_3 ):
        Beta=(x_r_1+x_r_3)/(y_r_1+y_r_3)
        Beta=np.arctan(int(Beta))
        V00=V00*np.cos(Beta)
        Bit3==True
        x1c=x_r_1
        y1c=y_r_1
        X1=True
    
    if(x_r_2>=x_r_3 and y_r_2>=y_r_3 or x_r_2>=x_r_3 and y_r_2<=y_r_3 or x_r_2<=x_r_3 and y_r_2>=y_r_3 or x_r_2<=x_r_3 and y_r_2<=y_r_3 ):
        Beta=(x_r_2+x_r_3)/(y_r_2+y_r_3)
        Beta=np.arctan(int(Beta))
        V01=V01*np.cos(Beta)
        Bit3==True
        x1c=x_r_2
        y1c=y_r_2
        X2=True
        
    if(x_r_2>=x_r_1 and y_r_2>=y_r_1 or x_r_2>=x_r_1 and y_r_2<=y_r_1 or x_r_2<=x_r_1 and y_r_2>=y_r_1 or x_r_2<=x_r_1 and y_r_2<=y_r_1 ):
        Beta=(x_r_2+x_r_1)/(y_r_2+y_r_1)
        Beta=np.arctan(int(Beta))
        V01=V01*np.cos(Beta)
        Bit1==True
        x1c=x_r_2
        y1c=y_r_2
        X2=True
        
    if(x_r_3>=x_r_1 and y_r_3>=y_r_1 or x_r_3>=x_r_1 and y_r_3<=y_r_1 or x_r_3<=x_r_1 and y_r_3>=y_r_1 or x_r_3<=x_r_1 and y_r_3<=y_r_1 ):
        Beta=(x_r_3+x_r_1)/(y_r_3+y_r_1)
        Beta=np.arctan(int(Beta))
        V02=V02*np.cos(Beta)
        Bit3==True
        x1c=x_r_3
        y1c=y_r_3
        X3=True
        
    if(x_r_3>=x_r_2 and y_r_3>=y_r_2 or x_r_3>=x_r_2 and y_r_3<=y_r_2 or x_r_3<=x_r_2 and y_r_3>=y_r_2 or x_r_3<=x_r_2 and y_r_3<=y_r_2 ):
        Beta=(x_r_3+x_r_2)/(y_r_3+y_r_2)
        Beta=np.arctan(int(Beta))
        V02=V02*np.cos(Beta)
        Bit2==True
        x1c=x_r_3
        y1c=y_r_3
        X3=True
    
    if(Bit2==True and Bit1==True or Bit2==True and Bit3==True or Bit3==True and Bit1==True or Bit3==True and Bit2==True or Bit1==True and Bit2==True or Bit1==True and Bit3==True):
        if(X3==True):
            x2c=x_r_3
            y2c=y_r_3
        if(X2==True):
            x2c=x_r_2
            y2c=y_r_2
        if(X1==True):
            x2c=x_r_1
            y2c=y_r_1
        T_k = i
        break
        
        
    i+=0.005
plt.figure(figsize=(15,15))
plt.scatter(res_x,res_y, 5, color='red')
plt.scatter(res_x2,res_y2, 5, color='orange')
plt.scatter(res_x3,res_y3, 5, color='blue')


plt.savefig('1.png')

array12 = np.array(['(' +str(round(x_r_1,2))+'('+str(round(T,2))+')'+', '+str(round(y_r_1,2))+'('+str(round(T,2))+')'+'); '+'('+str(round(V0x,2))+'('+str(round(T,2))+'), '+str(round(V0y,2))+'('+str(round(T,2))+')); '+'(' +str(round(x_r_2,2))+'('+str(round(T,2))+')'+','+str(round(y_r_2,2))+'('+str(round(T,2))+')); '+'('+str(round(V1x,2))+'('+str(round(T,2))+'), '+str(round(V1y,2))+'('+str(round(T,2))+')); '+'(' +str(round(x_r_3,2))+'('+str(round(T,2))+')'+', '+str(round(y_r_3,2))+'('+str(round(T,2))+')); '+'('+str(round(V2x,2))+'('+str(round(T,2))+'), '+str(round(V2y,2))+'('+str(round(T,2))+')); '+'('+str(round(x1c,2))+', '+str(round(y1c,2))+'); ('+str(round(x2c,2))+', '+str(round(y2c,2))+');'])
print(array12)
np.savetxt('output.txt', array12, delimiter='', fmt="%s")#
