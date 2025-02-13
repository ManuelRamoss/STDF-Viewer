import _cystdf
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal as Signal

import sys
import numpy as np

class nxpSignal4Analyzer(QtCore.QObject):
    # get text from analyzer
    resultSignal = Signal(str)
    progressSignal = Signal(int)
    # get finish signal from analyzer
    finishSignal = Signal(bool)

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
  signals = nxpSignal4Analyzer()
  resultSignal = signals.resultSignal
  progressSignal = signals.progressSignal
  finishSignal = signals.finishSignal
  stdPath='test_stdf.stdf.gz'

      # dict to store site/head checkbox objects
self =  SelfObject()
atdf=_cystdf.analyzeSTDF(sys.argv[1],self.signals,None,None)
print("excuting something")
print(atdf)
