# In this lab we will focus in data collection and data preparation step.
# It would be based on data ingestion, processing, and visualization.

# %%
import pandas as pd

# %% DATA INGESTION
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df_titanic = pd.read_csv(url)

# %% DATA PROCESSING
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# %%
df_titanic = df_titanic[['Survived', 'Pclass', 'Sex','Parch', 'Fare','Age', 'Embarked']]


# %%
df_titanic = df_titanic.dropna(subset=['Survived'])

# %%
