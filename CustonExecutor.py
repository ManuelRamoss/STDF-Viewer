from _cystdf import stdfRecordAnalyzer

class NXPCustom (self):
      # dict to store site/head checkbox objects
    self.site_cb_dict = {}
    self.head_cb_dict = {}
    self.availableSites = []
    self.availableHeads = []
    self.testRecTypeDict = {}
    self.waferInfoDict = {}
    self.failCntDict = {}
    self.dutArray = np.array([]) 
    self.signals = signal4Analyzer()
    self.resultSignal = self.signals.resultSignal
    self.progressSignal = self.signals.progressSignal
    self.finishSignal = self.signals.finishSignal
    self.stdPath='test_stdf.stdf.gz'
    
    def __init__():
        stdfRecordAnalyzer(self.stdPath, self.resultSignal, None, N)
