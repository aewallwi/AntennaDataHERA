import numpy as np
import matplotlib.pyplot as p
import gainData as gainData

fileNameS11VNA='../Cambridge UK results/S-Parameters/Feed diff S11 - 50-250MHz - 100ohm - meas - para cables.s1p'
fileNameS11CST='../Cambridge UK results/S-Parameters/Feed diff S11 - 50-250MHz - 100ohm - simu - para cables.s1p'

FLOW=0.1
FHIGH=0.2


gainData_cst=gainData.GainData(fileNameS11CST,
                               fileType='S11_S1P',
                               fMin=FLOW,fMax=FHIGH,
                               comment='s11 obtained from Nicolas\'s simulation')
gainData_vna=gainData.GainData(fileNameS11VNA,
                               fileType='S11_S1P',
                               fMin=FLOW,fMax=FHIGH,
                               comment='s11 obtained from Nicolas\'s differential vna measurement')

print gainData_cst.gainFrequency.shape

#first make original plot comparing s11 of time trace and s11 of vna

p.plot(gainData_vna.tAxis,10.*np.log10(np.abs(gainData_vna.gainDelay)),color='grey',ls='-',marker='o',label='VNA Measurement',markeredgecolor='none')
p.plot(gainData_cst.tAxis,10.*np.log10(np.abs(gainData_cst.gainDelay)),color='k',ls='--',marker='o',label='CST $S_{11}$',markeredgecolor='none')
p.xlim(-30,400)
p.ylim(-70,0)
p.ylabel('|$\widetilde{S}_{11}$|(dB)')
p.xlabel('delay (ns)')
p.legend(loc='best')
#p.show()
p.grid()
p.savefig('../plots/s11_UK_FeedOnly_Time.pdf',bbox_inches='tight')
p.close()

p.plot(gainData_vna.fAxis,10.*np.log10(np.abs(gainData_vna.gainFrequency)),color='grey',ls='-',marker='o',label='VNA Measurement',markeredgecolor='none')
p.plot(gainData_cst.fAxis,10.*np.log10(np.abs(gainData_cst.gainFrequency)),color='k',ls='--',marker='o',label='CST $S_{11}$',markeredgecolor='none')
p.xlim(.1,.2)
p.ylim(-25,0)
p.ylabel('|S$_{11}$|(dB)')
p.xlabel('f (GHz)')
p.legend(loc='best')
#p.show()
p.grid()
p.savefig('../plots/s11_UK_FeedOnly_Frequency.pdf',bbox_inches='tight')
p.close()

