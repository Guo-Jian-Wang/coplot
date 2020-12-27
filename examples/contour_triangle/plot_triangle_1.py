"""
===============================
Triangle plot with one data set
===============================

Plot triangle plot with one data set using some default settings.
"""
import coplot.plot_contours as plc
import matplotlib.pyplot as plt
import numpy as np


test1 = np.random.randn(50000, 3)


# If you want to use some default settings, you can use it like this:
fig = plc.Contours(test1).plot(labels=[r'$a$', r'$b$', r'$c$'], legend=True, subplots_adjust=False)
# and you can save the figure like this:
# pl.savefig('test_triangle_1.pdf', fig)
plt.show()