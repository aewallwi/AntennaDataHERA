import numpy as n
import matplotlib.pyplot as p
import gainData as gainData

fileNameTimeTraceCST='../cst/TallCylinderGapOverDish/TallCylinderGapOverDish_TerminalExcitation_timetrace.txt'
fileNameS11VNA='../reflectometry/RichBradley_GreenBank/TallCylinderGapOverDish_S11_Greenbank_RichBradley.d1'
fileNameS11CST='../cst/TallCylinderGapOverDish/TallCylinderGapOverDish_S11'

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
gainData_vna=gainData.GainData(fileNameS11VNA,
                               fileType='VNAHP_S11',
                               fMin=FLOW,fMax=FHIGH,
                               comment='s11 obtained from richs vna measurement')

print gainData_vna.tAxis
print gainData_timeTrace.tAxis
print gainData_timeTrace.gainDelay

#first make original plot comparing s11 of time trace and s11 of vna

p.plot(gainData_vna.tAxis,10.*n.log10(n.abs(gainData_vna.gainDelay)),color='grey',ls='-',marker='o')
p.plot(gainData_timeTrace.tAxis,10.*n.log10(n.abs(gainData_timeTrace.gainDelay)),color='k',ls='-',marker='o')
p.xlim(-30,400)
p.ylim(-50,0)
p.show()
