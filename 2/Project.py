import numpy as np
import io
from sympy import *
import sympy
import matplotlib.pyplot as plt
import math

s = io.BytesIO(open('input.txt', 'rb').read().replace(b',', b';').replace(b')', b' ').replace(b'(', b' ').replace(b'[',b' ').replace(b']', b' '))
data1 = np.genfromtxt(s, dtype=(float, float, float, float, float, float, float),delimiter=";")
Array=[]
n = 7
k = 6
result_0 = []
f=1
for i in range(0, k):
    x0 = data1[i][0]
    y0 = data1[i][1]
    m = data1[i][2]
    r = data1[i][3]
    miu = data1[i][4]
    V0x = data1[i][5]
    V0y = data1[i][6]
    
    g = 10

    #V=V0-at V=0
    #T=miu*m*g T=m*a

    a=miu*g

    #V0=a*t

    V0=sqrt((V0x**2)+(V0y**2))
    t=V0/a
    t=float(t)
    res_x=[]
    res_y=[]
    i=0.001
    alpha=1
    
    a=2
    b=1
    im=2
    k=1
    b=0
    z=1
    p=0
    buck_y=False
    buck_x=False
    x_T=True
    change=False
    Out="Out"
    res_x_y=[]
    res_od=[]
    count = 0
    while i<=t:
        x=x0+V0x*i+(a*(i**2))/2
        y=y0+V0y*i+(a*(i**2))/2
        if i>0.05:
            x_T=False
        if buck_y==False:
            if y>=k*40:
                
                buck_y=True
                change=True
                k+=1
                
            else:
               y=y-b*40
               
        if buck_y==True:
            y=y*(-1)+k*40
            
            if y<=0.11:
                buck_y=False
                change=True

                k+=1
                b+=2
        if buck_x==False:
            if x>=z*60:
                buck_x=True
                change=True
     
                z+=1
            else:
                x=x-p*60
        if buck_x==True:
            x=x*(-1)+z*60
            if x<=0.11:
                buck_x=False
                change=True
    
                z+=1
                p+=2

        if change==True:
            if x<0:
                x=x*-1
            if y<0:
                y=y*-1
            x=round(x, 1)
            y=round(y, 1)
            res_od.append(x)
            res_od.append(y)
            count+=1
            
            change=False
        if x>=59.9 and y-r>=19.5 and x>=59.9 and y+r<=20.5 or x<=0.1 and y-r>=19.5 and x<=0.1 and y+r<=20.5 and x_T==False:
            
            res_x_y.append(Out)
            break
        
                
        
            
        
            
        
             
        res_x.append(x)
        res_y.append(y)
        i+=0.001
    if not res_x_y:
        res_x_y.append(round(x,1))
        res_x_y.append(round(y,1))
        
    X_Y= str(res_x_y)
    X_Y=X_Y.replace("[", "")
    X_Y=X_Y.replace("]", "")
    
    z=""
    l=0
    while l<len(res_od):
        if l%2==0:
            z+="("+str(res_od[l])+", "
        if l%2!=0:
            z+=str(res_od[l])+"); "
    
        l+=1
    
    array = np.array(['(' + X_Y+'); '+str(round(t,2))+'; ' +z])
    Array.append(array)
    
    
    plt.figure(figsize=(15,15))
    plt.scatter(res_x,res_y, 1, label='Trajektoria ruchu kr????ka')
    
    if len(X_Y)>5: 
        plt.scatter(x, y, color='orange', label='Po??o??enie ko??cowe kr????ka')
    else: 
        plt.scatter(x, y, color='green', label='Po??o??enie ko??cowe kr????ka przed out')
    plt.scatter(x0, y0, color='y')
    
    plt.hlines(y=0, xmin=0, xmax=60, color='r')
    plt.vlines(x=0, ymin=0, ymax=19.5, color='r')
    plt.vlines(x=0, ymin=20.5, ymax=40, color='r')
    plt.hlines(y=40, xmin=0, xmax=60, color='r')
    plt.vlines(x=60, ymin=0, ymax=19.5, color='r')
    plt.vlines(x=60, ymin=20.5, ymax=40, color='r')
    a=""
    a=str(f)+'.png'
    
    f+=1
    plt.savefig(a)
np.savetxt('output.txt', (Array[0], Array[1], Array[2], Array[3], Array[4], Array[5]), delimiter='', fmt="%s")#