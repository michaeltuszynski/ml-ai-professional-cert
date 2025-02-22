# TensorFlow Neural Networks Quiz

## Question 1 (1 point)
What is the import statement in Python to import the layers library?

**Options:**
1. `from tensorflow.keras import layers`
2. `from layers import keras`
3. `from tensorflow import layers`
4. `from tensorflow import keras`

**Answer:** Option 1: `from tensorflow.keras import layers`

*Explanation:* The correct import statement for accessing Keras layers in TensorFlow is `from tensorflow.keras import layers`. This is the standard way to import the layers module since TensorFlow 2.0, where Keras became the primary API for building neural networks in TensorFlow.

## Question 2 (1 point)
Consider the given Python code:

```python
model = keras.Sequential([
    layers.Dense(3, activation="relu"),
    layers.Dense(4, activiation="relu"),
    layers.Dense(2, activation="relu"),
    layers.Dense(1, activation="sigmoid")
])
```

How many neurons does the third layer have?

**Options:**
1. 4
2. 1
3. 3
4. 2

**Answer:** Option 4: 2

*Explanation:* In a Dense layer, the first parameter specifies the number of neurons (units) in that layer. Looking at the third layer in the sequence: `layers.Dense(2, activation="relu")`, we can see it has 2 neurons.

## Question 3 (1 point)
Which of the following Python statements sets the optimization function as "rmsprop," the loss function as "binary_crossentropy," and the metric as "accuracy"?

**Options:**
1. `model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics="accuracy")`
2. `model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])`
3. `model.compile(optimizer=rmsprop, loss=binary_crossentropy, metrics=[accuracy])`
4. `model(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])`

**Answer:** Option 2: `model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])`

*Explanation:* This is the correct syntax for compiling a Keras model. The `metrics` parameter expects a list of metrics, even for a single metric, hence `["accuracy"]` is the correct format. The string values for optimizer and loss are properly quoted, and the `compile()` method is the correct way to configure the model's training parameters.

---

## Answer Key

1. Option 1: `from tensorflow.keras import layers` (Standard import for TensorFlow 2.x Keras layers)
2. Option 4: 2 (Third Dense layer specifies 2 neurons)
3. Option 2: `model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])` (Correct syntax for model compilation with metrics as a list)