import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../sample_data/DatasetObesity.csv')
print(df.shape)
df.head()

print("valeurs manquantes")
print(df.isnull().sum())
print(f"\nTotal:{df.isnull().sum().sum()} valeurs manquantes")