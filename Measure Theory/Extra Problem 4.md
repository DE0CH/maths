To simplify the proof, we first prove the following.

Lemma 1. Let $f \in \mathcal{M}^+(X, \mathcal{E})$ and $\int f\; d\mu < \infty$, and $(\phi_n)_n$ be a sequence of monotonically increasing simple functions that converges to $f$ pointwise (the construction used in Lemma 3.4 in the lecture notes works). By M.C.T, $\lim_{n \rightarrow \infty} \int \phi_n \; d\mu = \int f \; d\mu$. For all $\epsilon > 0$, let $N$ be such that for all $n \geq N$, $|\int \phi_n \; d\mu - \int f \; d\mu| \leq \epsilon / 2$ and let $\delta = \frac{\epsilon/2}{\sup_{x\in X}\phi_N(x)}$ (we will shorten $\sup_{x\in X}\phi_N(x)$ to $sup \phi_N$). Since $\phi_N$ is simple, the supremum exists and is finite. Then if $E \in \mathcal{E}$ and $\mu(E) \leq \delta$, then $|\int f \chi_E \; d\mu| \leq \epsilon$.

Proof. First $$\left| \int \phi_N \; d\mu - \int f \; d\mu \right| = \int f \; d\mu - \int \phi_N \; d\mu$$ (1.1) since $\phi_N \leq f$ and by monoticity of the integral. 

Second $$\int \sup \; \phi_N \chi_E \; d\mu \geq \int \phi_N \chi_E \; d\mu$$ (1.2) for all $E\in\mathcal{E}$ by monoticity of the integral.

Now we are ready to prove the lemma. 

For all $E \in \mathcal{E}$ such that $\mu(E) \leq \delta$

$$
\begin{aligned}
& \left| \int f \chi_E \; d\mu \right| \\
=& \int f \chi_E\; d\mu & (\text{as} f \geq 0) \\
=& \int (f - \phi_N+ \phi_N) \chi_E \; d\mu \\
=& \int (f - \phi_N) \chi_N \; d\mu + \int \phi_N \chi_E \; d\mu & (\text{by linearity}) \\
\leq & \int(f - \phi_N) \; d\mu + \int \phi_N \chi_E\; d\mu & (\text{by monoticity}) \\
\leq & \left| \int \phi_N \; d\mu - \int f \; d\mu \right| + \int \phi_N \chi_E \; d\mu & (\text{by (1.1)}) \\
\leq & \; \epsilon / 2 + \int \sup \phi_N \chi_E \; d\mu & (\text{by definition of $\phi_N$ and (1.2)}) \\ 
= &\; \epsilon / 2+ \sup \phi_N \mu(E) & (\text{by definition of the integral}) \\
\leq & \; \epsilon / 2 + \sup \phi_N \delta \\
= & \; \epsilon/2 + \sup \phi_N \frac{\epsilon/2}{\sup \phi_N} & (\text{substitute}\; \delta = \frac{\epsilon/2}{\sup \phi_N})\\
= & \; \epsilon
\end{aligned}
$$

Q.E.D

Now for $f \in \mathcal{L}(X, \mathcal{E}, \mu)$, we see by definition $f = f^+ - f^-$ where $\int f^+ \; d\mu < \infty$ and $\int f^- \; d\mu < \infty$. So for any $\epsilon > 0$, let $\delta_1$ be such that if $E \in \mathcal{E}$ and $\mu(E) \leq \delta_1$ then $\left| \int f^+ \chi_E \; d\mu \right| \leq \epsilon / 2$ and let $\delta_2$ be such that if $E \in \mathcal{E}$ and $\mu(E) \leq \delta_2$ then $\left| \int f^- \chi_E \; d\mu \right| \leq \epsilon/2$, and let $\delta = \min(\delta_1, delta_2)$. We then observe that for all $E \in \mathcal{E}$ such that $\mu(E) \leq \delta$, 
$$
\begin{aligned}
& \left| \int f \chi_E \; d\mu \right| \\
= & \left| \int (f^+ - f^-) \chi_E \; d\mu \right| \\
\leq & \left| \int f^+ \chi_E \; d\mu \right| + \left| \int f^- \chi_E \; d\mu \right| & (\text{by linearity of the integral and triangle inequality}) \\
\leq & \; \epsilon
\end{aligned}
$$.
