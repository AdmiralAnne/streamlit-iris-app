import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# time library seems to be inbuilt so, no 
st.title('💐 Iris Flower Classification')
st.info('A simple ML app for predicting Iris flower classification based on key physical features.')

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['species'] = df['target'].apply(lambda x: iris.target_names[x])

X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = SVC()
model.fit(X_train,y_train)


# User input for flower measurements
sepal_length = st.slider("Sepal Length (cm)", min_value=0.0, max_value=7.0, step=0.2)
sepal_width = st.slider("Sepal Width (cm)", min_value=0.0, max_value=7.0, step=0.2)
petal_length = st.slider("Petal Length (cm)", min_value=0.0, max_value=7.0, step=0.2)
petal_width = st.slider("Petal Width (cm)", min_value=0.0, max_value=7.0, step=0.2)

# Create a button to predict
if st.button("Predict"):
    # Create a new data point
    new_data = [[sepal_length, sepal_width, petal_length, petal_width]]

    #Make a prediction
    prediction = model.predict(new_data)[0]

    # Display the predicted species
    st.text("**Predicted Species**")
    st.success(f"{iris.target_names[prediction]}")