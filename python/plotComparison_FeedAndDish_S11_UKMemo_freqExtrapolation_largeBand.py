import numpy as np
import matplotlib.pyplot as p
import gainData as gainData

fileNameS11VNA='../Cambridge UK results/S-Parameters/HERA diff S11 - 10-300MHz - 100ohm - meas.s1p'
#fileNameS11VNA='../Cambridge UK results/S-Parameters/HERA S-param - single-ended mode - 10-300 MHz - 50 ohm - meas.s2p'
fileNameS11CST='../Cambridge UK results/S-Parameters/HERA diff S11 - 50-250MHz - 100ohm - simu - 47Mc.s1p'
fileNameS11CST_MIT='../cst/SouthAfricaFeedOverDish/SouthAfricaFeedOverDish_noGap_s11'
fileNameTimeTraceCST_MIT='../cst/SouthAfricaFeedOverDish/SouthAfricaFeedOverDish_noGap_terminal_excitation_timetrace.txt'

FLOW=0.0
FHIGH=0.25

gainData_cst_blackman=gainData.GainData(fileNameS11CST,
                                        fileType='S11_S1P',
                                        fMin=FLOW,
                                        fMax=FHIGH,
                                        comment='cst blackman window',
                                        extrapolateBand=True)
gainData_cst_tophat=gainData.GainData(fileNameS11CST,
                                      fileType='S11_S1P',
                                      fMin=FLOW,
                                      fMax=FHIGH,
                                      windowFunction='tophat',
                                      comment='cst tophat window',
                                      extrapolateBand=True)
gainData_vna_blackman=gainData.GainData(fileNameS11VNA,
                                        fileType='S11_S1P',
                                        fMin=FLOW,fMax=FHIGH,
                                        comment='vna blackman window',
                                        extrapolateBand=True)
gainData_vna_tophat=gainData.GainData(fileNameS11VNA,
                                      fileType='S11_S1P',
                                      fMin=FLOW,fMax=FHIGH,
                                      windowFunction='tophat',
                                      comment='vna tophat window',
                                      extrapolateBand=True)
#gainData_cst_mit=gainData.GainData(fileNameS11CST_MIT,
#                               fileType='CST_S11',
#                               fMin=FLOW,fMax=FHIGH,
#                               comment='s11 obtained from MIT simulation')
#gainData_cst_mit_tt=gainData.GainData(fileNameTimeTraceCST_MIT,
#                               fileType='CST_TimeTrace',
#                               fMin=FLOW,fMax=FHIGH,
#                               comment='time domain from MIT simulation')




print gainData_cst_tophat.gainFrequency.shape

p.plot(gainData_vna_tophat.fAxis,10.*np.log10(np.abs(gainData_vna_tophat.gainFrequency)),color='red',ls='--',label='VNA tophat',markeredgecolor='none')
p.plot(gainData_cst_tophat.fAxis,10.*np.log10(np.abs(gainData_cst_tophat.gainFrequency)),color='k',ls='-',label='CST tophat$',markeredgecolor='none')
p.plot(gainData_cst_blackman.fAxis,10.*np.log10(np.abs(gainData_cst_blackman.gainFrequency)),color='k',ls='-',label='CST blackman',markeredgecolor='none')
p.plot(gainData_vna_blackman.fAxis,10.*np.log10(np.abs(gainData_vna_blackman.gainFrequency)),color='red',ls='--',label='VNA blackman',markeredgecolor='none')

p.xlim(.0,.3)
p.ylim(-25,0)
p.ylabel('|S$_{11}$|(dB)')
p.xlabel('f (GHz)')
p.legend(loc='best')
#p.show()
p.grid()
p.savefig('../plots/s11_UK_FeedAndDish_largeBand_Compare_Frequency_bhVth.pdf',bbox_inches='tight')
p.close()



#first make original plot comparing s11 of time trace and s11 of vna

p.plot(gainData_vna_tophat.tAxis,10.*np.log10(np.abs(gainData_vna_tophat.gainDelay)),color='red',ls='--',label='VNA tophat',markeredgecolor='none')
p.plot(gainData_cst_tophat.tAxis,10.*np.log10(np.abs(gainData_cst_tophat.gainDelay)),color='k',ls='-',label='CST tophat',markeredgecolor='none')
p.plot(gainData_cst_blackman.tAxis,10.*np.log10(np.abs(gainData_cst_blackman.gainDelay)),color='k',ls='-',label='CST blackman',markeredgecolor='none')
p.plot(gainData_vna_blackman.tAxis,10.*np.log10(np.abs(gainData_vna_blackman.gainDelay)),color='red',ls='--',label='VNA blackman',markeredgecolor='none')



p.xlim(-200,600)
p.ylim(-70,0)
p.ylabel('|$\widetilde{S}_{11}$|(dB)')
p.xlabel('delay (ns)')
p.legend(loc='best')
#p.show()
p.grid()
p.savefig('../plots/s11_UK_FeedAndDish_largeBand_Compare_Time_bhVth.pdf',bbox_inches='tight')
p.close()


p.plot(gainData_vna_tophat.tAxis,10.*np.log10(np.abs(gainData_vna_tophat.gainDelay)),color='red',ls='-',label='VNA tophat',markeredgecolor='none')
p.plot(gainData_cst_tophat.tAxis,10.*np.log10(np.abs(gainData_cst_tophat.gainDelay)),color='k',ls='-',label='CST tophat',markeredgecolor='none')
p.plot(gainData_cst_blackman.tAxis,10.*np.log10(np.abs(gainData_cst_blackman.gainDelay)),color='k',ls='--',label='CST blackman',markeredgecolor='none')
p.plot(gainData_vna_blackman.tAxis,10.*np.log10(np.abs(gainData_vna_blackman.gainDelay)),color='red',ls='--',label='VNA blackman',markeredgecolor='none')



p.xlim(-2000,6000)
p.ylim(-70,0)
p.ylabel('|$\widetilde{S}_{11}$|(dB)')
p.xlabel('delay (ns)')
p.legend(loc='best')
#p.show()
p.grid()
p.savefig('../plots/s11_UK_FeedAndDish_largeBand_Compare_Time_largeDelays_bhVth.pdf',bbox_inches='tight')
p.close()

p.plot(gainData_vna_tophat.tAxis,20.*np.log10(np.abs(gainData_vna_tophat.gainDelay)),color='red',ls='-',label='VNA tophat',markeredgecolor='none')
p.plot(gainData_cst_tophat.tAxis,20.*np.log10(np.abs(gainData_cst_tophat.gainDelay)),color='k',ls='-',label='CST tophat',markeredgecolor='none')
p.xlim(0,400)
p.ylim(-70,0)
p.ylabel('$|\widetilde{S}_{11}|^2$(dB)')
p.xlabel('delay (ns)')
p.legend(loc='best')
#p.show()
p.grid()
p.gcf().set_size_inches(12,6)
p.savefig('../plots/s11_UK_FeedAndDish_largeBand_Compare_Time_largeDelays_Squared_bhVth.pdf',bbox_inches='tight')
p.close()
