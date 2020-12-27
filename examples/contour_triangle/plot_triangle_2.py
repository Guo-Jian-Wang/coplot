"""
=====================================
Triangle plot with multiple data sets
=====================================

Plot triangle plot with multiple data sets using some default settings.
"""
import coplot.plot_contours as plc
import matplotlib.pyplot as plt
import numpy as np


test1 = np.random.randn(50000, 3)
test2 = test1 + 1


# If you want to use some default settings, you can use it like this:
fig = plc.Contours([test1,test2]).plot(labels=[r'$a$', r'$b$', r'$c$'], legend=True, subplots_adjust=False)
# and you can save the figure like this:
# pl.savefig('test_triangle_2.pdf', fig)
plt.show()