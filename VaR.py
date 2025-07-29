#!/usr/bin/env python
# coding: utf-8

# In[52]:


#Made by Ayandeep Sadhukhan,FRM(Part 1 cleared),contact detail: ayndeepsadhukhan15@gmail.com

print("Historical VaR calculation:")

import numpy as np

returns = [-0.02, 0.01, -0.015, 0.02, -0.025, 0.005, -0.01, 0.03, -0.005, 0.015]
alpha = 0.05  # 95% confidence level

VaR = np.percentile(returns, alpha * 100)
print("VaR (95% confidence):", VaR)


# Plot histogram
plt.figure(figsize=(10, 5))
plt.hist(simulated_returns, bins=50, color='skyblue', edgecolor='black', alpha=1)

# Add VaR line (5th percentile)
plt.axvline(VaR, color='red', linestyle='dashdot', linewidth=2, label="5% VaR")

plt.xlabel('Simulated Returns')
plt.ylabel('Frequency')
plt.title('Monte Carlo Simulated Returns Distribution')

plt.legend()
plt.show()


# In[50]:


print("Parametric Method VaR")

import scipy.stats as stats

mu = 0.001  # Expected return (0.1%)
sigma = 0.02  # Standard deviation (2%)
alpha = 0.05  # 95% confidence level
z = stats.norm.ppf(1 - alpha)

VaR = mu - z * sigma
print("VaR (95% confidence): ", VaR)


# Plot histogram
plt.figure(figsize=(10, 5))
plt.hist(simulated_returns, bins=50, color='skyblue', edgecolor='black', alpha=1)

# Add VaR line (5th percentile)
plt.axvline(VaR, color='red', linestyle='dashdot', linewidth=2, label="5% VaR")

plt.xlabel('Simulated Returns')
plt.ylabel('Frequency')
plt.title('Monte Carlo Simulated Returns Distribution')

plt.legend()
plt.show()



# In[48]:


import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)
mu = 0.001  # Expected return (0.1%)
sigma = 0.02  # Standard deviation (2%)
alpha = 0.05  # 95% confidence level

simulated_returns = np.random.normal(mu, sigma, 10000)  # Simulated returns
VaR = np.percentile(simulated_returns, alpha * 100) # at 5% threshold 

print("Monte Carlo VaR (95% confidence): ", VaR)


# Plot histogram
plt.figure(figsize=(10, 5))
plt.hist(simulated_returns, bins=50, color='skyblue', edgecolor='black', alpha=1)

# Add VaR line (5th percentile)
plt.axvline(VaR, color='red', linestyle='dashdot', linewidth=2, label="5% VaR")

plt.xlabel('Simulated Returns')
plt.ylabel('Frequency')
plt.title('Monte Carlo Simulated Returns Distribution')

plt.legend()
plt.show()





# In[ ]:





# In[ ]:




