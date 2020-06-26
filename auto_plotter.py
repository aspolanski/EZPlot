#!/usr/bin/env python3

################################################################
# ______     ______     ______   __         ______     ______  #   
#/\  ___\   /\___  \   /\  == \ /\ \       /\  __ \   /\__  _\ #   
#\ \  __\   \/_/  /__  \ \  _-/ \ \ \____  \ \ \/\ \  \/_/\ \/ #   
# \ \_____\   /\_____\  \ \_\    \ \_____\  \ \_____\    \ \_\ #   
#  \/_____/   \/_____/   \/_/     \/_____/   \/_____/     \/_/ #   
################################################################                                                                
# Author: Alex Polanski  Date: June 24th 2020                  #
################################################################

import matplotlib.pyplot as plt
import numpy as np
import configparser
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

def plotit(config,x,y, *sigma):
    cfg = configparser.ConfigParser()
    cfg.read(config)
    
    font = {'family' : cfg['Labels']['FONT'] , 'size' : cfg['Labels']['FONT_SIZE']} 
    plt.rc('font', **font)
    fig, ax1 = plt.subplots(1)
    

    xlims = cfg['Axis Params']['XLIM'].split(',')
    xlims = [float(i) for i in xlims]

    ylims = cfg['Axis Params']['YLIM'].split(',')
    ylims = [float(i) for i in ylims]
    
    #title or no title
    if cfg['Labels'].getboolean('SET_TITLE') == True:
        ax1.set_title(cfg['Labels']['TITLE'])

    ax1.set_xlim(xlims[0],xlims[1])
    ax1.set_ylim(ylims[0],ylims[1])
    
    ax1.set_xlabel(cfg['Labels']['ABS_LABEL'])
    ax1.set_ylabel(cfg['Labels']['ORD_LABEL'])
    

    #Tick handling
    ax1.xaxis.set_ticks_position(cfg['Axis Params']['XTICK_POS'])
    ax1.yaxis.set_ticks_position(cfg['Axis Params']['YTICK_POS'])
    
    if cfg['Axis Params'].getboolean('XMINOR') == True:
        xwhich = 'both'
        ax1.xaxis.set_minor_locator(AutoMinorLocator(float(cfg['Axis Params']['XMIN_SPACE'])))
    else:
        xwhich = 'major'

    if cfg['Axis Params'].getboolean('YMINOR') == True:
        ywhich = 'both'
        ax1.yaxis.set_minor_locator(AutoMinorLocator(float(cfg['Axis Params']['YMIN_SPACE'])))
    else:
        ywhich = 'major'


    ax1.tick_params(axis='x', which = xwhich, direction = cfg['Axis Params']['XTICK_DIR'])
    ax1.tick_params(axis='y', which = ywhich, direction = cfg['Axis Params']['YTICK_DIR'])


    #Decide Scaling

    if cfg['Axis Params'].getboolean('XLOG') == True:
        ax1.set_xscale('log')
    
    if cfg['Axis Params'].getboolean('YLOG') == True:
        ax1.set_yscale('log')

        
      
    #Decide the plot type
    if cfg['Plot Type'].getboolean('SCATTER') == True:
        plot_object = ax1.scatter(x,y, 
                c = cfg['Data Params']['COLOR'], 
                s = float(cfg['Data Params']['MARK_SIZE']), 
                marker = cfg['Data Params']['MARK_TYPE'])

    if cfg['Plot Type'].getboolean('CONT') == True:
        plot_object = ax1.plot(x,y,
                color = cfg['Data Params']['COLOR'],
                linewidth = float(cfg['Data Params']['LINEWIDTH']))

    if cfg['Plot Type'].getboolean('ERR') == True:
        plot_object = ax1.errorbar(x,y,yerr=sigma[0],
                ls = 'none',
                markersize = float(cfg['Data Params']['MARK_SIZE']),
                color = cfg['Data Params']['COLOR'],
                capsize = float(cfg['Data Params']['CAP_SIZE']),
                marker = cfg['Data Params']['MARK_TYPE'])

    return(plot_object)



def plot_more(config,x,y, *sigma):
    #First, need to check that x,y,sigma inputs are lists and have same dimensions.

    check_lists = [x,y]

    if all(map(lambda x: isinstance(x, list),check_lists)) == False:
        print("\n All data inputs must be lists of arrays!\n")
        exit()

    #TEST FOR DIMENSIONALITY


    cfg = configparser.ConfigParser()
    cfg.read(config)


    #read in multi-plot configuration
    multi_config = np.genfromtxt(cfg['Multi-Plotting']['MULTI_CONFIG'],delimiter=',',comments='#',dtype=str)


    font = {'family' : cfg['Labels']['FONT'] , 'size' : cfg['Labels']['FONT_SIZE']}
    plt.rc('font', **font)
    fig, ax1 = plt.subplots(1)


    xlims = cfg['Axis Params']['XLIM'].split(',')
    xlims = [float(i) for i in xlims]

    ylims = cfg['Axis Params']['YLIM'].split(',')
    ylims = [float(i) for i in ylims]

    #title or no title
    if cfg['Labels'].getboolean('SET_TITLE') == True:
        ax1.set_title(cfg['Labels']['TITLE'])

    ax1.set_xlim(xlims[0],xlims[1])
    ax1.set_ylim(ylims[0],ylims[1])

    ax1.set_xlabel(cfg['Labels']['ABS_LABEL'])
    ax1.set_ylabel(cfg['Labels']['ORD_LABEL'])

    #Tick handling
    ax1.xaxis.set_ticks_position(cfg['Axis Params']['XTICK_POS'])
    ax1.yaxis.set_ticks_position(cfg['Axis Params']['YTICK_POS'])

    if cfg['Axis Params'].getboolean('XMINOR') == True:
        xwhich = 'both'
        ax1.xaxis.set_minor_locator(AutoMinorLocator(float(cfg['Axis Params']['XMIN_SPACE'])))
    else:
        xwhich = 'major'

    if cfg['Axis Params'].getboolean('YMINOR') == True:
        ywhich = 'both'
        ax1.yaxis.set_minor_locator(AutoMinorLocator(float(cfg['Axis Params']['YMIN_SPACE'])))
    else:
        ywhich = 'major'


    ax1.tick_params(axis='x', which = xwhich, direction = cfg['Axis Params']['XTICK_DIR'])
    ax1.tick_params(axis='y', which = ywhich, direction = cfg['Axis Params']['YTICK_DIR'])


    #Decide Scaling

    if cfg['Axis Params'].getboolean('XLOG') == True:
        ax1.set_xscale('log')

    if cfg['Axis Params'].getboolean('YLOG') == True:
        ax1.set_yscale('log')



    #Loop over data lists and decide the plot type

    for i in range(len(x)):

        if multi_config[i,0] == 'scatter':
            plot_object = ax1.scatter(x[i],y[i],
                    c = multi_config[i,2],
                    s = float(multi_config[i,3]),
                    marker = multi_config[i,4],
                    label=multi_config[i,6])

        elif multi_config[i,0] == 'cont':
            plot_object = ax1.plot(x[i],y[i],
                    color = multi_config[i,2],
                    linewidth = float(multi_config[i,1]),
                    label=multi_config[i,6])

        elif multi_config[i,0] == 'err':
            plot_object = ax1.errorbar(x[i],y[i],yerr=sigma[0],
                    ls = 'none',
                    markersize = float(multi_config[i,3]),
                    color = multi_config[i,2],
                    capsize = float(multi_config[i,5]),
                    marker = multi_config[i,4],
                    label=multi_config[i,6])
        else:
            print(f"\n Invalid plot type: {multi_config[i,0]}\n Must be 'cont','scatter', or 'err'\n")
            exit()

    #Legend

    if cfg['Labels'].getboolean('LEG') == True:
        ax1.legend()



    return(plot_object)



