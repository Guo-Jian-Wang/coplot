"""
==========================================================
Triangle plot with multiple data sets by changing settings
==========================================================

Plot good figures with multiple data sets using more settings.
"""
import coplot.plot_contours as plc
import matplotlib.pyplot as plt
import numpy as np


test1 = np.random.randn(50000, 3)
test2 = test1 + 1


# If you want to plot good figures, you should use it like this:
fig = plc.Contours([test1,test2]).plot(bins=150,labels=[r'$a$', r'$b$', r'$c$'],\
colors=['r','g'],line_styles=['-','--'],fill_contours=False, show_titles=True,
smooth=3,best_values=[[0,0,0],[1,1,1]],show_best_value_lines=True, ticks_size=10,
legend=True,legend_labels=['Data 1', 'Data 2'], subplots_adjust=False)
# and you can save the figure like this:
# pl.savefig('test_triangle_3.pdf', fig)
plt.show()