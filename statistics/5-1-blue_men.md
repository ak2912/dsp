mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)


low = dist.cdf(177.8)    # 5'10"
high = dist.cdf(185.4)   # 6'1"
low, high, high-low

#Approx 34.2% of the U.S. male population is between 5'10" and 6'1"
