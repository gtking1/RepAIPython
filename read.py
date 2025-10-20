import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 40, 12

data = np.loadtxt('10192025547PMData', delimiter=',')
setMarkers = np.loadtxt('10192025547PMSetMarkers', delimiter='\0')
repMarkers = np.loadtxt('10192025547PMRepMarkers', delimiter='\0')
print(len(data))
# print(len(setMarkers))
#data = data.reshape((len(data) // 8, 8))

df = pd.DataFrame(data[0:,0:])
print(len(df))
df.columns = ['Time', 'AccX', 'AccY', 'AccZ', 'GyrX', 'GyrY', 'GyrZ', 'HR']
df['Exercise'] = pd.Series(['Idle'] * len(df))
df.loc[(df.Time >= 11.449658989906311) & (df.Time <= 74.87261891365051), "Exercise"] = 'BarbellSquat'
df.loc[(df.Time >= 446.7501759529114) & (df.Time <= 494.95501494407654), "Exercise"] = 'BarbellSquat'
df.loc[(df.Time >= 867.3062160015106) & (df.Time <= 918.1417340040207), "Exercise"] = 'BarbellSquat'
df.loc[(df.Time >= 1584.1057080030441) & (df.Time <= 1624.5065599679947), "Exercise"] = 'SmithMachineCalfRaise'
# df['Exercise'] = pd.Series()
print(df.head())
print(df.tail())

df.to_csv('test.csv')

def strictly_increasing(L):
    return all(x<y for x, y in zip(L, L[1:]))

print(strictly_increasing(df.Time))

fig, axes = plt.subplots(3)
fig.suptitle('Accelerometer')
axes[0].plot(df.Time, df.AccX, color='red')
axes[0].vlines(setMarkers, min(df.AccX), max(df.AccX), colors="blue")
axes[0].set_title('X')
axes[1].plot(df.Time, df.AccY, color='blue')
axes[1].vlines(repMarkers, min(df.AccY), max(df.AccX), colors="red")
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

fig, axes = plt.subplots(1)
fig.suptitle('Heart Rate')
plt.plot(df.Time, df.HR, color='red')
axes.vlines(setMarkers, min(df.HR), max(df.HR), colors="blue")
axes.vlines(repMarkers, min(df.HR), max(df.HR), colors="green")
fig.tight_layout()
plt.savefig('HeartRatePlot')