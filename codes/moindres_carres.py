

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

Proies=[0.100421053,0.502330827,0.762806682,1.73082747,4.210526345,6.528057497,8.695329918,9.068326398,9.063258971,9.269173431,9.342376957,9.495362874,9.621052192]
Prédateurs=[1.278195485,3.928571425,5.905470521,4.795095477,2.979690409,2.164824870,1.51593945,1.247569314,0.785269564,0.571428568,0.365823675,0.237589156,0.170676693]
T=[0,2,4,6,8,10,12,14,16,18,20,22,24]

plt.plot(T,Proies,'.',color='green')
plt.plot(T,Prédateurs,'.',color='red')


x0=0.100421053
y0=1.278195485

N=1000

a1=1.288
a2=0.136
b1=1.36
b2=0.122

def LVx(temps,a3,b3):
    L=[]
    for k in range(len(temps)):
        T=np.linspace(0,temps[k],N)
        dt=temps[k]/N
        X=np.zeros(N)
        Y=np.zeros(N)
        X[0]=x0
        Y[0]=y0
        for i in range(N-1):

            X[i+1]=X[i]+dt*X[i]*(a1-a2*X[i]-a3*Y[i]/(1+X[i]))
            Y[i+1]=Y[i]+dt*Y[i]*(b1-b2*Y[i]-b3*X[i]/(1+X[i]))

        L.append(X[N-1])

    return np.array(L)        #renvoie la liste des x(t)



def LVy(temps,a3,b3):
    L=[]
    for k in range(len(temps)):
        T=np.linspace(0,temps[k],N)
        dt=temps[k]/N
        X=np.zeros(N)
        Y=np.zeros(N)
        X[0]=x0
        Y[0]=y0
        for i in range(N-1):

            X[i+1]=X[i]+dt*X[i]*(a1-a2*X[i]-a3*Y[i]/(1+X[i]))
            Y[i+1]=Y[i]+dt*Y[i]*(b1-b2*Y[i]-b3*X[i]/(1+X[i]))

        L.append(Y[N-1])

    return np.array(L)        #renvoie la liste des y(t)

temps=np.linspace(0,T[-1],len(T))


popt1 , pcov1 = opt.curve_fit(LVx,temps,Proies,bounds=([0.2, 1.5], [0.3,1.8]))
popt2 , pcov2 = opt.curve_fit(LVy,temps,Prédateurs,bounds=([0.2, 1.5],[0.3, 1.8]))

temps2=np.linspace(0,T[-1],N)
y_fit1=LVx(temps2,* popt1)
y_fit2=LVy(temps2,* popt2)
print(*popt1)
print('et')
print(*popt2)
plt.plot(temps2,y_fit1,color='green')
plt.plot(temps2,y_fit2,color='red')

plt.show()