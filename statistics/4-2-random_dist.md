import thinkstats2
import thinkplot

import random
t = [random.random() for _ in range(1000)]
pmf = thinkstats2.Pmf(t)
thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.Show()

cdf = thinkstats2.Cdf(t)
thinkplot.Cdf(cdf)
thinkplot.Show()


#The CDF is easier to read - Basically a straight line between (0,0) and (1,1).  If you take much fewer draws - let's say 10 - the resulting CDF resembles an uneven jagged line.
