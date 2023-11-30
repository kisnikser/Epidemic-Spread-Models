import numpy as np


def stochasticSIR(beta, gamma, N, I0):
    t = 0
    S = N - I0
    I = I0
    R = 0

    t_history, S_history, I_history, R_history = [], [], [], []
    while I > 0:
        t_history.append(t)
        S_history.append(S)
        I_history.append(I)
        R_history.append(R)

        a = beta * I * S / N
        b = gamma * I
        p1 = a / (a + b)
        p2 = b / (a + b)
        u1, u2 = np.random.random(), np.random.random()

        t = t - np.log(u1) / (a + b)
        if u2 <= p1:
            S -= 1
            I += 1
        else:
            I -= 1
            R += 1
    
    return np.array(t_history), np.array(S_history), np.array(I_history), np.array(R_history)


        

