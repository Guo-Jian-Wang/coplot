"""
============================
2D contour with one data set
============================

Plot 2D contour with one data set using some default settings.
"""
import coplot.plot_contours as plc
import matplotlib.pyplot as plt
import numpy as np


test1 = np.random.randn(50000, 2)
a1, b1 = test1[:,0], test1[:,1]

# If you want to use some default settings, you can use it like this:
fig = plc.Plot_2d([a1,b1]).plot(labels=[r'$a$', r'$b$'], legend=True, ticks_size=10)
# and you can save the figure like this:
# pl.savefig('test_2d_1.pdf', fig)
plt.show()