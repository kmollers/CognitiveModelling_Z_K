import numpy 
import matplotlib.pyplot as plt
import re

f = open("CategoryVectors.txt", "r")
v = open("CategoryLabels.txt", "r")
r = open ("NeuralResponses_S1.txt", "r")
#object # O.. is inanim in their task, but in file it says 2 
objNames = numpy.loadtxt(v, delimiter=',', skiprows=1, dtype=str)
data = numpy.loadtxt(f, delimiter=',', skiprows=1, dtype=str)
response = numpy.loadtxt(r, delimiter=',', skiprows=1, dtype=str)
pattern = r'[0-9]' 
results_anim =[]
results_unanim =[]
calc = 0
i=0

for result in response:
    #neurual Response , count neural response for anim ( value 1) and unanim (value 0)
    for cell in result:
        # no idea what to do with 5 different columns, took only first column, find the value of the object in a given response
       if(data[i][0] == '1'):
            results_anim.append(float(cell))
            i=i+1


for row in data:
    for value in row:
        for y in objNames:
            ## is animmate number 1 
            if(value == y[1] and not y[2].isdigit()):
                    print("hello")


print(results_anim)
fig, ax = plt.subplots()
N = 2
animMeans = (max(results_anim), min(results_anim))
ind = numpy.arange(N)    # the x locations for the groups

p1 = ax.bar(ind, animMeans)
p2 = ax.bar(ind, animMeans)

ax.axhline(0, color='grey', linewidth=0.8)
ax.set_xticks(ind, labels=['animate', 'animate'])
ax.legend()


ax.bar_label(p1, label_type='center')
ax.bar_label(p2, label_type='center')
ax.bar_label(p2)

plt.show()