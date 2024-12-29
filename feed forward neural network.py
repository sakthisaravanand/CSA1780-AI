import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Generate random training data for binary classification
# Inputs (X) and expected outputs (Y)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

Y = np.array([[0], [1], [1], [0]])  # XOR problem

# Set random seed for reproducibility
np.random.seed(42)

# Initialize weights and biases
input_layer_size = X.shape[1]  # 2 input features
hidden_layer_size = 4         # Arbitrary choice for hidden layer size
output_layer_size = Y.shape[1]  # 1 output for binary classification

# Weights and biases initialization
W1 = np.random.rand(input_layer_size, hidden_layer_size)  # Input to Hidden
b1 = np.random.rand(1, hidden_layer_size)  # Hidden bias

W2 = np.random.rand(hidden_layer_size, output_layer_size)  # Hidden to Output
b2 = np.random.rand(1, output_layer_size)  # Output bias

# Learning rate
learning_rate = 0.1

# Number of iterations (epochs)
epochs = 10000

# Training the neural network
for epoch in range(epochs):
    # Forward propagation
    Z1 = np.dot(X, W1) + b1  # Linear transformation for hidden layer
    A1 = sigmoid(Z1)  # Apply sigmoid activation function

    Z2 = np.dot(A1, W2) + b2  # Linear transformation for output layer
    A2 = sigmoid(Z2)  # Apply sigmoid activation function (output layer)

    # Compute the loss (error)
    loss = np.mean((Y - A2) ** 2)  # Mean Squared Error

    # Backpropagation
    # Output layer error and gradient
    dZ2 = A2 - Y
    dW2 = np.dot(A1.T, dZ2)
    db2 = np.sum(dZ2, axis=0, keepdims=True)

    # Hidden layer error and gradient
    dA1 = np.dot(dZ2, W2.T)
    dZ1 = dA1 * sigmoid_derivative(A1)
    dW1 = np.dot(X.T, dZ1)
    db1 = np.sum(dZ1, axis=0, keepdims=True)

    # Update weights and biases using gradient descent
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    # Print the loss every 1000 iterations
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss}")

# Final predictions
print("Final predictions after training:")
print(A2)
