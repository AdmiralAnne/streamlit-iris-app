import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# time library seems to be inbuilt so, no 
st.title('💐 Iris Flower Classification')\

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['species'] = df['target'].apply(lambda x: iris.target_names[x])

X = iris.data
y = iris.target
df
X
y


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = SVC()
model.fit(X_train,y_train)

def main():
  st.title("Iris Flower Classifier")

  # User input for flower measurements
  sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0)
  sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0)
  petal_length = st.number_input("Petal Length (cm)", min_value=0.0)
  petal_width = st.number_input("Petal Width (cm)", min_value=0.0)

  # Create a button to predict
  if st.button("Predict"):
    # Create a new data point
    new_data = [[sepal_length, sepal_width, petal_length, petal_width]]

    # Make a prediction
    prediction = model.predict(new_data)[0]

    # Display the predicted species
    st.write(f"Predicted Species: {iris.target_names[prediction]}")

if __name__ == '__main__':
  main()
