"""
SIR disease model

dS/dt = -beta*S*I/N
dI/dt = beta*S*I/N - gamma*I
dR/dt = gamma*I
"""

import numpy as np
from ODESolver import ForwardEuler

class SIR:
    def __init__(self, beta, gamma, S0, I0, R0):
        """
        beta, gamma: parameters in the ODE system
        S0, I0, R0: initial values
        """

        if isinstance(beta, (float, int)):
            # Is number?
            self.beta = lambda t: beta 
        elif callable(beta):
            self.beta = beta

        if isinstance(gamma, (float, int)):
            self.gamma = lambda t: gamma
        elif callable(gamma):
            self.gamma = gamma

        self.initial_conditions = [S0, I0, R0]
        self.N = S0 + I0 + R0

    def __call__(self, t, u):

        S, I, _ = u

        return np.asarray([
            -self.beta(t)*S*I/self.N, # Susceptibles
            self.beta(t)*S*I/self.N - self.gamma(t)*I, # Infected
            self.gamma(t)*I # Recovered
        ])
