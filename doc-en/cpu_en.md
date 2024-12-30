**cpu.md** -> **cpu_en.md**.

---

# Using the CPU for Artificial Intelligence and Machine Learning

## Introduction
This guide provides examples of how to use the CPU for machine learning tasks in Python. The examples include the use of libraries such as Scikit-learn for supervised learning and TensorFlow for neural networks.

---

## Practical Examples

### 1. Classification with Scikit-learn
In this example, we use the CPU to train a classification model with Scikit-learn.

#### Code:
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset
data = load_iris()
X, y = data.data, data.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
```

#### Explanation:
- We load the Iris dataset.
- Split the data into training and testing sets.
- Train a Random Forest classifier.
- Evaluate the model's performance using the accuracy metric.

---

### 2. Neural Networks with TensorFlow and CPU
In this example, we create and train a neural network for digit classification using TensorFlow.

#### Code:
```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the data
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=32)

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {accuracy:.2f}")
```

#### Explanation:
- We use TensorFlow to create a dense neural network.
- Load and normalize the MNIST dataset.
- Train the model for 5 epochs and evaluate its performance.

---

## Configuration for CPU
By default, both Scikit-learn and TensorFlow use the CPU. Ensure your TensorFlow installation is correctly configured for CPU. To check:

```python
import tensorflow as tf
print("Available devices:", tf.config.list_physical_devices('CPU'))
```

---

These examples demonstrate how to efficiently use the CPU for machine learning.
