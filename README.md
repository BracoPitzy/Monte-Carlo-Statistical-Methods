# Monte-Carlo-Statistical-Methods
2024 SCU College of Mathematics - Monte Carlo Statistical Methods Assignments

**Textbook:** Monte Carlo Statistical Methods (Second Edition) by Christian P. Robert George Casella

## Assignment 1 : Realize Fig. 3.7 (P99) - Estimators $E_f[X^5 \cdot 1_{X\ge 2.1}]$
Consider $X \sim \mathcal{T} (\nu ,\theta ,\sigma ^2)$, $f$ is its p.d.f., take $\nu=0$, $\theta=12$, $\sigma=1$.

Simulate $E_f[X^5 \cdot 1_{X\ge 2.1}]$ with importance sampling distribution: $\mathcal{T} (\nu ,\theta ,\sigma ^2)$ itself, Cauchy instrumental distribution, uniform $U([O, 1/2.1])$ and normal instrumental distribution, respectively.

![Fig. 3.7](https://github.com/BracoPitzy/Monte-Carlo-Statistical-Methods/blob/main/assignmt_1/Fig3.7.png)

## Assignment 2 : Realize Fig. 4.5 (P132) - Estimators of $E[\exp(-X^2)]$
Consider $X \sim \mathcal{T} (\nu ,\theta ,\sigma ^2)$, take $(\nu ,\theta ,\sigma )=(4.6,0,1)$.

TheStudent'stdistributioncanbe simulated as a mixture of a normal distribution and of a gamma distribution by Dickey's decomposition (1968),

$$X|y \sim \mathcal{N}(\theta,\sigma^2y) \quad \mathrm{and} \quad Y^{-1} \sim \mathcal{Ga}(\nu/2, \nu/2) .$$

Then the two estimators of $E[\exp(-X^2)]$ are given as:

$$\delta_1 = \frac{1}{2}\sum_{j=1}^m \exp(-X_j^2) $$

$$\delta_2=  \frac{1}{2}\sum_{j=1}^m E[\exp(-X^2)|Y_j]= \frac{1}{2}\sum_{j=1}^m \frac{1}{\sqrt{2\sigma^2 Y_j+1}} $$

![Fig. 4.5](https://github.com/BracoPitzy/Monte-Carlo-Statistical-Methods/blob/main/assignmt_2/Fig4.5.png)


## Assignment 3 : Realize Fig. 5.4 (P166) - A first simulated annealing maximization for $h(x) = [\cos(50x) + \sin(20x)]^2$

Calculation of the maximum of the function $h(x) = [\cos(50x) + \sin(20x)]^2 , x \in [0,1]$. Show the trajectory of 2500 pairs $(x_{(t)}, h(x_{(t)})$ for each runs.

![Fig. 5.4](https://github.com/BracoPitzy/Monte-Carlo-Statistical-Methods/blob/main/assignmt_3/Fig5.4.png)

## Assignment 4 : Realize Fig. 7.1 (P280) - Accept- Reject and Metropolis-Hastings Algorithm estimators to $E_f[X^2]$ and $E_f[X^3]$

Using the algorithm of Example 2.19 (see also Example 3.15), an Accept-Reject method can be derived to generate random variables from the $\mathcal{Ga}(\alpha,\beta)$ distribution using a Gamma $\mathcal{Ga}(\left \lfloor a \right \rfloor  ,b)$ candidate (where laJdenotes the integer part of $a$). When $\beta = 1$, the optimal choice of $b$ is
$$b = \frac{\left \lfloor a \right \rfloor }{a}.$$
Here, we take $a=2.43$.

Compare the performance of Accept- Reject and Metropolis-Hastings Algorithm estimators for $E_f[X^2]$ and $E_f[X^3]$.
<p align="center">
  <img src="https://github.com/BracoPitzy/Monte-Carlo-Statistical-Methods/blob/main/assignmt_4/Figure_X%5E2.png" alt="Fig. 7.1" width="80%">
  <img src="https://github.com/BracoPitzy/Monte-Carlo-Statistical-Methods/blob/main/assignmt_4/Figure_X%5E3.png" alt="Fig. 7.2" width="80%">
</p>
<p align="center">

<p align="center">
  Figure 7.1: Estimator performance for $E_f[X^2]$ (up) and $E_f[X^3]$ (below)
</p>


## Assignment 5 : Realize Fig. 8.2 (P325) - 2D slice sampler for truncated normal distribution

First 20 steps of the slice sampler for the truncated normal distribution $\mathcal{N}(3,1)$, restricted to the interval $[0, 1]$.

![Fig. 8.2](https://github.com/BracoPitzy/Monte-Carlo-Statistical-Methods/blob/main/assignmt_5/Fig8.2.png)
