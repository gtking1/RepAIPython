import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 40, 12

data = np.loadtxt('10202025636PMData', delimiter=',')
setMarkers = np.loadtxt('10202025636PMSetMarkers', delimiter='\0')
repMarkers = np.loadtxt('10202025636PMRepMarkers', delimiter='\0')
print(len(data))
# print(len(setMarkers))
#data = data.reshape((len(data) // 8, 8))

df = pd.DataFrame(data[0:,0:])
print(len(df))
df.columns = ['Time', 'AccX', 'AccY', 'AccZ', 'GyrX', 'GyrY', 'GyrZ', 'HR']
df['Exercise'] = pd.Series(['Idle'] * len(df))
df.loc[(df.Time >= 237.60957300662994) & (df.Time <= 279.49456095695496), "Exercise"] = 'MachineChestPress'
df.loc[(df.Time >= 637.5524300336838) & (df.Time <= 680.0952860116959), "Exercise"] = 'MachineChestPress'
df.loc[(df.Time >= 943.0562419891357) & (df.Time <= 988.0508450269699), "Exercise"] = 'RopeOverheadTricepsExtension'
df.loc[(df.Time >= 1171.8675060272217) & (df.Time <= 1214.2162539958954), "Exercise"] = 'DumbbellLateralRaise'
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