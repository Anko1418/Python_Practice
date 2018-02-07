# np_baseball is available

# Import numpy
import numpy as np

np_baseball = np.array([[74., 180., 22.99],
                        [74., 215., 34.69],
                        [72., 210., 30.78],
                        [75., 205., 25.19],
                        [75., 190., 31.01],
                        [73., 195., 27.92]])

# Print mean height (first column)
avg = np.mean(np_baseball[:, 0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:, 0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("Correlation: " + str(corr))
