# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:37:36 2020

@author: ivanling92
https://github.com/ivanling92/perioddoublingbifurcation
A simple python experiment showing period doubling bifurcation on varying growth rate in a logistics curve.

"""
import matplotlib.pyplot as plt 
import numpy as np
import imageio


#Parameters
sizearr = 10000 #Points per plot
starta = 1.0 #Starting point (Recommended start point is around 2.8)
enda = 3.89 #Endpoint don't go beyond 4, it gives infinite (Because of chaos)

def breed(x, l):
    ans = l*x*(1.0-x/1000) #gets the population of next timestep
    return ans

def finalPop(x, k): #Gets the steady state population
    a = (1/10**55)*(10**k) #initialize initial population. k is a multiplier that increases the population 10 times.
    arr = []
    for i in range(100):
        a = breed(a, x)
        arr.append(a)
    return arr[len(arr)-1]

def getPlot(k):
    myarr = []
    for i in np.linspace(starta,enda, sizearr):
        myarr.append(finalPop(i, k))    #Gets the steady state population for a given growth rate, i and initial condition multiplier, k
    fig, ax = plt.subplots(figsize=(10,5)) #Gets the plot area
    ax.scatter(np.linspace(starta,enda, sizearr), myarr, marker='o', s=0.1); #Plots the graph
    ax.set_ylim(0, 1000) #Set the Y limit to be constant so it looks nice on animation
    fig.canvas.draw() #Draw it
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8') #Take the figure, convert to image
    image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,)) #Resize the image
    return image #Return it to the GIF maker

kwargs_write = {'fps':1.0, 'quantizer':'nq'}
imageio.mimsave('./powers.gif', [getPlot(k) for k in range(60)], fps=13) #Takes the returned image in an array and convert to GIF
#Change the fps to make animation slower or faster.



