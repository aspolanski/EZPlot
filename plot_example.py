#!/usr/bin/env python3

##############################################################
#Example script for using both plotit and plot_more functions#
##############################################################
#Author: Alex Polanski    Date: June 25 2020                 #
##############################################################

import matplotlib.pyplot as plt
import numpy as np
from auto_plotter import plotit,plot_more


#Create some data to plot -- sines, c osines, and some scatter.

time = np.linspace(0,10,30)

sig = np.sin(time)

sig_err = 1.5*np.ones(len(sig)) #change 'plot type' to 'err' to plot errorbars.

sig2 = np.cos(time)

sig3 = sig2*np.random.randn(len(sig2))

#Load the plotting configuation file

plot_file = '/home/alex/research/code/plotting_configs/test.plot' 

#Plot a single data set.

ob = plotit(plot_file, time, sig, sig_err)

plt.show()

#To plot multiple data sets on one axis, we need to compile x and y data into their own lists.
#compile data into the lists:

x = [time, time, time]

y = [sig,sig2,sig3]

#plot_more only takes lists of data. The same plotting config can be used -- the parameters for each data set are defined in 'multi_test.mplt' and is loaded from the plotting configuration file.

plot_more(plot_file,x,y)

plt.show()
