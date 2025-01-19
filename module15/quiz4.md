# Linear Regression Quiz

## Question 1 (1 point)
Consider the following two-dimensional linear regression model:

```
f𝜃(x) = (x)ᵀθ = θ₀x₀ + θ₁x₁
```

What would the squared loss be for the single prediction of a linear regression model provided below?

l(θ,x,yᵢ)

**Options:**
1. (θ₀x₀−θ₁x₁)²
2. (yᵢ−θ₀x₀−θ₁x₁)
3. (yᵢ−θ₀x₀)²
4. (yᵢ−θ₀x₀−θ₁x₁)²

**Answer:** Option 4 - (yᵢ−θ₀x₀−θ₁x₁)²

**Explanation:**
Core Definition: The squared loss function measures the squared difference between the actual value (yᵢ) and the predicted value (f𝜃(x)).

Implementation Details:
- The predicted value is f𝜃(x) = θ₀x₀ + θ₁x₁
- We subtract this prediction from the actual value yᵢ
- The difference is squared to ensure positive values and penalize larger errors more heavily
- Options 1-3 are incorrect because they either miss components or don't square the difference

---

## Question 2 (1 point)
The squared loss function for a two-dimensional regression model is given by:

```
l(θ,x,yᵢ) = (yᵢ−θ₀x₀−θ₁x₁)²
```

What would the gradient formula of this loss function be?

**Options:**
1. [-2(yᵢ−θ₀x₀−θ₁x₁)(x₀)]
2. [-2(yᵢ−θ₀x₀−θ₁x₁)(x₁)−2(yᵢ−θ₀x₀−θ₁x₁)(x₁)]
3. [-2(yᵢ−θ₀x₀−θ₁x₁)(x₀)−2(yᵢ−θ₀x₀−θ₁x₁)(x₁)]
4. [-2(yᵢ−θ₀x₀−θ₁x₁)(x₁)]

**Answer:** Option 3

**Explanation:**
Core Definition: The gradient is a vector of partial derivatives with respect to each parameter (θ₀ and θ₁).

Implementation Details:
- Using the chain rule to differentiate (yᵢ−θ₀x₀−θ₁x₁)²:
  - ∂/∂θ₀: -2(yᵢ−θ₀x₀−θ₁x₁)(x₀)
  - ∂/∂θ₁: -2(yᵢ−θ₀x₀−θ₁x₁)(x₁)
- The gradient combines both partial derivatives into a vector
- Options 1 and 4 are incomplete as they only include one component
- Option 2 incorrectly repeats the θ₁ component

---

## Question 3 (1 point)
The loss function for a two-dimensional linear regression model is defined as:

```
L(θ₁,θ₂) = 1/n ∑ᵢ₌₁ⁿ(yᵢ−(θ₁xᵢ+θ₂))²
```

What is the partial derivative of L with respect to θ₁?

**Options:**
1. −1/n ∑ᵢ₌₁ⁿ(yᵢ−θ₁xᵢ)
2. ∑ᵢ₌₁ⁿ(yᵢ−(θ₁xᵢ+θ₂))
3. 2/n ∑ᵢ₌₁ⁿ(yᵢ−(θ₁xᵢ+θ₂))⋅x₁
4. −2/n ∑ᵢ₌₁ⁿ(yᵢ−(θ₁xᵢ+θ₂))⋅x₁

**Answer:** Option 4

**Explanation:**
Core Definition: The partial derivative measures the rate of change of the loss function with respect to θ₁.

Implementation Details:
- Apply the chain rule to differentiate the squared term
- The 1/n term remains as a coefficient
- The negative sign comes from the negative term inside the squared expression
- The xᵢ term comes from differentiating θ₁xᵢ
- Options 1-3 are incorrect because they either:
  - Miss the factor of 2 from differentiating the square
  - Have the wrong sign
  - Don't include all necessary terms

---

# Answer Key
1. Option 4: (yᵢ−θ₀x₀−θ₁x₁)² - Squared loss between actual and predicted values
2. Option 3: [-2(yᵢ−θ₀x₀−θ₁x₁)(x₀)−2(yᵢ−θ₀x₀−θ₁x₁)(x₁)] - Complete gradient vector
3. Option 4: −2/n ∑ᵢ₌₁ⁿ(yᵢ−(θ₁xᵢ+θ₂))⋅x₁ - Partial derivative with respect to θ₁