from libPython.tnpClassUtils import tnpSample

### qll stat
#eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
#eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
#eosDirREC = 'eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
#eosWinter17 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/Moriond17_v1/'
eosMoriond18 = '/eos/cms/store/group/phys_egamma/swmukher/ntuple_2017_v2/'
eos_run3_commissioning_data2022B = "/eos/user/f/fmausolf/TnP_Ntuplizer_test/"
eos_run3_commissioning_data2022C = "/eos/cms/store/group/phys_egamma/ec/fmausolf/EGM_comm/ntuple_Run3_data_call_10_data/data/EGamma/crab_Egamma2022C/220812_095635/0000/"
eos_run3_commissioning_MC = "/eos/cms/store/group/phys_egamma/ec/fmausolf/EGM_comm/TnP_DY_NLO_MC_Run3Winter22/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8/TnP_DY_NLO_MC_Run3Winter22/220812_091911/0000/"

Moriond18_94X = {
    ### MiniAOD TnP for IDs scale factors
    'DY_1j_madgraph'              : tnpSample('DY_1j_madgraph',
                                       eosMoriond18 + 'DY1JetsToLLM50madgraphMLM.root',
                                       isMC = True, nEvts =  -1 ),
#    'DY_amcatnlo'                 : tnpSample('DY_amcatnlo',
#                                       eosMoriond18 + 'DYJetsToLLM50amcatnloFXFX.root',
#                                       isMC = True, nEvts =  -1 ),
    'DY_amcatnloext'                 : tnpSample('DY_amcatnloext',
                                       eosMoriond18 + 'DYJetsToLLM50amcatnloFXFXext.root',
                                       isMC = True, nEvts =  -1 ),


    'data_Run2017B' : tnpSample('data_Run2017B' , eosMoriond18 + 'RunB.root' , lumi = 4.793 ),
    'data_Run2017C' : tnpSample('data_Run2017C' , eosMoriond18 + 'RunC.root' , lumi = 9.753),
    'data_Run2017D' : tnpSample('data_Run2017D' , eosMoriond18 + 'RunD.root' , lumi = 4.320 ),
    'data_Run2017E' : tnpSample('data_Run2017E' , eosMoriond18 + 'RunE.root' , lumi = 8.802),
    'data_Run2017F' : tnpSample('data_Run2017F' , eosMoriond18 + 'RunF.root' , lumi = 13.567),

    }



commissioning_Run3 = {

    'DY_powheg'              : tnpSample('DY_powheg',
                                       eos_run3_commissioning_MC + 'merged.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2022B' : tnpSample('data_Run2022B' , eos_run3_commissioning_data2022B + "data.root" , lumi = 0.08 ),
    'data_Run2022C' : tnpSample('data_Run2022C' , eos_run3_commissioning_data2022B + "merge.root" , lumi = 0.166131 )
    }
