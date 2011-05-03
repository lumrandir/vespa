from subprocess import call
from PyQt4.QtCore import QMimeData

def calculateTheApocalypse(vessel):
        blood = collectTheBlood(vessel)
        if not callTheDemon(blood) == 0:
                print("Noe gikk galt...")
                return
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

