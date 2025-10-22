import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 80, 12

data = np.loadtxt('10212025836PMData', delimiter=',')
setMarkers = np.loadtxt('10212025836PMSetMarkers', delimiter='\0')
repMarkers = np.loadtxt('10212025836PMRepMarkers', delimiter='\0')
print(len(data))
# print(len(setMarkers))
#data = data.reshape((len(data) // 8, 8))

df = pd.DataFrame(data[0:,0:])
print(len(df))
df.columns = ['Time', 'AccX', 'AccY', 'AccZ', 'GyrX', 'GyrY', 'GyrZ', 'HR']
df['Exercise'] = pd.Series(['Idle'] * len(df))
df.loc[(df.Time >= 13.763474941253662) & (df.Time <= 75.24), "Exercise"] = 'CablePullover'
df.loc[(df.Time >= 156.003515958786) & (df.Time <= 191.20), "Exercise"] = 'PreacherCurl'
df.loc[(df.Time >= 249.97008097171783) & (df.Time <= 308.34), "Exercise"] = 'CablePullover'
df.loc[(df.Time >= 362.13921797275543) & (df.Time <= 394.52), "Exercise"] = 'PreacherCurl'
df.loc[(df.Time >= 466.45665895938873) & (df.Time <= 518.26), "Exercise"] = 'CablePullover'
df.loc[(df.Time >= 569.3107579946518) & (df.Time <= 605.73), "Exercise"] = 'PreacherCurl'
df.loc[(df.Time >= 807.5213029384613) & (df.Time <= 853.51), "Exercise"] = 'DumbbellCurl'
df.loc[(df.Time >= 1017.3243778944016) & (df.Time <= 1052.11), "Exercise"] = 'DumbbellCurl'
df.loc[(df.Time >= 1230.5598009824753) & (df.Time <= 1274.55), "Exercise"] = 'DumbbellCurl'
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
axes[0].vlines(repMarkers, min(df.AccY), max(df.AccX), colors="green")
axes[0].set_title('X')
axes[1].plot(df.Time, df.AccY, color='blue')
#axes[1].vlines(setMarkers, min(df.AccY), max(df.AccY), colors="red")
axes[1].set_title('Y')
axes[2].plot(df.Time, df.AccZ, color='green')
#axes[2].vlines(setMarkers, min(df.AccZ), max(df.AccZ), colors="blue")
axes[2].set_title('Z')
fig.tight_layout()
#plt.show()
plt.savefig('AccelerometerPlots')

fig, axes = plt.subplots(3)
fig.suptitle('Gyroscope')
axes[0].plot(df.Time, df.GyrX, color='red')
axes[0].vlines(setMarkers, min(df.GyrX), max(df.GyrX), colors="blue")
axes[0].set_title('X')
axes[1].plot(df.Time, df.GyrY, color='blue')
axes[1].vlines(setMarkers, min(df.GyrY), max(df.GyrY), colors="red")
axes[1].set_title('Y')
axes[2].plot(df.Time, df.GyrZ, color='green')
axes[2].vlines(setMarkers, min(df.GyrZ), max(df.GyrZ), colors="blue")
axes[2].set_title('Z')
fig.tight_layout()
#plt.show()
plt.savefig('GyroscopePlots')

fig, axes = plt.subplots(1)
fig.suptitle('Heart Rate')
plt.plot(df.Time, df.HR, color='red')
#axes.vlines(setMarkers, min(df.HR), max(df.HR), colors="blue")
#axes.vlines(repMarkers, min(df.HR), max(df.HR), colors="green")
fig.tight_layout()
plt.savefig('HeartRatePlot')