import os
os.chdir('C:\\ds\\metis\\prework\\ThinkStats2\\code\\')

import chap01soln
resp = chap01soln.ReadFemResp()

import thinkstats2
pmf = thinkstats2.Pmf(resp.numkdhh)

import thinkplot
thinkplot.Hist(pmf, label='numkdhh')
thinkplot.Show()


def BiasPmf(pmf, label=''):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf

biased = BiasPmf(pmf, label='biased')

thinkplot.PrePlot(2)
thinkplot.PrePlot(2, cols=2)
thinkplot.Hist(pmf, align='right', width=.5)
thinkplot.Hist(biased, align='left', width=.5)
thinkplot.Show()

pmf.Mean()
#1.0242051550438309

biased.Mean()
#2.4036791006642821
