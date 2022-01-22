#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
#SECTION 1: INTRODUCTION AND BROWNIAN MOTION GENERATION IMPLEMENTATION (WIWNER PROCESS)
print('The purpose of this portion of the project is to implement the well studied Wiener process, a real-valued stochastic '
      'process considered to be synonymous with Brownian motion due to serving as the stochastic (probabilistic) model for '
      'the one-dimensional case of Brownian motion. Note that a random walk is inherently a binomial process but for large '
      'numbers of trials (steps), '
      'this process can be approximated by a normal distribution by the cental limit theorem. '
       'The Wiener process itself is typically generated from a Gaussian/normal distribution, and thus for large values '
       'of the number of steps, the Wiener process can be generated from a random walk model to illustrate Brownian motion.'
       'The mathematical theorem facilitating this is known as the functional central limit theorem.')

def brown_randwalk(step):
    """
    This custom function generates Brownian motion from a random walk process implementation via numpy's random choice feature.
        
    step = Number of steps.
            
    The function returns an array containing Brownian motion data generated from random walk data with the "step" variable's
    number of steps.
    """
    #initializing the arrays corresponding to the conventional basis set of cartesian space
    x = np.ones(step)
    y = np.ones(step)
    z = np.ones(step)
 

    for i in range(1,step):
        # This is the process of creating a lattice random walk where the particle can sometimes move in the increasing or 
        #decreasing direction of the x,y and z unit vectors, or not move whatsoever. (This produces a three-dimensional
        #random lattice walk.)
        yi = np.random.choice([1,0,-1])
        ji = np.random.choice([1,0,-1])
        hi = np.random.choice([1,0,-1])
        # Here, the weiner process is generated from the lattice random walk.
        x[i] = x[i-1]+(yi/np.sqrt(step))
        y[i] = y[i-1]+(ji/np.sqrt(step))
        z[i] = z[i-1]+(hi/np.sqrt(step))

    return x,y,z
#SECTION 2: PLOTTING

#One Dimensional Brownian Motion
plt.figure(figsize=(20, 12))
x,y,z= brown_randwalk(1000)
plt.plot(x)
plt.title('One-dimensional representation of a Brownian motion pattern with 1000 steps.')
plt.xlabel('Number of steps')
plt.ylabel('Position of the particle')
plt.show()


#Two Dimensional Brownian Motion
plt.figure(figsize=(20, 12))
x,y,z = brown_randwalk(1000)
plt.plot(x,y)
plt.title('Two-dimensional representation of a Brownian motion pattern with 1000 steps.')
plt.xlabel('Position of the particle in the x direction')
plt.ylabel('Position of the particle in the y direction')
plt.show()
    
#Three Dimensional Brownian Motion
fig = plt.figure(figsize=(20, 12))
x,y,z = brown_randwalk(1000)
ax = fig.add_subplot(projection='3d')

ax.scatter(x,y,z)

ax.set_xlabel('Position of the particle in the x direction')
ax.set_ylabel('Position of the particle in the y direction')
ax.set_zlabel('Position of the particle in the z direction')

ax.set_title('Three-dimensional representation of a Brownian motion pattern with 1000 steps.')


# In[ ]:




