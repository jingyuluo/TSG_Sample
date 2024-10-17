import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_2023_cff import Run3_2023

process = cms.Process('HLT',Run3_2023)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.Run3_2023_LHC_Simulation_12p5h_9h_hybrid2p23_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_2023v12_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('file:/eos/cms/store/group/dpg_bril/comm_bril/lumi/test/MC_test/HLLbbbb_GENSIM/HToLL_Run3/HToLLTo4b_Powheg_M40_10mm_CP5_13p6TeV_HPt100_GENSIM_Run2024/240603_192447/0000/TSG-Run3Winter24wmLHEGS-00035_70.root'),
    inputCommands = cms.untracked.vstring(
        'keep *',
        'drop *_genParticles_*_*',
        'drop *_genParticlesForJets_*_*',
        'drop *_kt4GenJets_*_*',
        'drop *_kt6GenJets_*_*',
        'drop *_iterativeCone5GenJets_*_*',
        'drop *_ak4GenJets_*_*',
        'drop *_ak7GenJets_*_*',
        'drop *_ak8GenJets_*_*',
        'drop *_ak4GenJetsNoNu_*_*',
        'drop *_ak8GenJetsNoNu_*_*',
        'drop *_genCandidatesForMET_*_*',
        'drop *_genParticlesForMETAllVisible_*_*',
        'drop *_genMetCalo_*_*',
        'drop *_genMetCaloAndNonPrompt_*_*',
        'drop *_genMetTrue_*_*',
        'drop *_genMetIC5GenJs_*_*'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--python_filename nevts:168'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:TSG-Run3Winter24Digi-00012.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/000c9fac-9641-4f89-a3eb-e6ff6ed4480d.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/0017db1e-da6f-4fa4-8b9b-30a406e2474d.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/00bcd062-f0ac-487d-9859-ae628a788512.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/00f36c7f-a451-4129-b5cd-db45a285c8ed.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/01a2380f-5e0e-4914-a011-d4eace35ef33.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/01ed0f5a-7128-4906-9e8c-b343e7b6fa93.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/020b0120-983d-43dd-a724-b6eae2d8984f.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/023bf415-d57e-448d-8a1a-5197f79b862d.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/0269fc50-0d4f-4de2-a019-767db5ab38f7.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/02747c68-6b9a-4025-80ed-fc29a1c51def.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/02aa7851-5147-40c6-b1ef-72eb311be15c.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/03a319c3-3cc8-4a7a-ba9a-2749b813ff56.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/040b7b67-1352-44bd-a4f9-7b4eba011758.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/0492359c-0b60-41d0-ad8b-710f7fd2a728.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/04a11c21-3cbd-4eee-824c-8d0bb48ec4bc.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/04c1c7bf-da8a-4730-9bac-75ff0eb8e09e.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/056ecaa4-093c-4e17-94e7-0098c3a0d0a4.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/05854e16-1247-4520-84fc-fb64350f4291.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/05e9ae19-1b6d-4a4b-bdbb-738cbd1a0d77.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/06158515-984d-4b11-aa69-3cdf63c88e8e.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/063b9e8d-99a1-42fe-8133-25c846de7149.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/069ba98b-1aa3-46fc-bb18-4ec7eb4e8d03.root', '/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60000/06d88951-0434-4805-bc8c-ffce3d6ae47e.root']) 
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '133X_mcRun3_2024_realistic_v8', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
# process.schedule imported from cff in HLTrigger.Configuration
process.schedule.insert(0, process.digitisation_step)
process.schedule.insert(1, process.L1simulation_step)
process.schedule.insert(2, process.digi2raw_step)
process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads = 1
process.options.numberOfStreams = 0

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
