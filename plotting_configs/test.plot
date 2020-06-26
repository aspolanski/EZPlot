# example configuration file for auto_plotter.py
# use with ConfigParser package
# Author: Alex Polanski
# 05/5/2020

############################################################################
[Labels]
############################################################################

#title or no title (boolean)
SET_TITLE = True

#title of the plot
TITLE = This is my Test Title 

#legend (boolean)
LEG = True

#label of the Abscissa (x-axis)
ABS_LABEL = Abscissa Label

#label of the ordinate (y-axis)
ORD_LABEL = Ordinate label

#Font type (see your system's available font families)
FONT = Liberation Serif

#Font size (points)
FONT_SIZE = 26

############################################################################
[Plot Type]
############################################################################

#Plot data as a scatter plot (boolean)
SCATTER = False 

#Plot data continuously (boolean)
CONT = True

#Plot data with error bars (boolean)
ERR = False

############################################################################
[Axis Params]
############################################################################

#plot with tight layout
TIGHT = True

#set x limit (comma seperated)
XLIM = 0.0,5.0 

#set y limit (comma seperated)
YLIM = -3.0,3.0

#Tick stuff

#x tick posotions
XTICK_POS = both

#y tick positions
YTICK_POS = both

#x tick direction
XTICK_DIR = in

#y tick direction
YTICK_DIR = in

#x minor ticks?
XMINOR = True

#x minor ticks per major tick
XMIN_SPACE = 5

#y minor ticks?
YMINOR = True

#y minor ticks per major tick
YMIN_SPACE = 4

############################################################################
[Data Params]
############################################################################

#Linewidth
LINEWIDTH = 3

#Marker Size
MARK_SIZE = 8.0

#Marker type
MARK_TYPE = o

#color
COLOR = red

#errorbar capsize
CAP_SIZE = 0.0

############################################################################
[Multi-Plotting]
############################################################################

#config file for multi plotting, contains color, linewdth, marker size etc information. Above Data Params not relevant when multi-plotting.
MULTI_CONFIG = /home/alex/research/code/plotting_configs/multi_configs/multi_test.mplt
 
############################################################################
[Subplots]
############################################################################






