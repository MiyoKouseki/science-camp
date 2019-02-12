import numpy as np
import matplotlib.pyplot as plt

if True:
    data = np.loadtxt('FeedBack.csv',delimiter=',',comments='%')
    f = data[:,0]
    ch1 = data[:,1]
    ch2 = data[:,2]
    plt.loglog(f,ch1,'r-',label='Feedback',linewidth=1)
    plt.loglog(f,ch2,'k-',label='Not connected',linewidth=1)
    plt.grid(b=True, which='major', color='gray', linestyle='-')
    plt.grid(b=True, which='minor', color='gray', linestyle=':')
    plt.xlim(1,2000)
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude [V/rtHz]')
    plt.legend()
    plt.savefig('ASD_FeedBack.png')
    plt.close()
    

if True:
    data = np.loadtxt('OpenLoop.csv',delimiter=',',comments='%')
    f = data[:,0]
    ch1_mag = data[:,1] # dB
    ch1_phase = data[:,2] # deg
    ch2_mag = data[:,3] # dB
    ch2_phase = data[:,4] # deg
    tf12_mag = data[:,5] # dB
    tf12_phase = data[:,6] # deg 
    fig, (ax0,ax1) = plt.subplots(2,1,sharex=True)    
    ax0.semilogx(f,tf12_mag,'k-',label='Openloop',linewidth=1)
    ax0.grid(b=True, which='major', color='gray', linestyle='-')
    ax0.grid(b=True, which='minor', color='gray', linestyle=':')
    ax0.set_xlim(1e0,3e3)
    ax0.set_ylim(-25,50)
    ax0.set_ylabel('Magnitude')
    ax0.legend()    
    ax1.semilogx(f,tf12_phase,'k-',label='Openloop',linewidth=1)    
    ax1.grid(b=True, which='major', color='gray', linestyle='-')
    ax1.grid(b=True, which='minor', color='gray', linestyle=':')
    ax1.set_ylabel('Tf12_phase [deg]')    
    ax1.set_xlim(1e0,3e3)
    ax1.set_xlabel('Frequency [Hz]')
    ax1.set_yticks(np.arange(-180,181,90))
    ax1.set_ylim(-180,180)
    ax1.legend()
    plt.savefig('BODE_OpenLoop.png')
    plt.close()

