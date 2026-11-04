# An exact certificate for the known mismatch failure

This note illustrates a limitation already identified by Duncan, Nüsken and Pavliotis (2017, Remark 5, Figure 1b and Remark 9). It is not claimed as a new variance-reduction phenomenon.

In two dimensions, let $J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}$, $k,\gamma>0$, and consider

$$
dq=(p-\mu kJq)dt,\qquad
dp=(-kq-\gamma p-\mu Jp)dt+\sqrt{2\gamma}\,dW.
$$

Its stationary covariance is $\operatorname{diag}(k^{-1}I_2,I_2)$. The target is preserved even when the position and momentum rotations have different speeds. For the centred radial observable $f(q)=k|q|^2-2$, its full long-run variance is exactly

$$
V_f(\mu)=\frac4\gamma+\frac{4\gamma}{k}
          +\frac{4\mu^2(1-k)^2}{k\gamma}.
$$

Thus any nonzero scalar precision mismatch in this specified implementation destroys universal global variance reduction. The example does not assert that every kind of approximation or every observable suffers this failure.

## Direct Poisson-equation proof

The rotating frame $x=e^{\mu ktJ}q$, $y=e^{\mu ktJ}p$ preserves the radial observable and gives

$$
dx=y\,dt,\qquad
dy=(-kx-\gamma y-\delta Jy)dt+\sqrt{2\gamma}\,d\widetilde W,
\qquad \delta=\mu(1-k).
$$

Define the four centred quadratic functions

$$
A=k|x|^2-2,\quad B=|y|^2-2,\quad C=x\cdot y,\quad D=x\cdot Jy.
$$

Their generator identities are

$$
LA=2kC,\quad LB=-2kC-2\gamma B,\quad
LC=B-A-\gamma C-\delta D,\quad LD=\delta C-\gamma D.
$$

Therefore $-Lh=A$ for

$$
h=\left(\frac1{2\gamma}+\frac\gamma{2k}
        +\frac{\delta^2}{2k\gamma}\right)A
  +\frac{B}{2\gamma}+C-\frac\delta\gamma D.
$$

Under the stationary Gaussian law, $A$ is orthogonal to $B,C,D$ and $\mathbb E A^2=4$. Hence $V_f=2\langle A,h\rangle$ gives the displayed formula. The independent Lyapunov checks in `../code/verify_matrix_extension.py` include this identity at several precisions and amplitudes.

## Source

Duncan, A. B., Nüsken, N., & Pavliotis, G. A. (2017). Using perturbed underdamped Langevin dynamics to efficiently sample from probability distributions. *Journal of Statistical Physics, 169*, 1098–1131. https://doi.org/10.1007/s10955-017-1906-8
