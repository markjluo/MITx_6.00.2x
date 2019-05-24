#1.
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    viruses = []
    means = []
    timeSeries = []
    for i in range(numViruses):
        viruses.append(SimpleVirus(maxBirthProb, clearProb))

    for tiral in range(numTrials):
        patient = Patient(viruses, maxPop)
        print(viruses)
        totalviruses = []
        for i in range(10):
            #### This step modified the viruses list, since it is an attribute of patient which was modified by the update method
            patient.update()
            totalviruses.append(patient.getTotalPop())
        timeSeries.append(totalviruses)
        print(timeSeries)

    for timeStep in range(len(timeSeries[0])):
        samples = []
        for serie in timeSeries:
            samples.append(serie[timeStep])
        means.append(sum(samples)/len(samples))



print(simulationWithoutDrug(10, 1000, 0.1, 0.05, 3))
