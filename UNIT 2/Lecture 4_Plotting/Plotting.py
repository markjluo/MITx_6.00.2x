import matplotlib.pyplot as plt


mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential =[]

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)


plt.figure('Quad vs Exp')
plt.clf()
plt.subplot(428)
plt.title('Quadratic xy')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.plot(mySamples, myQuadratic, 'r--', label='a', linewidth=4)
plt.plot(myQuadratic, mySamples, c='k', label='b', linewidth=0.1)
plt.legend(loc='upper left')

plt.subplot(421)
plt.title('Exponential xy')
plt.xlabel('x')
plt.xlabel('y')
plt.plot(mySamples, myExponential)
plt.plot(myExponential, mySamples)
plt.yscale('log')
plt.xscale('log')
plt.xlim(1, 5)
plt.ylim(1, 5)
plt.show()