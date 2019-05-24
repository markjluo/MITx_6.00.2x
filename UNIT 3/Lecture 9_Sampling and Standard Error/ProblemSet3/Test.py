import random
import pylab



class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """


'''
End helper code
'''


class SimpleVirus(object):

    def __init__(self, maxBirthProb, clearProb):
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        return self.maxBirthProb

    def getClearProb(self):
        return self.clearProb

    def doesClear(self):
        prob = random.random()
        if prob <= self.getClearProb():
            return True
        else:
            return False

    def reproduce(self, popDensity):
        prob = random.random()
        repro = self.getMaxBirthProb() * (1 - popDensity)
        if prob <= repro:
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
        else:
            raise NoChildException


class Patient(object):
    def __init__(self, viruses, maxPop):
        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        return self.viruses

    def getMaxPop(self):
        return self.maxPop

    def getTotalPop(self):
        return len(self.viruses)

    def update(self):
        clear = []
        for virus in self.getViruses():
            if virus.doesClear():
                clear.append(virus)
        for cleared in clear:
            self.viruses.remove(cleared)
        popden = self.getTotalPop() / self.getMaxPop()
        viruses_copy = self.getViruses().copy()
        for left in viruses_copy:
            try:
                self.viruses.append(left.reproduce(popden))
            except NoChildException:
                continue
        return self.getTotalPop()


# virus = SimpleVirus(1.0, 0.0)
# pa = Patient([virus], 100)
# pa.update()
# print(pa.getTotalPop())


def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):

    means = []
    timeSeries = []

    for tiral in range(numTrials):
        viruses = []
        for i in range(numViruses):
            viruses.append(SimpleVirus(maxBirthProb, clearProb))
        patient = Patient(viruses, maxPop)
        totalviruses = []
        for i in range(300):
            patient.update()
            totalviruses.append(patient.getTotalPop())
        timeSeries.append(totalviruses)

    for timeStep in range(len(timeSeries[0])):
        samples = []
        for serie in timeSeries:
            samples.append(serie[timeStep])
        means.append(sum(samples)/len(samples))

    pylab.plot(means, label="SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc="best")
    pylab.show()


# simulationWithoutDrug(100, 1000, 0.1, 0.05, 1)


class ResistantVirus(SimpleVirus):

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = float(mutProb)

    def getResistances(self):
        return self.resistances

    def getMutProb(self):
        return self.mutProb

    def isResistantTo(self, drug):
        if drug in self.resistances.keys():
            return self.getResistances()[drug]
        else:
            return False

    def reproduce(self, popDensity, activeDrugs):
        repro = True
        try:
            for drug in activeDrugs:
                if not self.getResistances()[drug]:
                    repro = False
        except KeyError:
            repro = False
        if repro:
            prob = random.random()
            if prob <= self.maxBirthProb * (1 - popDensity):
                resis_copy = self.getResistances().copy()
                offspring = ResistantVirus(self.getMaxBirthProb(), self.getClearProb(), resis_copy, self.getMutProb())
                for drug in offspring.getResistances():
                    if random.random() <= self.getMutProb():
                        offspring.resistances[drug] = not offspring.resistances[drug]
                return offspring
            else:
                raise NoChildException
        else:
            raise NoChildException





class TreatedPatient(Patient):

    def __init__(self, viruses, maxPop):
        Patient.__init__(self, viruses, maxPop)
        self.drugs = []

    def addPrescription(self, newDrug):
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)

    def getPrescriptions(self):
        return self.drugs

    def getResistPop(self, drugResist):

        pop = 0
        for virus in self.getViruses():
            res = True
            for drug in drugResist:
                if drug not in virus.getResistances().keys() or not virus.getResistances()[drug]:
                    res = False
            if res == True:
                pop += 1
        return pop


    def update(self):

        clear = []
        for virus in self.getViruses():
            if virus.doesClear():
                clear.append(virus)
        for cleared in clear:
            self.viruses.remove(cleared)
        popden = self.getTotalPop() / self.getMaxPop()
        viruses_copy = self.getViruses().copy()
        for left in viruses_copy:
            # print(len(self.viruses))
            try:
                self.viruses.append(left.reproduce(popden, self.getPrescriptions()))
            except NoChildException:
                pass
        return self.getTotalPop()


# virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
# # virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
# # virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
# # patient = TreatedPatient([virus1, virus2, virus3], 100)
# #
# # print(patient.getResistPop(['drug1']))
# # print(patient.getResistPop(['drug2']))
# # print(patient.getResistPop(['drug1', 'drug2']))
# # print(patient.getResistPop(['drug3']))
# # print(patient.getResistPop(['drug1', 'drug3']))
# # print(patient.getResistPop(['drug1', 'drug2', 'drug3']))



def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials):

    trialTotal = []
    trialResist = []

    meanTotal = []
    meanResist = []
    for trial in range(numTrials):
        viruses = []
        for i in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        p = TreatedPatient(viruses, maxPop)
        virusesT = []
        virusesR = []
        for step in range(150):
            p.update()
            virusesT.append(p.getTotalPop())
            if not resistances.keys():
                virusesR.append(0)
            else:
                virusesR.append(p.getResistPop(resistances.keys()))
        p.addPrescription('guttagonol')
        for step in range(150):
            p.update()
            virusesT.append(p.getTotalPop())
            if not resistances.keys():
                virusesR.append(0)
            else:
                virusesR.append(p.getResistPop(resistances.keys()))
        trialTotal.append(virusesT)
        trialResist.append(virusesR)

    for time_step in range(len(trialTotal[0])):
        sampleT = []
        sampleR = []
        for trialT in trialTotal:
            sampleT.append(trialT[time_step])
        meanTotal.append(sum(sampleT)/len(sampleT))
        for trialR in trialResist:
            sampleR.append(trialR[time_step])
        meanResist.append(sum(sampleR)/len(sampleR))



    pylab.plot(meanTotal, label="Total Viruses")
    pylab.plot(meanResist, label="Virus With Resistances")
    pylab.title("Virus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc="best")
    pylab.show()





# virus = ResistantVirus(0.1, 0.05, {'guttagonol': False}, 0.005)
# p = TreatedPatient([virus], 1000)

simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 20)

# simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)