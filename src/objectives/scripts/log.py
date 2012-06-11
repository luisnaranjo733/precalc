"""from pylab import *

t = arange(0.0, 8.0, 0.5)
s = log(t)/log(2.0)

plot(t, s, linewidth=1.0)

xlabel('x')
ylabel('y')
title('y = log(x)/log(2)')
grid(True)
show()

print s"""


from pylab import *

t = arange(0.0, 2.0, 0.01)
s = sin(2*pi*t)
plot(t, s, linewidth=1.0)

xlabel('time (s)')
ylabel('voltage (mV)')
title('About as simple as it gets, folks')
grid(True)
show()
