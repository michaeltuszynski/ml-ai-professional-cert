# Module 7 Quiz 4

## Question 1 (1 point)
Which Python library in SciPy is used for minimization?

**Options:**
1. scipy.stats
2. scipy.interpolate
3. scipy.integrate
4. scipy.optimize

**Answer:** Option 4: scipy.optimize

*Explanation:* The scipy.optimize module is specifically designed for function minimization and optimization tasks. From the course content, we see it being used extensively with `scipy.optimize.minimize()` for finding optimal parameters in machine learning models.

## Question 2 (1 point)
Which of the following statements is correct regarding the shape of a loss function in optimization?

**Options:**
1. The shape of a loss function is irrelevant to both optimization and the selection of a minimum.
2. The shape of a loss function does not affect optimization or the selection of a minimum.
3. The shape of a loss function is critical for optimization and can influence the selection of a minimum.
4. The shape of a loss function only affects the speed of optimization but not the selection of a minimum.

**Answer:** Option 3: The shape of a loss function is critical for optimization and can influence the selection of a minimum.

*Explanation:* The shape of the loss function is crucial as it determines whether we can find a true minimum and affects the optimization process. From the course content, we see that different shapes (like L1 vs L2 loss) can lead to different optimal parameters and affect how numerical methods perform.

## Question 3 (1 point)
Which of the following statements about local minima is correct when using the scipy.optimize module in Python?

**Options:**
1. "scipy.optimize.minimize" ignores local minima and directly finds the global minimum.
2. "scipy.optimize.minimize" is not used for finding minima.
3. "scipy.optimize.minimize" can get stuck in local minima, depending on the starting point and optimization method used.
4. "scipy.optimize.minimize" always finds the global minimum.

**Answer:** Option 3: "scipy.optimize.minimize" can get stuck in local minima, depending on the starting point and optimization method used.

*Explanation:* From the course content, we see that scipy.optimize.minimize can fail and get stuck in local minima based on the starting point. The success of optimization depends on both the function shape and the initial starting point.

---

# Answer Key
1. Option 4 - scipy.optimize (The dedicated minimization library in SciPy)
2. Option 3 - The shape of a loss function is critical (Affects optimization process and minimum selection)
3. Option 3 - Can get stuck in local minima (Depends on starting point and method)