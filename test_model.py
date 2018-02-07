"""
Test
----

Main testing file for model.

"""


import numpy as np
import numpy.testing as npt
import model

p = model.parameter_set(beta=1.0,gamma=0.4)
x0 = np.array([0.99,0.01])
T = 20

ts,result = model.simulate(p,x0,T=T,dt=0.01)


def test_parameters_set():
    """
    Test that parameter set works correctly.

    """
    beta = 0.1
    gamma = 0.2
    p = model.parameter_set(beta=beta,gamma=gamma)

    npt.assert_equal(beta, p['beta'])
    npt.assert_equal(gamma, p['gamma'])

def test_model_size():
    """
    Test that model gives correct dimensional output.
    """

    npt.assert_equal(ts.size,result[:,1].size)

    npt.assert_equal(2,result[0,:].size)



def test_model_output_between_zero_and_one():
    """
    Test that model values between 0 and 1.
    """

    np.testing.assert_array_less(0.0, result)

    np.testing.assert_array_less(result, 1.0)
