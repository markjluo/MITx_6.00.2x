import matplotlib.pyplot as plt

def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    reference = [0]
    mRate = rate/12
    for i in range(1, terms+1):
        base += [i]
        reference += [reference[-1] + monthly]
        savings += [savings[-1]*(1 + mRate) + monthly]
    return base, reference, savings



def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure('Retire Monthlies')
    plt.clf()
    for monthly in monthlies:
        plt.title('Monthely = '+ str(monthly))
        base, reference, savings = retire(monthly, rate, terms)
        # plt.plot(base, reference, 'k--', label='Reference Line', linewidth=0.5)
        plt.plot(base, savings, label='Savings Monthly = '+str(monthly))
        plt.legend(loc='upper left')
    plt.show()





displayRetireWMonthlies([400, 500, 600], 0.05, 40*12)