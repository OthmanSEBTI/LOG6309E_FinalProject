from pydataset import data
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from Parse_commits_logs import NumberOfMerges
from Parse_commits_logs import NumberOfFailures

d = {'Merges': NumberOfMerges, 'Failures': NumberOfFailures}
df = pd.DataFrame(data=d)
df.plot(kind='scatter', x='Merges', y='Failures')
#plt.plot( NumberOfMerges, NumberOfFailures,)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(df.Merges, df.Failures)
plt.scatter(X_train, y_train, label='Training Data', color='r', alpha=.7)
plt.scatter(X_test, y_test, label='Testing Data', color='g', alpha=.7)
plt.legend()
plt.title("Test train split")
plt.show()

LR = LinearRegression()
LR.fit(X_train.values.reshape(-1, 1), y_train.values)

prediction = LR.predict(X_test.values.reshape(-1, 1))

plt.plot(X_test, prediction, label='Linear Regression', color='b')
plt.scatter(X_test, y_test, label='Actual Test Data', color='g', alpha=.7)
plt.legend()
plt.title("Linear regression and prediction on testing data")
plt.show()

LR.predict(np.array([[1000]]))[0]

print(LR.score(X_test.values.reshape(-1, 1), y_test.values))
