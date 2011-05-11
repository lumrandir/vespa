from subprocess import call
from PyQt4.QtCore import QMimeData
import csv

class Spike(object):
        def __init__(self):
                pass

        def readCSV(self):
                fileFP = csv.reader(open("fixedPeriodResults.csv", "r"))
                self.fpResults = map(lambda l: map(int, l), fileFP)
                fileFS = csv.reader(open("fixedSizeResults.csv", "r"))
                self.fsResults = map(lambda l: map(int, l), fileFS)
                fpu = min(self.fpResults[0])
                self.optimalSize = self.fpResults[0].index(fpu) + 1
                fsu = min(self.fsResults[0])
                self.optimalPeriod = self.fsResults[0].index(fsu) + 1
               
def calculateTheApocalypse(vessel, spike):
        blood = collectTheBlood(vessel)
        if not callTheDemon(blood) == 0:
                print("Noe gikk galt...")
                return
        spike.readCSV()
        vessel.resultPeriodEdit.setText(str(spike.optimalSize))
        vessel.resultSizeEdit.setText(str(spike.optimalPeriod))
        return

def callTheDemon(blood):
        invocation = "./vespa \"{args}\"".format(args=blood)
        exitCode = call(invocation, shell=True)
        return exitCode

def collectTheBlood(vessel):
        vial = (int(vessel.initialStorageEdit.text()),
                        int(vessel.countPeriodEdit.text()),
                        int(vessel.fixedPeriodEdit.text()),
                        int(vessel.fixedSizeEdit.text()),
                        int(vessel.maxPeriodEdit.text()),
                        int(vessel.maxSizeEdit.text()),
                        int(vessel.unitCostEdit.text()),
                        int(vessel.orderCostEdit.text()),
                        int(vessel.deficitCostEdit.text())
               )
        buf = []
        for row in range(0, vessel.ordTable.rowCount()):
                buf = buf + [(int(vessel.ordTable.item(row, 0).text()), 
                                float(vessel.ordTable.item(row, 1).text())
                            )]
        vial = vial + (list(set(buf)),)
        buf = []
        for row in range(0, vessel.delTable.rowCount()):
                buf = buf + [(int(vessel.delTable.item(row, 0).text()),
                                float(vessel.delTable.item(row, 1).text())
                            )]
        vial = vial + (list(set(buf)),)
        return vial

