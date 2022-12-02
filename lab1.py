# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:58:32 2022

@author: theko
"""

## cognitive modelling lab assignment 1
import matplotlib.pyplot as plt

def start(Type="middle"):
    time = 0
    return time
    
def perceptualstep(Type="middle"):
    if Type=="middle":
        time = 100
    elif Type=="slow":
        time=200
    elif Type=="fast":
        time=50
    return time
    
def cognitivestep(Type="middle"):
    if Type=="middle":
        time = 70
    elif Type=="slow":
        time=170
    elif Type=="fast":
        time=25
    return time
    
def motorstep(Type="middle"):
    if Type=="middle":
        time = 70
    elif Type=="slow":
        time=100
    elif Type=="fast":
        time=30
    return time

def example1():
    totaltime = (start() + perceptualstep() + cognitivestep() + motorstep())
    return totaltime

def example2(completeness="extremes"):
    if completeness == 'extremes':
        fastman = (start() + perceptualstep("fast") + cognitivestep("fast") + motorstep("fast"))
        middleman = (start() + perceptualstep("middle") + cognitivestep("middle") + motorstep("middle"))
        slowman = (start() + perceptualstep("slow") + cognitivestep("slow") + motorstep("slow"))
        return fastman, middleman, slowman #this is correct according what the doc says :D
    elif completeness == 'all': #maybe a bit overkill LOL
        print("Order: Start -> Perceptual -> Cognitive -> Motor")
        comblist = ["fast", "middle", "slow"]
        totallist = []
        orderlist = []
        for i in comblist:
            a = perceptualstep(i)
            for j in comblist:
                b = cognitivestep(j)
                for n in comblist:
                    c = motorstep(n)
                    total = a+b+c
                    order = f"{i} -> {j} ->{n}"
                    totallist.append(total)
                    orderlist.append(order)
                    
        plot = plt.boxplot(totallist)
            
            
    else:
        return "Wrong input"
    return orderlist,totallist,plot


def example3():
    print("Order: Start -> Perceptual -> Cognitive -> Motor")
    comblist = ["fast", "middle", "slow"]
    totallist = []
    orderlist = []
    
    for i in comblist:
            a = perceptualstep(i)*2 #because there are two perception steps in the new process, perceptual processing for two stimuli
            for j in comblist:
                b = cognitivestep(j)*2 #because there are two motor steps in the new process, comparing stimuli, motor prep
                for n in comblist:
                    c = motorstep(n)
                    total = a+b+c
                    order = f"{i} -> {j} ->{n}"
                    totallist.append(total)
                    orderlist.append(order)    
    return orderlist,totallist
                    
def example4():
    t = [40, 80, 110, 150, 210, 240]
    comblist = ["fast", "middle", "slow"]
    totallist = []
    orderlist = []
    
    for stim in t:
        for i in comblist:
            perc1 = perceptualstep(i)
            if stim >= perc1:
                perc = stim+perc1
            if stim <= perc1:
                perc = perc1 + perc1
                
            for j in comblist:
                b = cognitivestep(j)*2 #because there are two motor steps in the new process, comparing stimuli, motor prep
                for n in comblist:
                    c = motorstep(n) 
                    total = perc+b+c
                    order = f"time = {stim}:  {i} -> {j} ->{n}"
                    totallist.append(total)
                    orderlist.append(order)   
    return totallist, orderlist


#### NOT COMPLETE


def example5():
    print("Order: Start -> Perceptual -> Cognitive -> Motor")
    comblist = ["fast", "middle", "slow"]
    totallist = []
    orderlist = []
    EPlist =[]
    EP = 0.01
    
    
    for i in comblist:
        
        if i == "fast":
            EP= EP*3
            EP= EP*3
        elif i =="middle":
            EP= EP*2
            EP= EP*2
        elif i=="slow":
            EP= EP*0.5
            EP= EP*0.5
            
        a = perceptualstep(i)*2 #because there are two perception steps in the new process, perceptual processing for two stimuli
        for j in comblist:
            if j == "fast":
                EP= EP*3
                EP= EP*3
            elif j =="middle":
                EP= EP*2
                EP= EP*2
            elif j=="slow":
                EP= EP*0.5
                EP= EP*0.5
            b = cognitivestep(j)*2
            for n in comblist:
                if j == "fast":
                    EP= EP*3
                    EP= EP*3
                elif j =="middle":
                    EP= EP*2
                    EP= EP*2
                elif j=="slow":
                    EP= EP*0.5
                    EP= EP*0.5                
                
                
                c = motorstep(n) #because there are two motor steps in the new process, comparing stimuli, motor prep
                total = a+b+c
                order = f"{i} -> {j} ->{n}"
                totallist.append(total)
                orderlist.append(order) 
                EPlist.append(EP)
                EP = 0.01
    return EPlist,totallist,orderlist
    
                    
                               
import matplotlib.pyplot as plt
b,a,c = example5()
plt.scatter(a,b)
plt.show




"""
    step1 = start(x)
    step2 = perceptualstep(x)
    step3 = perceptualstep(x)
    step4 = cognitivestep(x)
    step5 = cognitivestep(x)
    step6 = motorstep(x)
    
"""       
