# perioddoublingbifurcation
A simple python experiment showing period doubling bifurcation on varying growth rate in a logistics curve.


##Simple population size formula
The formula for getting the population size in the presence of some limiting factor is simply:
>future_population = growth_rate*current_population*(1.0-current_population/population_limit)

This is simply implemented in python as my *breed()* function.
>
>def breed(x, l):
>    ans = l*x*(1.0-x/1000) #gets the population of next timestep
>    return ans

##Steady state population
To get the steady state population, we need to let the system run for a certain period of time, say 100 time steps. You may wish to increase this value, but I find that at 100 steps, it will reach (or at least be close enough) to steady state. 

>def finalPop(x, k): #Gets the steady state population
>    a = (1/10**55)*(10**k) #initialize initial population. k is a multiplier that increases the population 10 times.
>    arr = []
>    for i in range(100):
>        a = breed(a, x)
>        arr.append(a)
>    return arr[len(arr)-1]
>

##Plotting the Period Doubling Bifurcation
The *finalpop()* function simply returns a steady state value. Hence, we will need to store this value into an array to compare the evolution of the steady state value with varying growth rate. 

To do this, we use the *getplot()* function
>
>def getPlot(k):
>    myarr = []
>    for i in np.linspace(starta,enda, sizearr):
>        myarr.append(finalPop(i, k))    
>        #Gets the steady state population for a given growth rate, i and initial condition multiplier, k
>    plt.scatter(np.linspace(starta,enda, sizearr), myarr, marker='o', s=0.1); #Plots the graph
>

I've modified the file to plot multiple time and to convert each frame into a GIF. 

