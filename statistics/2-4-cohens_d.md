import os
os.chdir('C:\\ds\\metis\\prework\\ThinkStats2\\code\\')

import math

import nsfg
df = nsfg.ReadFemPreg()

def CohenEffectSize(group1, group2):
    diff = group1.mean()-group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1*var1+n2*var2)/(n1+n2)
    d = diff/math.sqrt(pooled_var)
    return d

df_firstborn = (df.loc[df['birthord']==1])

df_notfirstborn = (df.loc[df['birthord']!=1])

df_firstborn["totalwgt_lb"].mean()
df_notfirstborn["totalwgt_lb"].mean()


CohenEffectSize(df_firstborn["totalwgt_lb"], df_notfirstborn["totalwgt_lb"])

#-0.088936411777190513

# The mean weight of first born children is ~.089 SDs less than the mean weight of children born later.  This difference in means is much larger than the difference in means in pregnancy length.
