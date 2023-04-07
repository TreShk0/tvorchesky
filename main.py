import pandas as pd

table = pd.read_csv('dataset.csv', delimiter=',')
result = table.groupby(['platform', 'event']).size()
result.to_csv('result.csv', sep=',')