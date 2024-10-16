import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Initialize weights
def initialize_weights(input_size, hidden_size, output_size):
    np.random.seed(1)  # To make the random numbers deterministic
    weights_input_hidden = np.random.rand(input_size, hidden_size)
    weights_hidden_output = np.random.rand(hidden_size, output_size)
    return weights_input_hidden, weights_hidden_output

# Feedforward step
def feedforward(X, weights_input_hidden, weights_hidden_output):
    # Input to hidden layer
    hidden_input = np.dot(X, weights_input_hidden)
    hidden_output = sigmoid(hidden_input)
    
    # Hidden layer to output
    final_input = np.dot(hidden_output, weights_hidden_output)
    final_output = sigmoid(final_input)
    
    return hidden_output, final_output

# Backpropagation and weight updates
def backpropagate(X, y, hidden_output, final_output, weights_input_hidden, weights_hidden_output, learning_rate):
    # Calculate output layer error
    output_error = y - final_output
    output_delta = output_error * sigmoid_derivative(final_output)
    
    # Calculate hidden layer error
    hidden_error = output_delta.dot(weights_hidden_output.T)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_output)
    
    # Update weights
    weights_hidden_output += hidden_output.T.dot(output_delta) * learning_rate
    weights_input_hidden += X.T.dot(hidden_delta) * learning_rate
    
    return weights_input_hidden, weights_hidden_output

# Training the neural network
def train(X, y, input_size, hidden_size, output_size, epochs=10000, learning_rate=0.5):
    # Initialize weights
    weights_input_hidden, weights_hidden_output = initialize_weights(input_size, hidden_size, output_size)
    
    # Training loop
    for epoch in range(epochs):
        # Feedforward
        hidden_output, final_output = feedforward(X, weights_input_hidden, weights_hidden_output)
        
        # Backpropagate
        weights_input_hidden, weights_hidden_output = backpropagate(
            X, y, hidden_output, final_output, weights_input_hidden, weights_hidden_output, learning_rate)
        
    return weights_input_hidden, weights_hidden_output

# Prediction
def predict(X, weights_input_hidden, weights_hidden_output):
    _, final_output = feedforward(X, weights_input_hidden, weights_hidden_output)
    return final_output

# Example dataset: XOR problem
X = np.array([[0,0], [0,1], [1,0], [1,1]])  # XOR input
y = np.array([[0], [1], [1], [0]])  # XOR output

# Define network structure
input_size = 2
hidden_size = 2
output_size = 1

# Train the neural network
weights_input_hidden, weights_hidden_output = train(X, y, input_size, hidden_size, output_size)

# Test the network
test_data = np.array([[0,0], [0,1], [1,0], [1,1]])
predictions = predict(test_data, weights_input_hidden, weights_hidden_output)

print("Predictions for XOR test data:")
print(predictions)
