import numpy as np
import matplotlib.pyplot as plt
from bisect import bisect_left


lower_bound = float(input("What is the first bound point? "))
upper_bound = float(input("What is the second bound point? "))
num_riemann_sums = int(input("What is the wanted number of Rieman sums? "))
num_values = int(input("How many values do you want in the graph? "))
dx = (upper_bound-lower_bound)/num_riemann_sums

f = input("What is the function you want to use? (leave blank for -x^2+13*x) ")

f = f.replace('^', '**').replace('sin', 'np.sin').replace('cos', 'np.cos').replace('tan', 'np.tan').replace('sqrt', 'np.sqrt').replace('log', 'np.log').replace('exp', 'np.exp')

# function in the random sample
# where the function is negative, the code will consider the absolute value
def unnormalizedFunction(x):
  if f == "":
    return (-x**2+13*x)
  else:
    return eval(f)




sampleValues = np.linspace(lower_bound,upper_bound,(num_riemann_sums + 1))

def function(x):
  valueSoFar = 0
  for v in sampleValues:
    valueSoFar = valueSoFar + np.abs(unnormalizedFunction(v))*dx
  return(np.abs(unnormalizedFunction(x))/valueSoFar)





ASF = []
for s in sampleValues:
  if s == sampleValues[0]:
    ASF = [function(s)*dx]
  else: 
    ASF.append(ASF[-1] + (function(s)*dx))

def inverseAreaSoFar(output):
  closest = sampleValues[np.argmin([np.abs(x - output) for x in ASF])]
  return closest

ASFSampleValues = ASF
ASFSampleValues.sort()

def sampleRand(rand):
    # Find the index of the closest value to rand in the sorted ASFSampleValues array
    index = bisect_left(ASFSampleValues, rand)
    if index == 0:
        closest = ASFSampleValues[0]
    elif index == len(ASFSampleValues):
        closest = ASFSampleValues[-1]
    else:
        before = ASFSampleValues[index - 1]
        after = ASFSampleValues[index]
        closest = before if rand - before <= after - rand else after
    return inverseAreaSoFar(closest)


def randomValues(n):
  random_values = []
  for i in range(n):
    random_values.append(sampleRand(np.random.random()))
  return random_values



randomResults = randomValues(num_values)

if len(randomResults) <= 1000:
  print(str(randomResults))

def graph(array):
    unique, counts = np.unique(array, return_counts=True)
    plt.bar(unique, counts)
    plt.xlabel("Number")
    plt.ylabel("Frequency (probability)")
    plt.title("Frequency of Numbers")
    plt.show()

graph(randomResults)
