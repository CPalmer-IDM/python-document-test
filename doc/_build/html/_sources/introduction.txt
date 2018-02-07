
.. toctree::
   :maxdepth: 2

Introduction
============

Equations are:

.. math::

    \frac{dS}{dt} &= -\beta S I \\
    \frac{dI}{dt} &= \beta S I - \gamma I


And refer to a paper [author2015]_.


.. [author2015] first a., second a., third a. (2015). The title of their
                paper. Journal of papers, *15*: 1023-1049.

To start do the following

.. code-block:: python

    import model as m
    import numpy as np

    p = m.parameter_set()
    x0 = np.array([0.99,0.01])
    T = 20
    ts,result = m.simulate(p,x0,T=T,dt=0.01)
