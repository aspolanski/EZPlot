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
TITLE = Simulated Atmosphere - Wolf503b 

#label of the Abscissa (x-axis)
ABS_LABEL = Wavelength (microns)

#label of the ordinate (y-axis)
ORD_LABEL = Depth (PPM)

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
XLIM = 0.2,30.0 

#set y limit (comma seperated)
YLIM = 0.0007,0.0011

#plot x-axis with log scale (boolean)
XLOG = True

#plot y-axis with log scale (boolean)
YLOG = False

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
LINEWIDTH = 1

#Marker Size
MARK_SIZE = 8.0

#Marker type
MARK_TYPE = o

#color
COLOR = blue

#errorbar capsize
CAP_SIZE = 0.0
 
############################################################################
[Subplots]
############################################################################






