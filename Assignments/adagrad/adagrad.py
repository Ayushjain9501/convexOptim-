import numpy as np 
import math
import pandas as pd 
import matplotlib.pyplot as plt 
import time


dataset = pd.read_csv(r"~/convexOptim/Assignments/dataset.csv",index_col=0)
x=np.array(dataset['x'])
y=np.array(dataset['y'])


def value(theta0, theta1, x):
    y = theta0 + theta1 * x
    return y

def squareLoss(theta0,theta1,x,y):
    ypred = np.array([value(theta0,theta1,x) for x in x])
    subtracted = ypred - y
    sumSquareLoss = np.sum(np.power(subtracted,2))
    return sumSquareLoss

def partialDeriv0(theta0,theta1,x,y):
    ypred = np.array([value(theta0,theta1,x) for x in x])
    
    subtracted = ypred - y
    update = np.sum(subtracted) * 2
    return update


def partialDeriv1(theta0,theta1,x,y):
    ypred = np.array([value(theta0,theta1,x) for x in x])
    
    subtracted =2* x * (ypred - y)
    update = np.sum(subtracted)
    return update

#try to fit a linear model
# y= mx+c type
theta0 = 0
theta1 = 1


iterations = 1000
lossHistory = np.empty(iterations)
count = [i for i in range(1,iterations+1)]  #x-axis for plotting lossHistory
eta = 10
epsilon = 0.00000001
gTheta0 = gTheta1 = 0

startTime = time.time()
for iteration in range(0,iterations):
    
    loss = squareLoss(theta0,theta1,x,y)
    partialTheta0 = partialDeriv0(theta0,theta1,x,y)
    partialTheta1 = partialDeriv1(theta0,theta1,x,y)
    gTheta0 = gTheta0 + (partialTheta0**2)
    gTheta1 = gTheta1 + (partialTheta1**2)
    lrTheta0 = eta/math.sqrt(epsilon + gTheta0)
    lrTheta1 = eta/math.sqrt(epsilon + gTheta1)
    step0 = lrTheta0  * partialTheta0
    step1 = lrTheta1  * partialTheta1
    theta0 = theta0 - step0
    theta1 = theta1 - step1
    lossHistory[iteration] = loss

endTime = time.time()

print("Theta 0 : ",theta0,"Theta1 : ",theta1)
print("Time Taken : ",endTime-startTime)

plt.figure(0)
plt.scatter(x,y, c='red')
plt.plot(x,theta0 + theta1*x)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Dataset')
plt.savefig('output.png')
plt.show()

plt.figure(1)
plt.plot(count,lossHistory)
plt.xlabel('iteration')
plt.ylabel('Loss')
plt.title('Loss History')
plt.savefig('loss.png')
plt.show()


