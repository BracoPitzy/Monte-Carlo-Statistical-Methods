# Monte-Carlo-Statistical-Methods
2024 SCU College of Mathematics - Monte Carlo Statistical Methods Assignments
Textbook: Monte Carlo Statistical Methods (Second Edition) by Christian P. Robert George Casella

## Assignment 1 : Realize Fig. 3.7 (P99) - Estimators $E_f[X^5 \cdot 1_{X\ge 2.1}]$
Consider $X \sim \mathcal{T} (\nu ,\theta ,\sigma ^2)$, $f$ is its p.d.f., take $\nu=0$, $\theta=12$, $\sigma=1$.

Simulate $E_f[X^5 \cdot 1_{X\ge 2.1}]$ with importance sampling distribution: $\mathcal{T} (\nu ,\theta ,\sigma ^2)$ itself, Cauchy instrumental distribution, uniform $U([O, 1/2.1])$ and normal instrumental distribution, respectively.

## Assignment 2 : Realize Fig. 4.5 (P132) - Estimators of $E[\exp(-X^2)]$
Consider $X \sim \mathcal{T} (\nu ,\theta ,\sigma ^2)$, take $(\nu ,\theta ,\sigma )=(4.6,0,1)$.

TheStudent'stdistributioncanbe simulated as a mixture of a normal distribution and of a gamma distribution by Dickey's decomposition (1968),

$$X|y \sim \mathcal{N}(\theta,\sigma^2y) \textit{and} Y^{-1} \sim \mathcal{Ga}(\nu/2, \nu/2) $$.

then the two estimators of $E[exp(-X^2)]$ are given as:

$$\delta_1 = \frac{1}{2}\sum_{j=1}^m \exp(-X_j^2) $$

$$\delta_2=  \frac{1}{2}\sum_{j=1}^m E[\exp(-X^2)|Y_j]= \frac{1}{2}\sum_{j=1}^m \frac{1}{\sqrt{2\sigma^2 Y_j+1}} $$

## Assignment 2 : Realize Fig. 5.4 (P166) - A first simulated annealing maximization for $h(x) = [cos(50x) + sin(20x)]^2$

