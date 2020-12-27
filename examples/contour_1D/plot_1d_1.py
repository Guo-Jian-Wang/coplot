"""
============================
1D contour with one data set
============================

Plot 1D contour with one data set using some default settings.
"""
import coplot.plot_contours as plc
import coplot.plots as pl
import matplotlib.pyplot as plt
import numpy as np


a1 = np.random.randn(10000)

# If you want to use some default settings, you can use it like this:
fig = plc.Plot_1d(a1).plot(labels=r'$a$', ticks_size=10)
# and you can save the figure like this:
# pl.savefig('test_1d_1.pdf', fig)
plt.show()