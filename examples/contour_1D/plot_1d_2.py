"""
==================================
1D contour with multiple data sets
==================================

Plot 1D contour with multiple data sets using some default settings.
"""
import coplot.plot_contours as plc
import coplot.plots as pl
import matplotlib.pyplot as plt
import numpy as np


a1 = np.random.randn(10000)
a2 = a1 + 1

# If you want to use some default settings, you can use it like this:
fig = plc.Plot_1d([a1,a2]).plot(labels=[r'$a$', r'$\rm PDF$'], legend=True, ticks_size=10)
# and you can save the figure like this:
# pl.savefig('test_1d_2.pdf', fig)
plt.show()