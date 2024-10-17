import subprocess
import sys, os
import argparse
from subprocess import getstatusoutput

from CRABClient.UserUtilities import config
from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from http.client import HTTPException
#from httplib import HTTPException

config = config()
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.workArea = "crab_projects"

config.JobType.pluginName = 'Analysis'
config.JobType.maxMemoryMB = 3000
config.JobType.allowUndistributedCMSSW = True
#config.Data.outputPrimaryDataset = 'XXTo4J_2017'
config.Data.inputDBS = 'phys03'

config.Data.splitting = 'FileBased'
#config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 1
#NJOBS = 1000
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/dpg_bril/comm_bril/lumi/test/MC_test/HLLbbbb_RAWSIM' #'/store/group/lpcbril/MC_test/ggH4b_RAWSIM_Run3' 
config.Data.publication = True

config.Site.storageSite = 'T2_CH_CERN'
#config.Site.blacklist = ['T3_US_UCR']

from multiprocessing import Process
#config.Site.whitelist = ['T3_US_Colorado', 'T2_US_Florida', 'T3_CH_PSI', 'T2_DE_RWTH']#['T2_CH_CERN', 'T2_US_*', 'T2_IT_Pisa','T2_UK_London_IC','T2_HU_Budapest', 'T2_IT_Rome', 'T2_IT_Bari', 'T2_IT_Legnaro', 'T2_FR_CCIN2P3', 'T2_FR_GRIF_LLR', 'T2_DE_DESY', 'T2_DE_RWTH', 'T2_UK_London_Brunel', 'T2_ES_CIEMAT', 'T2_ES_IFCA', 'T2_BE_IIHE']

#def produce_new_cfg(mass, life, lines):
#    file = open("XXTo4J/XXTo4J_M"+str(mass)+"_CTau"+str(life)+"mm_CP2_GENSIM.py", "w")
#    #width = 0.0197327e-11/float(life)
#    #print width
#    for line in lines:
#        newline = line.replace("AAAA", str(mass)).replace("BBBB", str(life))
#        file.write(newline)
#    file.close()

def submit(config):
    try:
        crabCommand('submit', config = config)
    except HTTPException as hte:
        print("Failed submitting task: %s", (hte.headers))
    except ClientException as cle:
        print("Failed submitting task: %s", (cle))


def sub_crab_job(mass, life):
    
    datasetname = getstatusoutput("das_client --query='dataset=/HToLL_Run3/*-HToLLTo4b_Powheg_M"+str(mass)+"_"+str(life)+"mm_CP5_13p6TeV_HPt100_GENSIM_Run2024_ext*/USER instance=prod/phys03'")[1].split("\n")[0]
    config.General.requestName = 'HToLLTo4b_Powheg_M'+str(mass)+'_'+str(life)+'mm_CP5_13p6TeV_HPt100_RAWSIM_Run2024_ext'
    config.JobType.psetName = 'TSG_RAWSIM.py' 
    config.Data.outputDatasetTag = 'HToLLTo4b_Powheg_M'+str(mass)+'_'+str(life)+'mm_CP5_13p6TeV_HPt100_RAWSIM_Run2024_ext'
    config.Data.inputDataset = datasetname 
    print("submit: Mass:",mass, "life:", life)
    print(datasetname)
    #submit(config)
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()


#infile = open('XXTo4J_MAAAA_CTauBBBBmm_TuneCP2_13TeV_pythia8_GENSIM.py')
#lines = infile.readlines()

for m in [15, 30, 40]:#[50, 60, 70, 80, 90, 100, 150, 200, 300, 400, 700, 1000, 1500, 3000]: 
    for l in [1, 10, 100, 1000]:#[3, 30, 300, 3000]:
#for m in [1000]:
#    for l in [1]: 
        #produce_new_cfg(m, l, lines)
        sub_crab_job(m, l)
