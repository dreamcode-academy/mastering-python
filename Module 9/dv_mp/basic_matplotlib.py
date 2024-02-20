import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [1,4,9,16])
plt.plot([2,3,1,4], [2,2,5,10])

plt.title('First plot')
plt.xlabel('label x')
plt.ylabel('label y')

plt.legend(['label1', 'label2'])
plt.show()