import numpy as np
import io
from sympy import *
import sympy
import matplotlib.pyplot as plt
import math
s = io.BytesIO(open('input.txt', 'rb').read().replace(b',', b';').replace(b')', b' ').replace(b'(', b' ').replace(b'[',b' ').replace(b']', b' '))
data1 = np.genfromtxt(s, dtype=(float, float, float, float, float, float),delimiter=";")
Array=[]
R=0.03
r=0.05
m=0.017
miu=0.015
d=0.1
l=2.7
h=1.35
g=9.81

counter=2
count_band_b=0
mo=0
for il in range(0, counter):
    x0 = data1[il][0]
    y0 = data1[il][1]
    V0x = data1[il][2]
    V0y = data1[il][3]
    x2 = data1[il][4]
    y2 = data1[il][5]
#V=V0-at V=0
#T=miu*m*g T=m*a
    a_pred=miu*g
#V0=a_pred*t
    V0=sqrt((V0x**2)+(V0y**2))
    t=V0/a_pred
    t=float(t)
    res_x=[]
    res_y=[]
    res_x2=[]
    res_y2=[]
    i=0.001
    alpha=1
    N1=0
    N2=0
    N3=0
    faul=False
    score=False
    b=1
    im=2
    k=1
    b=0
    z=1
    p=0
    testing=0.03
    buck_y=False
    buck_x=False
    V_dx=0
    V_dy=0
    change=False
    count = 0
    while i<=t:
        x=x0+V0x*i+(a_pred*(i**2))/2
        y=y0+V0y*i+(a_pred*(i**2))/2
        if buck_y==False:
            if y>k*1.35:
                buck_y=True
                change=True
                k+=1
            else:
               y=y-b*1.35
        if buck_y==True:
            y=y*(-1)+k*1.35
            if y<0:
                buck_y=False
                change=True
                k+=1
                b+=2
        if buck_x==False:
            if x>z*2.7:
                buck_x=True
                change=True
                z+=1
            else:
                x=x-p*2.7
        if buck_x==True:
            x=x*(-1)+z*2.7
            if x<=0:
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
            N2+=1
            change=False
        if x>=2.7-(r-R) and y>=1.35-(r-R) or x>=2.7-(r-R) and y<=0+(r-R) or x<=0+(r-R) and y>=1.35-(r-R) or x<=0+(r-R) and y<=0+(r-R) or y<=0+(r-R) and x>=1.35-(r-R) and x<=1.35+(r-R)  or y>=1.35-(r-R) and x>=1.35-(r-R) and x<=1.35+(r-R):
            faul=True
            break
        if(N2>mo):
            v_new=sqrt((V0**2)*0.7)
            t=v_new/a_pred
            mo+=1
        res_x.append(x)
        res_y.append(y)
        if i==0.001:
            x01=x
            y01=y
        i+=0.001
    plt.figure(figsize=(15,8))
    plt.scatter(res_x,res_y, 1)
    plt.scatter(x01, y01, color='red', label='Poczatkowe polozenie bili bialey')
    plt.scatter(x, y, color='green', label='Koncowe polozenie bili bialey')
    plt.scatter(x2,y2, color='orange', label='Polozenie bili')
    plt.hlines(y=1.35, xmin=0.05, xmax=1.3, color='r')
    plt.hlines(y=1.35, xmin=1.4, xmax=2.65, color='r')
    plt.hlines(y=0, xmin=0.05, xmax=1.3, color='r')
    plt.hlines(y=0, xmin=1.4, xmax=2.65, color='r')
    plt.vlines(x=0, ymin=0.05, ymax=1.3, color='r')
    plt.vlines(x=2.7, ymin=0.05, ymax=1.3, color='r')
    pictures=""
    pictures=str(il+1)+'.png'
    plt.savefig(pictures)
    x=str(round(x,1))
    y=str(round(y,1))
    x2=str(round(x2,1))
    y2=str(round(y2,1))
    if faul==False:
        array = np.array(['(' +x+','+y+'); ('+x2+','+y2+'); '+' '+str(N1)+'; '+str(N2)+'; '+str(N3)+';'])
    elif faul==True:
        array = np.array(['(faul); ('+x2+','+y2+'); '+' '+str(N1)+'; '+str(N2)+'; '+str(N3)+';'])
    Array.append(array)
np.savetxt('output.txt', (Array[0], Array[1]), delimiter='', fmt="%s")
