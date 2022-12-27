import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import tqdm as tqdm
import sys as sys

'''What was suggested to me, was that this demonstrates
 the flaws in assuming something is truly "random." Someone 
 else that I had asked about the behavior of this voiced
 that the flip sequences should be asymptotic in nature, 
 approaching 50% probability but never crossing it, 
 though as can be observed here, this is often not the case
 in reality.'''

def coinPlot(data: pd.DataFrame) -> None:
 
   '''
   Plots the sequence of flips.
   
   Parameters
   ----------
   data : pd.DataFrame
       data to be plotted.
   '''

   ax1 = data.plot(figsize=[14.275,9.525],linewidth = 1)
   ax1.minorticks_on()
   ax1.title.set_text('Probability of Flipping Heads')
   ax1.tick_params(labelsize=16, labelright=True)
   ax1.axhline(0.5, linewidth = 1.5, color='firebrick', zorder = 1)
   ax1.set_ylim(.4, .6)
   ax1.get_legend().remove()
   ax1.grid(which='both', linestyle='-', linewidth='1', color='dimgrey')
   ax1.grid(which='minor', linestyle=':', linewidth='1', color='grey')
   plt.pause(.01)
    

'''Virtually flips the coin. Also stores data.'''

flips = pd.DataFrame()

for j in tqdm.tqdm(range(10)): #desired amount of flipping sequences
        
    allFlips = []
    probabilitiesHeads = []
    
    heads = 0
    tails = 0
    for i in tqdm.tqdm(range(1000)): #desired amount of flips
         currentFlip = random.randint(0, 1)
         if (currentFlip == 0):
            allFlips.append("Heads")
            headsCount = allFlips.count("Heads")
            tailsCount = allFlips.count("Tails")
            totalCount = (headsCount + tailsCount)
            pHeads = (headsCount/totalCount)
            probabilitiesHeads.append(pHeads)
         else:
            allFlips.append("Tails")
            headsCount = allFlips.count("Heads")
            tailsCount = allFlips.count("Tails")
            totalCount = (headsCount + tailsCount)
            pHeads = (headsCount/totalCount)
            probabilitiesHeads.append(pHeads)
    
    flips[j] = np.array(probabilitiesHeads)

coinPlot(flips)


'''Used to observe behavior of flips after n(params) flips
   have taken place. Have not included the csv file for the 
   flip sequences up to n = 1,000,000, as it was about 50MB, 
   but generate one of your own if curious. I've attached a
   chart showing the results from the code below in the repository'''

try:
    flips = pd.read_csv('flips.csv')
except FileNotFoundError:
    print("\n\n Not all of this code will run for you. Review last comment for further details.")
    sys.exit()

params = [500000, 600000, 700000, 800000, 900000]
minValues = []
maxValues =[]
standardDeviations = []

for i in params:
    
    subsection = flips[i:1000000]
    #print(subsection)
    #subsectionAbove50 = subsection[subsection > 0.5]
    print("\nStandard Deviations\n")
    print(subsection.std())
    standardDeviations.append(subsection.std())
    print("\nMaximum Values\n")
    print(subsection.max())
    maxValues.append(subsection.max())
    print("\nMinimum Values\n")
    print(subsection.min())
    minValues.append(subsection.min())
    subsection['0'].plot(figsize=[14.275,9.525],linewidth = 1, color='black')
    subsection['1'].plot(figsize=[14.275,9.525],linewidth = 1, color='dimgray')
    plt.axhline(.5,linewidth = 1.5, color='firebrick', zorder = 1)
    plt.title('Flips 500,000 through 1,000,000 for 2 Sequences')
    plt.tick_params(labelsize=16, labelright=True)
    plt.grid(which='both', linestyle='-', linewidth='1', color='dimgrey')
