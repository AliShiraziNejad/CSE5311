import time
import numpy as np
import matplotlib.pyplot as plt


def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x = x + 1
    return x


N_values = list(range(1, 50))
times = []

for n in N_values:
    start = time.time()
    _ = f(n)
    end = time.time()
    times.append(end - start)
    # print(n)

coeffs = np.polyfit(N_values, times, 2)
poly = np.poly1d(coeffs)

N_fine = np.linspace(min(N_values), max(N_values), 300)
times_fitted = poly(N_fine)

plt.figure(figsize=(8, 5))
plt.scatter(N_values, times, color='blue', label='Recorded times')
plt.plot(N_fine, times_fitted, color='red', label='2nd degree polyfit')

plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Runtime of f(n) vs. n')
plt.legend()
plt.grid(True)
plt.show()

print("Fitted polynomial coefficients (a, b, c):", coeffs)
print("Polynomial model:\n", poly)
