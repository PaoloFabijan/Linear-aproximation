# author: Paolo Fabijan

import numpy as np
import matplotlib.pyplot as plt 

freq = 100
time_step = 1/freq

t_start = 0
t_end = 5
N = 2000
dt = t_end/N

data = np.genfromtxt("test10.csv", delimiter = ",", missing_values = None, filling_values = 0.0)
A = np.reshape(data, (len(data), len(data[0])))

if time_step % dt == 0:
    n = np.floor(time_step/dt)-1
    B = []
    for i in range(1, len(A)-1, 1):
        for j in range(1, int(n)+1, 1):
            B.append(np.array([A[i, 0]+j*dt, 0, 0, 0, 0, 0]))
    B = np.asarray(B)

    C = np.zeros(((len(A)+len(B)), len(A[0])), float)

    range_B = np.arange(0, len(B), 1) # Indeksi u matrici B, vremena t+n*dt
    range_3 = np.arange(0, len(C)-1, int(n+1)) # Indeksi postojećih podataka iz matrice A koji su ubačeni u matricu C (matrica C)
    range_A = np.arange(0, len(A), 1) # Indeksi u matrici A, postojeći podaci
    range_1 = np.arange(0, len(C)-1, 1)
    range_1 = np.delete(range_1, range_3)

    for i, j in zip(range_1, range_B):
        C[i,:] = B[j,:]
    for k, t in zip(range_3, range_A):
        C[k,:] = A[t,:]
        C[len(C)-1,:] = A[len(A)-1,:]

    range_5 = np.repeat(range_3, int(n))
    for col in range(1, len(C[0]), 1):
        for row, arr in zip(range_1, range_5):
            C[row, col] = C[arr, col] + (C[arr+int(n+1), col] - C[arr, col]) * ((C[row, 0]-C[arr, 0])/(C[arr+int(n+1), 0]-C[arr, 0]))   

else:
    n = np.floor(time_step/dt) # Broj dodanih vremenskih koraka između dva postojeća vremena
    B = []
    for i in range(0, len(A)-1, 1):
        for j in range(1, int(n)+1, 1):
            B.append(np.array([A[i, 0]+j*dt, 0, 0]))
    B = np.asarray(B)

    C = np.zeros(((len(A)+len(B)), len(A[0])), float)

    range_B = np.arange(0, len(B), 1) # Indeksi u matrici B, vremena t+n*dt
    range_3 = np.arange(0, len(C)-1, int(n)+1) # Indeksi postojećih podataka iz matrice A koji su ubačeni u matricu C (matrica C)
    range_A = np.arange(0, len(A), 1) # Indeksi u matrici A, postojeći podaci
    range_1 = np.arange(0, len(C)-1, 1)
    range_1 = np.delete(range_1, range_3)

    for i, j in zip(range_1, range_B):
        C[i,:] = B[j,:]
    for k, t in zip(range_3, range_A):
        C[k,:] = A[t,:]
        C[len(C)-1,:] = A[len(A)-1,:]

    range_5 = np.repeat(range_3, int(n))
    for col in range(1, len(C[0]), 1):
        for row, arr in zip(range_1, range_5):
            C[row, col] = C[arr, col] + (C[arr+(int(n)+1), col] - C[arr, col]) * ((C[row, 0]-C[arr, 0])/(C[arr+(int(n)+1), 0]-C[arr, 0]))


plt.plot(C[:,0], C[:,1], 'bo')
plt.plot(data[:,0], data[:,1], 'r+')
plt.xlim([102.6,102.8])
plt.show()

# np.savetxt('data.csv', C, delimiter=',')