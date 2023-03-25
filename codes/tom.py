#%%

#Dans ce modÃ¨le: dx/dt=x{t}*(alpha_1-alpha_2*x{t}-alpha_3*y{t})
#                dy/dt=y{t}*(beta_1-beta_2*y{t}-beta_3*x{t})

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

x0=0.5
y0=0.6

delta_t=10        #delta_t=durÃ©e de l'Ã©tude
N=1000

#On choisit arbitrairement x0 et y0 = densitÃ©s de population initiales
#   x-->proies          y--> prÃ©dateurs
def LV_comp(a1,a3,b3):
                                                      #alpha = paramÃ¨tre propre au modÃ¨le de Lotka Volterra

    a2=a1/10
    T=np.linspace(0,delta_t,N)        # N=arbitraire -> nombre de valeurs dans la liste T
    dt=delta_t/N                #dt=diffÃ©rence temporelle entre chaque valeur calculÃ©e --> sert pour approximer x' et y'
    X=np.zeros(N)
    Y=np.zeros(N)
    X[0]=x0
    Y[0]=y0
    for i in range(N-1):                              #la boucle calcule rÃ©cursivement les diffÃ©rentes valeurs de X et Y

        X[i+1]=X[i]+dt*X[i]*(a1-a2*X[i]-a3*Y[i]/(1+X[i]))                 #on fait l'approximation dx/dt=(x(t+dt)-x(t))/dt
        Y[i+1]=Y[i]+dt*Y[i]*(a1-a2*Y[i]-b3*X[i]/(1+X[i]))                     #idem pour dy/dt


    return X,Y

A1 = plt.axes([0.2, 0.2, 0.65, 0.03])
A1_slider = Slider(
    ax=A1,
    label='a1',
    valmin=0,
    valmax=3,
    valinit=1.01)

A3 = plt.axes([0.2, 0.15, 0.65, 0.03])
A3_slider = Slider(
    ax=A3,
    label='a3',
    valmin=0,
    valmax=1,
    valinit=0.5)

B3 = plt.axes([0.2, 0.1, 0.65, 0.03])
B3_slider = Slider(
    ax=B3,
    label='b3',
    valmin=0,
    valmax=1,
    valinit=0.48)
T=np.linspace(0,delta_t,N)

print(A1_slider.valinit,'/',A3_slider.valinit,'/',B3_slider.valinit)
X,Y=LV_comp(A1_slider.valinit,A3_slider.valinit,B3_slider.valinit)
fig, ax = plt.subplots()
line_1, = plt.plot(T, X, lw=2,color='green')
line_2, = plt.plot(T, Y, lw=2,color='red')

ax.set_xlabel('Temps')
ax.set_ylabel('proies(vert) , prÃ©dateurs(rouge)')

plt.subplots_adjust(bottom=0.5)

def update(val):
    X,Y=LV_comp(A1_slider.val,A3_slider.val,B3_slider.val)
    line_1.set_ydata(X)
    line_2.set_ydata(Y)
    fig.canvas.draw_idle()



A1 = plt.axes([0.2, 0.2, 0.65, 0.03])
A1_slider = Slider(
    ax=A1,
    label='a1',
    valmin=0,
    valmax=3,
    valinit=1.01)

A3 = plt.axes([0.2, 0.15, 0.65, 0.03])
A3_slider = Slider(
    ax=A3,
    label='a3',
    valmin=0,
    valmax=1,
    valinit=0.5)

B3 = plt.axes([0.2, 0.1, 0.65, 0.03])
B3_slider = Slider(
    ax=B3,
    label='b3',
    valmin=0,
    valmax=1,
    valinit=0.48)



A1_slider.on_changed(update)
A3_slider.on_changed(update)
B3_slider.on_changed(update)
    ### On veut a1/a2=10 => on ne met que a1 en variable


plt.show()

# %%
