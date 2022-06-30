# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import AutoMinorLocator


#to be improved
class PlotSettings:
    def __init__(self, set_fig=False, figsize=(6*1.05, 4.5*1.05)):
        #move parameters to here
        if set_fig:
            self.fig = plt.figure(figsize=figsize)
    
    def set_label(self):
        pass
    
    def set_locator(self):
        pass
    
    def set_size(self):
        pass
    
    def set_tick(self):
        pass
    
    def setting(self, ax=None, location=None,lims=None,set_labels=True,labels=None,ticks_size=12,
                rotation=None,major_locator_N=None,major_locator_length=None,
                minor_locator=True,minor_locator_N=None,show_xticks=True,show_yticks=True,
                show_xticklabels=True,show_yticklabels=True,show_xlabel=True,
                show_ylabel=True, old_ticksStyle=False,rightTopTicks=True):
        ''' 
        Set the attribute of panels.
        
        :param lims: [min_x, max_x, min_y, max_y], where min_* or max_* is a real number or None
        :param labels: the label of a panel
        :param ticks_size: the font size of ticks
        :param rotation: the rotation of the label of ticks
        :param major_locator_N: the number of major locators
        :param minor_locator: if the minor_locator is True(False), show(don't show) the minor locators
        :param minor_locator_N: the number of minor locators
        :param show_xticks: if show_xticks is True(False), show(don't show) ticks of X axis
        :param show_yticks: if show_yticks is True(False), show(don't show) ticks of Y axis
        :param show_xticklabels: if True(False), show(don't show) the labels of ticks of X axis
        :param show_yticklabels: if True(False), show(don't show) the labels of ticks of Y axis
        :param show_xlabel: if True(False), show(don't show) the labels of X axis
        :param show_ylabel: if True(False), show(don't show) the labels of Y axis
        '''
        
        if location is None:
            location = (1,1,1)
        if ax is None:
            self.ax = plt.subplot(location[0],location[1],location[2])
        else:
            self.ax = ax
        
        if lims is not None:
            min_x, max_x, min_y, max_y = lims[0], lims[1], lims[2], lims[3]
            if min_x is not None and max_x is not None:
                self.ax.set_xlim(min_x, max_x)
            if min_y is not None and max_y is not None:
                self.ax.set_ylim(min_y, max_y)
        
        # set ticks
        if major_locator_length is None:
            major_locator_length = 5.5
        minor_locator_length = major_locator_length*0.5 #618
        self.ax.tick_params(which='major', length=major_locator_length, width= 0.5, color='k')
        self.ax.tick_params(which='minor', length=minor_locator_length, width= 0.5, color='k')
        
        if major_locator_N is None:
            major_locator_N = 6.0
        if minor_locator_N is None:
            minor_locator_N = 10.0
        
        if old_ticksStyle:
            if rightTopTicks:
                self.ax.axes.tick_params(axis='both',which='both',direction='in',right=True,top=True)
            else:
                self.ax.axes.tick_params(axis='both',which='both',direction='in',right=False,top=False)
        
        if show_xticks is True:
            if minor_locator is True:
                self.ax.xaxis.set_major_locator( MaxNLocator(major_locator_N) )
                self.ax.xaxis.set_minor_locator( AutoMinorLocator(minor_locator_N) )
            else:
                self.ax.xaxis.set_major_locator( MaxNLocator(major_locator_N) )
        else:
            self.ax.set_xticks([])
        if show_yticks is True:
            if minor_locator is True:
                self.ax.yaxis.set_major_locator( MaxNLocator(major_locator_N) )
                self.ax.yaxis.set_minor_locator( AutoMinorLocator(minor_locator_N) )
            else:
                self.ax.yaxis.set_major_locator( MaxNLocator(major_locator_N) )
        else:
            self.ax.set_yticks([])
        
        # set ticks label
        if ticks_size is None:
            self.ticks_size = 12
        else:
            self.ticks_size = ticks_size
        if rotation is None:
            rotation = 0
        if show_xticklabels is True:
            self.ax.tick_params(axis='both', which='major', labelsize=ticks_size)
            for tick in self.ax.xaxis.get_major_ticks():
                tick.label.set_rotation(rotation)
        else:
            self.ax.set_xticklabels([])
        if show_yticklabels is True:
            self.ax.tick_params(axis='both', which='major', labelsize=ticks_size)
            for tick in self.ax.yaxis.get_major_ticks():
                tick.label.set_rotation(rotation)
        else:
            self.ax.set_yticklabels([])

        # set labels
        if set_labels:
            # labels_size = ticks_size/0.618
            labels_size = ticks_size * 1.55
            if labels is None:
                labels = [r'$x$',r'$y$']
            if show_xlabel is True:
                self.ax.set_xlabel(r'%s'%labels[0], fontsize=labels_size)
            if show_ylabel is True:
                self.ax.set_ylabel(r'%s'%labels[1], fontsize=labels_size)
        return self.ax
    
    def set_legend(self, legend_size=None):
        if legend_size is None:
            legend_size = self.ticks_size * 1.20833
        self.ax.legend(fontsize=legend_size)

