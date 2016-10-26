#************************************************************
#library for reading cst and VNA data files
#************************************************************
import numpy as n
import healpy as hp



class metaData():
    def __init__(self):
        self.device=''
        self.date=''
        self.dtype=''
        self.comment=''
        self.date=''
        self.datarange=''

#Read HP VNA data used in Greenbank measurements
def readVNAHP(filename,comment=''):
    dataFile=open(filename)
    dataLines=dataFile.readlines()
    FLOW=float(dataLines[7].split()[1]);FHIGH=float(dataLines[7].split()[2]);NDATA=int(dataLines[7].split()[3])
    data=n.loadtxt(filename,skiprows=9,delimiter=',')
    device=dataLines[1]
    dtype=dataLines[4].split()[1]
    meta=metaData(device=device,dtype=['FREQ',dtype],datarange=[FLOW,FHIGH,NDATA],comment=comment)
    fAxis=n.arange(NDATA)*(FHIGH-FLOW)+FLOW
    return fAxis,data[:,0]+1j*data[:,1],meta
    
#Read CST time trace file
def readCSTTimeTrace(filename,comment=''):
    dataFile=open(filename)
    dataLines=dataFile.readlines()
    inputTrace=[]
    outputTrace1=[]
    outputTrace2=[]
    lNum=0
    while lNum <len(dataLines):
        if('o1' in dataLines[lNum]):
            thisTrace=outputTrace1
            lNum+=2
        elif('o2' in dataLines[lNum]):
            thisTrace=outputTrace2
            lNum+=2
        elif('i1' in dataLines[lNum]):
            thisTrace=inputTrace
            lNum+=2
            dtype='Terminal Excitation'
        elif('Plane wave' in dataLines[lNum]):
            thisTrace=inputTrace
            lNum+=2
            dtype='PlaneWave Excitation'
        else:
            entry=dataLines[lNum].split()
            thisTrace.append([float(entry[0]),float(entry[1])])
            lNum+=1
    inputTrace=n.array(inputTrace)
    outputTrace1=n.array(outputTrace1)
    outputTrace2=n.array(outputTrace2)
    meta=(device='CST',dtype=['Time',dtype],datarange=[inputTrace[:,0].min(),inputTrace[:,0].max(),len(inputTrace[:,0])],comment=comment)
    return [inputTrace,outputTrace1,outputTrace2],meta
    
def readCSTS11(filename,comment=''):
    amp=n.loadtxt(filename+'_amp.txt',skiprows=2)
    pha=n.loadtxt(filename+'_pha.txt',skiprows=2)
    

FILETYPES=['CST','VNAHP']
class gainData():
    def __init__(self):
        
        
    
