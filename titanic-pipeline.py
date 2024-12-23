# In this lab we will focus in data collection and data preparation step.
# It would be based on data ingestion, processing, and visualization.

# %% DATA INGESTION
import pandas as pd

# %%
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df_titanic = pd.read_csv(url)

# %%
df_titanic.info()

# %%
df_titanic

# %% DATA PROCESSING
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# %%
df_titanic = df_titanic[['Survived', 'Pclass', 'Sex','Parch', 'Fare','Age', 'Embarked']]

# %%
df_titanic = df_titanic.dropna(subset=['Survived'])
df_titanic

# %%
X = df_titanic.drop('Survived', axis = 1)
y = df_titanic['Survived']

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# %%
numerical_feature = ['Age', 'Parch', 'Fare']
categorical_feature = ['Pclass', 'Sex', 'Embarked']

# %%
numeric_transformer = Pipeline(
    steps = [
        ('imputer', SimpleImputer(strategy = 'median')),
        ('scaler', StandardScaler())
    ]
)

categorical_transformer = Pipeline(
    steps = [
        ('imputer', SimpleImputer(strategy = 'constant', fill_value = 'missing')),
        ('onehot', OneHotEncoder(handle_unknown = 'ignore'))
    ]
)

preprocessor = ColumnTransformer(
    transformers = [
        ('num', numeric_transformer, numerical_feature),
        ('cat', categorical_transformer, categorical_feature)
    ]
)

# %%
X_train = preprocessor.fit_transform(X_train)
X_test = preprocessor.transform(X_test)

# %% Machine Learning
from sklearn.linear_model import LogisticRegression
import joblib

# %%
model = LogisticRegression(random_state = 42)
model.fit(X_train, y_train)

# %%
joblib.dump(model, 'titanic_logistic_regression_model.joblib')
joblib.dump(preprocessor, 'titanic_preprocessor.joblib')

# %%
accuracy = model.score(X_test, y_test)
print(accuracy)

# %% Visualization
import matplotlib.pyplot as plt
import numpy as np

importance = model.coef_[0]
features = np.array(numerical_feature + list(preprocessor.named_transformers_['cat']['onehot'].get_feature_names_out(categorical_feature)))

plt.figure(figsize=(10, 8))
plt.barh(features, importance)
plt.xlabel('Importance')
plt.title('Feature Importance')
plt.show()