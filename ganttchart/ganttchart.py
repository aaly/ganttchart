#!/bin/env python

__author__ = "A.Aly Saad"
__license__ = "Whatever"
__version__ = "0.2 beta"

import time
import datetime
import matplotlib.pyplot
import matplotlib.patches

class ganttchart:
    matplotlib.pyplot.rcdefaults()
    fig,ax = matplotlib.pyplot.subplots()
    barHeight = 0.3
    yLabels = []
    xLabels = []
    xticks = []
    xticksMap = []
    roundValue=2
    bars = []
    legends = []

    def getTimeStr(self, tick: float):
        milliseconds = (tick - int(tick))
        tickStr = time.strftime("%H:%M:%S", time.localtime(tick))
        tickStr = tickStr + "." + str(round (milliseconds, self.roundValue)).split('.')[1]
        return tickStr

    def addTask(self, name, start: float, end: float, resource, color):
        _end    = round(end, self.roundValue)
        _start = round(start, self.roundValue)

        bar = [name, _start, _end, resource, color]
        if bar not in self.bars:
            self.bars.append(bar)
            if name not in self.yLabels:
                self.yLabels.append(name)
            
            if _start not in self.xticksMap:
                self.xticksMap.append(_start)

            if _end not in self.xticksMap:
                self.xticksMap.append(_end)

        if [resource, color] not in self.legends:
            self.legends.append([resource, color])

    def show(self, title):
        self.xticksMap.sort()
        for item in self.xticksMap:
            self.xticks.append(len(self.xticks))
            tickStr = self.getTimeStr(item)
            if tickStr not in self.xLabels:
                self.xLabels.append(tickStr)

        for bar in self.bars:
            self.ax.barh(bar[0],  self.xticksMap.index(bar[2])-self.xticksMap.index(bar[1]), height=self.barHeight, left=self.xticksMap.index(bar[1]),align='center',color=bar[4], ecolor='black')
            
        self.ax.set_xticks(self.xticks)
        self.ax.set_xticklabels(self.xLabels)
        self.ax.set_yticklabels(self.yLabels)
        self.ax.invert_yaxis()  # labels read top-to-bottom
        self.ax.set_xlabel('Time')  
        self.ax.set_title(title)

        #for legend in self.legends:
        plotLegends = []
        for legend in self.legends:
            plotLegends.append(matplotlib.patches.Patch(color=legend[1], label=legend[0]))
        
        matplotlib.pyplot.legend(handles=plotLegends)

        matplotlib.pyplot.show()
