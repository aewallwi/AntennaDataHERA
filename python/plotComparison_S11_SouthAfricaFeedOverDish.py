import numpy as n
import matplotlib.pyplot as p
import gainData as gainData

fileNameTimeTraceCST='../cst/SouthAfricaFeedOverDish/SouthAfricaFeedOverDish_TerminalExcitation_timetrace.txt'
fileNameS11CSV='../reflectometry/CambridgeMeasurements/FeedOverDish/HERA_dish_LB_S11_measured.csv'
fileNameS11CST='../cst/SouthAfricaFeedOverDish/SouthAfricaFeedOverDish_S11'

FLOW=0.1
FHIGH=0.2


gainData_timeTrace=gainData.GainData(fileNameTimeTraceCST,
                                     fileType='CST_TimeTrace',
                                     fMin=FLOW,fMax=FHIGH,
                                     comment='s11 derived from cst time domain data')
gainData_cst=gainData.GainData(fileNameS11CST,
                               fileType='CST_S11',
                               fMin=FLOW,fMax=FHIGH,
                               comment='s11 obtained directly from cst')
gainData_vna=gainData.GainData(fileNameS11CSV,
                               fileType='S11_CSV',
                               fMin=FLOW,fMax=FHIGH,
                               comment='s11 obtained from richs vna measurement')

print gainData_cst.gainFrequency.shape

#first make original plot comparing s11 of time trace and s11 of vna

p.plot(gainData_vna.tAxis,10.*n.log10(n.abs(gainData_vna.gainDelay)),color='grey',ls='-',marker='o',label='VNA Measurement',markeredgecolor='none')
p.plot(gainData_timeTrace.tAxis,10.*n.log10(n.abs(gainData_timeTrace.gainDelay)),color='k',ls='-',marker='o',label='CST timetrace',markeredgecolor='none')
p.plot(gainData_cst.tAxis,10.*n.log10(n.abs(gainData_cst.gainDelay)),color='k',ls='--',marker='o',label='CST $S_{11}$',markeredgecolor='none')
p.xlim(-30,400)
p.ylim(-70,0)
p.ylabel('|$\widetilde{S}_{11}$|(dB)')
p.xlabel('delay (ns)')
p.legend(loc='best')
#p.show()
p.grid()
p.savefig('../plots/s11_CST_vs_Reflectometry_SouthAfricaFeedOverDish_Delay.pdf',bbox_inches='tight')
p.close()

p.plot(gainData_vna.fAxis,10.*n.log10(n.abs(gainData_vna.gainFrequency)),color='grey',ls='-',marker='o',label='VNA Measurement',markeredgecolor='none')
p.plot(gainData_timeTrace.fAxis,10.*n.log10(n.abs(gainData_timeTrace.gainFrequency)),color='k',ls='-',marker='o',label='CST timetrace',markeredgecolor='none')
p.plot(gainData_cst.fAxis,10.*n.log10(n.abs(gainData_cst.gainFrequency)),color='k',ls='--',marker='o',label='CST $S_{11}$',markeredgecolor='none')
p.xlim(.1,.2)
p.ylim(-15,0)
p.ylabel('|S$_{11}$|(dB)')
p.xlabel('f (GHz)')
p.legend(loc='best')
#p.show()
p.grid()
p.savefig('../plots/s11_CST_vs_Reflectometry_SouthAfricaFeedOverDish_Frequency.pdf',bbox_inches='tight')
p.close()

