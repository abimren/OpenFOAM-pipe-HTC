"""
Plots OpenFOAM residuals. Use after processing OpenFOAM log file:
foamLog log.solver

author: abdurrahman.imren 
"""
import numpy as np
import matplotlib.pyplot as plt
# Set Runtime Configuration in family groups
plt.rc('figure',autolayout=True,figsize=(8,6))
#plt.rc('font',family='Arial',size=20)
plt.rc('font',size=18)
# *********************************************************
file='../logs/Ux_0'
Ux_0=np.loadtxt(file,delimiter='s')
file='../logs/UxFinalRes_0'
UxFinalRes_0=np.loadtxt(file,delimiter='s')
file='../logs/Uy_0'
Uy_0=np.loadtxt(file,delimiter='s')
file='../logs/UyFinalRes_0'
UyFinalRes_0=np.loadtxt(file,delimiter='s')
file='../logs/Uz_0'
Uz_0=np.loadtxt(file,delimiter='s')
file='../logs/UzFinalRes_0'
UzFinalRes_0=np.loadtxt(file,delimiter='s')
file='../logs/p_0'
p_0=np.loadtxt(file,delimiter='s')
file='../logs/pFinalRes_0'
pFinalRes_0=np.loadtxt(file,delimiter='s')

#print(file,data.shape,data[0])
plt.plot(Ux_0[:,0],Ux_0[:,1],'-r',lw=2,label='Ux_0')
plt.plot(UxFinalRes_0[:,0],UxFinalRes_0[:,1],'--r',lw=2,label='UxFinalRes_0')
plt.plot(Uy_0[:,0],Uy_0[:,1],'-g',lw=2,label='Uy_0')
plt.plot(UyFinalRes_0[:,0],UyFinalRes_0[:,1],'--g',lw=2,label='UyFinalRes_0')
plt.plot(Uz_0[:,0],Uz_0[:,1],'-b',lw=2,label='Uz_0')
plt.plot(UzFinalRes_0[:,0],UzFinalRes_0[:,1],'--b',lw=2,label='UzFinalRes_0')
plt.plot(p_0[:,0],p_0[:,1],'-k',lw=2,label='p_0')
plt.plot(pFinalRes_0[:,0],pFinalRes_0[:,1],'--k',lw=2,label='pFinalRes_0')
plt.ylabel('Residuals')
plt.xlabel('Iteration')
plt.legend(fontsize=12,loc='lower center',bbox_to_anchor=(0.5,1.05),ncol=4,fancybox=True,shadow=True)
# center left , upper center
plt.yscale('log')
#plt.ylim((0,300))
#plt.ylim(bottom=-1000) 
#plt.xlim(right=0.2)
plt.grid(ls='--')
plt.savefig(f"residuals_logs.png")
plt.show()
# line  '-',':','--','-.'
# color r,g,b,c,m,y,k,w
# marker o,*,v,^,<,>,s,D,  d,x,X,+,P,p,h,1,2,3,4,|
# marker color e.g., mfc="blue", mfc="none"
# format: 'marker line color' e.g., 'D-k' 
#plt.plot(results[:,0],results[:,1],'s-.',label='DVODE',ms=10,mfc="none",markevery=5)