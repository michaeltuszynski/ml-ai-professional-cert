# Module 22: Neural Networks for Sequential Data Quiz

## Question 1 (1 point)
What is the type of neural network that works best for sequential data?

**Options:**
1. Feed forward neural network (FNN)
2. Generative adversarial network (GAN)
3. Convolutional neural network (CNN)
4. Recurrent neural network (RNN)

**Answer:** Option 4: Recurrent neural network (RNN)

Recurrent neural networks are specifically designed to handle sequential data by maintaining an internal state (memory) that can persist information across time steps. This architecture allows RNNs to capture temporal dependencies in sequential data such as time series, text, speech, and video.

---

## Question 2 (1 point)
Which of the following statements correctly describes the memory structure in a recurrent neural network (RNN)?

**Options:**
1. The memory cell of the network is where weights are stored during training.
2. The total RNN memory content at any point in time is referred to as the activation function.
3. The memory cell of the network holds the input data from the training set.
4. The total RNN memory content at any point in time is called the state of the network.

**Answer:** Option 4: The total RNN memory content at any point in time is called the state of the network.

The state of an RNN encapsulates all information the network has processed up to that point in time. This internal state allows RNNs to maintain context across sequence elements, enabling them to learn patterns in sequential data. The state is updated with each new input in the sequence based on both the current input and the previous state.

---

## Question 3 (1 point)
Which of the following Python statements correctly adds an LSTM input layer with 16 internal units using Keras?

**Options:**
1. `model.add(LSTM(units=16, input_shape=(batch_size, input_dim)))`
2. `model.add(LSTM(16, batch_input_shape=(None, input_dim)))`
3. `model.add(LSTM(16, units=input_dim))`
4. `model.add(LSTM(16, input_shape=(None, input_dim)))`

**Answer:** Option 4: `model.add(LSTM(16, input_shape=(None, input_dim)))`

In Keras, LSTM layers are configured with the number of memory units (16 in this case) as the first parameter. The `input_shape` parameter should specify the shape of input sequences, where `None` indicates variable sequence length and `input_dim` represents the feature dimensionality. This is the correct format for defining an LSTM input layer in Keras.

---

## Answer Key

1. Option 4: Recurrent neural network (RNN) - (Specialized network architecture designed for sequential data)
2. Option 4: The total RNN memory content at any point in time is called the state of the network. - (State maintains context across sequence elements)
3. Option 4: `model.add(LSTM(16, input_shape=(None, input_dim)))` - (Proper Keras syntax for LSTM with variable sequence length)
