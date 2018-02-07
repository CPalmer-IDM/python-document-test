"""
Model
-----

Python module for an example epidemiological model

Routine Listings
----------------

1. left_hand_side: function
2. euler_step: function
3. simulate: function
4. parameter_set: function
"""

# load libraries
import numpy as np

def left_hand_side(x,p,t):
    """
    Left-hand side of ODE equation

    Parameters
    ----------
        x : array
            current state
        p : dictionary
            parameters
        t : float
            current time

    Returns
    -------
    dx : array
        derivative of x wrt t
    """
    S,I = x[0],x[1]
    dS = -p['beta']*S*I
    dI = p['beta']*S*I - p['gamma']*I

    # return result as an array
    return np.array([dS,dI])

def euler_step(x,p,t,dt):
    """
    Euler step method for solving ODE.

    https://en.wikipedia.org/wiki/Euler_method

    Parameters
    ----------
        x : array
            current state
        p : dictionary
            parameters
        t : float
            current time
        dt : float
            step-size

    Returns
    -------
    array
        state at time t + dt
    """
    dx = left_hand_side(x,p,t)
    return x + dt*dx

def simulate(p,x0,T=10,dt=0.1):
    """
    Solve ODE with initial values x0 up until time T.

    Example
    -------

    >>> import model as m
    >>> import numpy as np
    >>> p = m.parameter_set()
    >>> x0 = np.array([0.99,0.01])
    >>> T = 20
    >>> ts,result = m.simulate(p,x0,T=T,dt=0.01)


    Parameters
    ----------

        p : dictionary
            parameters
        x0 : array
            initial state
        T : float
            final time to simulate until
        dt : float
            step-size

    Returns
    -------
    ts : array
        time-points for simulation
    array
        result of simulation
    """

    # get array of times to simulate at.
    ts = np.arange(0,T,dt)

    #initialise results list
    results = []
    x = x0
    for t in ts:
        x = euler_step(x,p,t,dt)
        results.append(x)

    return ts,np.array(results)

def parameter_set(beta=1.0,gamma=0.1):
    """
    Create parameter dictionary from list of parameters

    Parameters
    ----------
    beta : float
        infectivity

    gamma : float
        recovery rate

    Returns
    -------
    dictionary
        dictionary of parameters

    """

    return {'beta':beta,'gamma':gamma}
