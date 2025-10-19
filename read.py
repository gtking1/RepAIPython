import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 40, 12

data = np.loadtxt('test.txt', delimiter=',')
# setMarkers = np.loadtxt('setMarkers.txt', delimiter=',')
# repMarkers = np.loadtxt('repMarkers.txt', delimiter=',')
print(len(data))
# print(len(setMarkers))
data = data.reshape((len(data) // 8, 8))

df = pd.DataFrame(data[0:,0:])
df.columns = ['Time', 'AccX', 'AccY', 'AccZ', 'GyrX', 'GyrY', 'GyrZ', 'HR']
print(df.head())
print(df.tail())

df.to_csv('test.csv')

def strictly_increasing(L):
    return all(x<y for x, y in zip(L, L[1:]))

print(strictly_increasing(df.Time))

fig, axes = plt.subplots(3)
fig.suptitle('Accelerometer')
axes[0].plot(df.Time, df.AccX, color='red')
#axes[0].vlines(setMarkers, min(df.AccX), max(df.AccX), colors="blue")
axes[0].set_title('X')
axes[1].plot(df.Time, df.AccY, color='blue')
#axes[1].vlines(repMarkers, min(df.AccY), max(df.AccX), colors="red")
axes[1].set_title('Y')
axes[2].plot(df.Time, df.AccZ, color='green')
axes[2].set_title('Z')
fig.tight_layout()
plt.savefig('AccelerometerPlots')

fig, axes = plt.subplots(3)
fig.suptitle('Gyroscope')
axes[0].plot(df.Time, df.GyrX, color='red')
axes[0].set_title('X')
axes[1].plot(df.Time, df.GyrY, color='blue')
axes[1].set_title('Y')
axes[2].plot(df.Time, df.GyrZ, color='green')
axes[2].set_title('Z')
fig.tight_layout()
plt.savefig('GyroscopePlots')

plt.plot(df.HR, color='red')