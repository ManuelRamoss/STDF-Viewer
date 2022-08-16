import _cystdf
import _cystdf.signal4Analyzer
import sys
import numpy as np

class SelfObject:
  self = {}
  site_cb_dict = {}
  head_cb_dict = {}
  availableSites = []
  availableHeads = []
  testRecTypeDict = {}
  waferInfoDict = {}
  failCntDict = {}
  dutArray = np.array([]) 
  signals = signal4Analyzer()
  resultSignal = self.signals.resultSignal
  progressSignal = self.signals.progressSignal
  finishSignal = self.signals.finishSignal
  stdPath='test_stdf.stdf.gz'

class NXPCustom ():
      # dict to store site/head checkbox objects
    self =  SelfObject()
    def __init__(self):
      atdf=_cystdf.analyzeSTDF(sys.argv[1],self.signal,None,None)
      print(atdf)
