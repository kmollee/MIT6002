import pylab

principal = 10000  # initial investment
interestRate = 0.05
years = 20
values = []

for i in range(years + 1):
    values.append(principal)
    principal += principal * interestRate
# defualt color is blue 'b' red 'r'
# defulat line style '-'
# style is 'b-'
# 'o' is circle
#pylab.plot(range(years + 1), values)
# change line style
#pylab.plot(range(years + 1), values, 'r-')
# linewidth 30 30point
pylab.plot(range(years + 1), values, linewidth=3)
pylab.title('5% Growth, Compounded Annually')

#pylab.xlabel('Years of Compounding')
#pylab.ylabel('Value of Principal ($)')

# change lable font size
pylab.xlabel('Years of Compounding', fontsize=6)
pylab.ylabel('Value of Principal ($)', fontsize=20)

pylab.show()
