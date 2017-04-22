import numpy as np
import matplotlib.pyplot as p
import gainData as gainData

fileNameS11VNA='../Cambridge UK results/S-Parameters/HERA diff S11 - 10-300MHz - 100ohm - meas.s1p'
#fileNameS11VNA='../Cambridge UK results/S-Parameters/HERA S-param - single-ended mode - 10-300 MHz - 50 ohm - meas.s2p'
fileNameS11CST='../Cambridge UK results/S-Parameters/HERA diff S11 - 50-250MHz - 100ohm - simu - 47Mc.s1p'
fileNameS11CST_MIT='../cst/SouthAfricaFeedOverDish/SouthAfricaFeedOverDish_noGap_s11'
fileNameTimeTraceCST_MIT='../cst/SouthAfricaFeedOverDish/SouthAfricaFeedOverDish_noGap_terminal_excitation_timetrace.txt'

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
gainData_cst_mit=gainData.GainData(fileNameS11CST_MIT,
                               fileType='CST_S11',
                               fMin=FLOW,fMax=FHIGH,
                               comment='s11 obtained from MIT simulation')
gainData_cst_mit_tt=gainData.GainData(fileNameTimeTraceCST_MIT,
                               fileType='CST_TimeTrace',
                               fMin=FLOW,fMax=FHIGH,
                               comment='time domain from MIT simulation')




print gainData_cst.gainFrequency.shape

p.plot(gainData_vna.fAxis,10.*np.log10(np.abs(gainData_vna.gainFrequency)),color='grey',ls='-',marker='o',label='UK VNA Measurement',markeredgecolor='none')
p.plot(gainData_cst.fAxis,10.*np.log10(np.abs(gainData_cst.gainFrequency)),color='k',ls='--',marker='o',label='UK CST $S_{11}$',markeredgecolor='none')
p.plot(gainData_cst_mit.fAxis,10.*np.log10(np.abs(gainData_cst_mit.gainFrequency)),color='red',ls=':',marker='x',label='MIT CST $S_{11}$',markeredgecolor='none')
p.plot(gainData_cst_mit_tt.fAxis,10.*np.log10(np.abs(gainData_cst_mit_tt.gainFrequency)),color='red',ls=':',marker='o',label='MIT CST Time Trace',markeredgecolor='none')

p.xlim(.1,.2)
p.ylim(-25,0)
p.ylabel('|S$_{11}$|(dB)')
p.xlabel('f (GHz)')
p.legend(loc='best')
#p.show()
p.grid()
p.savefig('../plots/s11_UK_FeedAndDish_MIT_Compare_Frequency.pdf',bbox_inches='tight')
p.close()



#first make original plot comparing s11 of time trace and s11 of vna

p.plot(gainData_vna.tAxis,10.*np.log10(np.abs(gainData_vna.gainDelay)),color='grey',ls='-',marker='o',label='UK VNA Measurement',markeredgecolor='none')
p.plot(gainData_cst.tAxis,10.*np.log10(np.abs(gainData_cst.gainDelay)),color='k',ls='--',marker='o',label='UK CST $S_{11}$',markeredgecolor='none')
p.plot(gainData_cst_mit.tAxis,10.*np.log10(np.abs(gainData_cst_mit.gainDelay)),color='red',ls=':',marker='x',label='MIT CST $S_{11}$',markeredgecolor='none')
p.plot(gainData_cst_mit_tt.tAxis,10.*np.log10(np.abs(gainData_cst_mit_tt.gainDelay)),color='red',ls=':',marker='o',label='MIT CST Time Trace',markeredgecolor='none')



p.xlim(-200,600)
p.ylim(-70,0)
p.ylabel('|$\widetilde{S}_{11}$|(dB)')
p.xlabel('delay (ns)')
p.legend(loc='best')
#p.show()
p.grid()
p.savefig('../plots/s11_UK_FeedAndDish_MIT_Compare_Time.pdf',bbox_inches='tight')
p.close()


p.plot(gainData_vna.tAxis,10.*np.log10(np.abs(gainData_vna.gainDelay)),color='grey',ls='-',marker='o',label='UK VNA Measurement',markeredgecolor='none')
p.plot(gainData_cst.tAxis,10.*np.log10(np.abs(gainData_cst.gainDelay)),color='k',ls='--',marker='o',label='UK CST $S_{11}$',markeredgecolor='none')
p.plot(gainData_cst_mit.tAxis,10.*np.log10(np.abs(gainData_cst_mit.gainDelay)),color='red',ls=':',marker='x',label='MIT CST $S_{11}$',markeredgecolor='none')
p.plot(gainData_cst_mit_tt.tAxis,10.*np.log10(np.abs(gainData_cst_mit_tt.gainDelay)),color='red',ls=':',marker='o',label='MIT CST Time Trace',markeredgecolor='none')



p.xlim(-2000,6000)
p.ylim(-70,0)
p.ylabel('|$\widetilde{S}_{11}$|(dB)')
p.xlabel('delay (ns)')
p.legend(loc='best')
#p.show()
p.grid()
p.savefig('../plots/s11_UK_FeedAndDish_MIT_Compare_Time_largeDelays.pdf',bbox_inches='tight')
p.close()

