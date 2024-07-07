import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

result = {}
column_names = []

for i in lst:
  if not i in column_names:
    column_names.append(i)

for c in column_names:
  column_values = []
  for i in lst:
    if i == c:
      column_values.append(1)
    else:
      column_values.append(0)

  result[c] = column_values

print(pd.DataFrame(result))