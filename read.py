import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 80, 12

data = np.loadtxt('10212025757PMData', delimiter=',')
setMarkers = np.loadtxt('10212025756PMSetMarkers', delimiter='\0')
repMarkers = np.loadtxt('10212025756PMRepMarkers', delimiter='\0')
print(len(data))
# print(len(setMarkers))
#data = data.reshape((len(data) // 8, 8))

df = pd.DataFrame(data[0:,0:])
print(len(df))
df.columns = ['Time', 'AccX', 'AccY', 'AccZ', 'GyrX', 'GyrY', 'GyrZ', 'HR']
df['Exercise'] = pd.Series(['Idle'] * len(df))
df.loc[(df.Time >= 4.481359004974365) & (df.Time <= 41.07985806465149), "Exercise"] = 'PullUp'
df.loc[(df.Time >= 502.4444980621338) & (df.Time <= 533.6277290582657), "Exercise"] = 'PullUp'
df.loc[(df.Time >= 894.2969930171967) & (df.Time <= 922.568874001503), "Exercise"] = 'PullUp'
df.loc[(df.Time >= 1289.7804629802704) & (df.Time <= 1350.267012000084), "Exercise"] = 'BarbellRow'
df.loc[(df.Time >= 1720.529265999794) & (df.Time <= 1754.6738389730453), "Exercise"] = 'BarbellRow'
df.loc[(df.Time >= 1892.5951030254364) & (df.Time <= 1929.585245013237), "Exercise"] = 'BarbellRow'
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