import matplotlib.pyplot as plt


categories = ['Category A', 'Category B', 'Category C']

values = [23, 45, 56]

'''
# Bar chart
plt.bar(categories, values)
plt.show()


#Histograms for Frequency Distribution
ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 2, 102]

plt.hist(ages, bins=10)

plt.show()
'''

# Scatter Plots

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]

y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86]


#plt.style.use('stlye name') styles

plt.style.use('ggplot')

plt.scatter(x,y, color='green')

plt.axis([0, 20, 75, 110])
plt.grid(True)  

plt.annotate('Important Point', xy=(x[2], y[2]))
plt.text(10,105, 'Example text')


plt.xlabel('x var')
plt.ylabel('y var')
plt.title("Customized Scatter plot")

#plt.show()

plt.savefig('plot.svg', format='svg', dpi=300)
