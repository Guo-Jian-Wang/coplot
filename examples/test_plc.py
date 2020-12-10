import sys
sys.path.append("..")
import coplot.plots as pl
import coplot.plot_contours as plc
import matplotlib.pyplot as plt
import numpy as np


test1 = np.random.randn(50000, 3)
a1, b1, int1 = test1[:,0], test1[:,1], test1[:,2]
test2 = test1 + 1
a2, b2, int2 = test2[:,0], test2[:,1], test2[:,2]



''' the use of plc.Plot_1d '''
# If you want to use some default settings, you can use it like this:
fig = plc.Plot_1d([a1,a2]).plot(labels=[r'$a$', r'$\rm PDF$'], legend=True)
# or
fig = plc.Plot_1d(a1).plot(labels=r'$a$')

# If you want to plot good figures, you should use it like this:
fig = plc.Plot_1d([a1,a2]).plot(labels=[r'$a$', r'$\rm PDF$'],colors=['r','b'],\
line_styles=['-','--'])
# or
fig = plc.Plot_1d([a1,a2]).plot(bins=100,labels=[r'$a$', r'$\rm PDF$'],colors=['r','b'],\
line_styles=['-','--'], smooth=3, ticks_size=None)

# Finally, you can save the figure like this:
#pl.savefig('test_plc_1d.pdf', fig)



''' the use of plc.Plot_2d '''
## If you want to use some default settings, you can use it like this:
fig = plc.Plot_2d([a1,b1]).plot(labels=[r'$a$', r'$b$'], fill_contours=True,\
legend=True, legend_loc='center')
## or
fig = plc.Plot_2d([[a1,b1],[a2,b2]]).plot(labels=[r'$a$', r'$b$'])
## or 
fig = plc.Plot_2d([[a1,b1],[a2,b2]]).plot(labels=[r'$a$', r'$b$'],fill_contours=False)

## If you want to plot good figures, you should use it like this:
fig = plc.Plot_2d([[a1,b1],[a2,b2]]).plot(labels=[r'$a$', r'$b$'],colors=['r','b'],\
line_styles=['-','--'])
## or 
fig = plc.Plot_2d([[a1,b1],[a2,b2]]).plot(bins=100,labels=[r'$a$', r'$b$'],fill_contours=True,\
colors=['r','g'],line_styles=['-','--'], smooth=3, ticks_size=None,\
best_values=[[52.78,1.56],[52.93,1.44]], legend=True, legend_labels=['one','two'])

## Finally, you can save the figure like this:
#pl.savefig('test_plc_2d.pdf', fig)



''' the use of plc.Contours '''
### If you want to use some default settings, you can use it like this:
fig = plc.Contours(test1).plot(labels=[r'$a$', r'$b$', r'$c$'],legend=True)
print( plc.best_params(test1))
## or
fig = plc.Contours([test1,test2]).plot(labels=[r'$a$', r'$b$', r'$c$'])

## If you want to plot good figures, you should use it like this:
fig = plc.Contours([test1,test2]).plot(bins=100,labels=[r'$a$', r'$b$', r'$c$'],\
colors=['r','b'],line_styles=['-','--'])
## or
fig = plc.Contours([test1,test2]).plot(bins=100,labels=[r'$a$', r'$b$', r'$c$'],\
colors=['r','g'],line_styles=['-','--'],fill_contours=True, show_titles=True, smooth=3,\
best_values=[[52.79,1.56,0.40],[52.93,1.44,0.24]], ticks_size=None,legend=True)

## Finally, you can save the figure like this:
#pl.savefig('test_plc_contours.pdf', fig)




plt.show()




