# computations

- mkdocs supports rendering computations if you want to get that nerdy :)
- get nerdy and show computations

$$
\cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}
$$

The homomorphism $f$ is injective if and only if its kernel is only the
singleton set $e_G$, because otherwise $\exists a,b\in G$ with $a\neq b$ such
that $f(a)=f(b)$.

- this feature requires some setup
- <https://squidfunk.github.io/mkdocs-material/reference/math/#mathjax-docsjavascriptsmathjaxjs>

```lex
$$
\cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}
$$
```

## Eclipse Prediction with MathJax

This document demonstrates the use of MathJax to format equations for predicting eclipses.

### 1. Synodic Month

The **synodic month** represents the time between successive new moons. It’s computed as follows:

\[
T_s = \frac{1}{\frac{1}{T_m} - \frac{1}{T_e}}
\]

where:

- \( T_s \) is the synodic month (about 29.53059 days),
- \( T_m \) is the Moon’s sidereal orbital period around Earth (27.321661 days),
- \( T_e \) is Earth’s sidereal orbital period around the Sun (365.25636 days).

## 2. Draconic (Nodal) Month

The **draconic month** is the period it takes the Moon to return to one of its nodes. Eclipses can occur only when the Moon is near a node:

\[
T_d = 27.2122 \text{ days}
\]

This period is important for predicting eclipse timings.

### 3. Eclipse Season

Eclipses can occur when the Sun is near a node within a certain angular range, calculated by:

\[
T_{\text{season}} = \frac{1}{\frac{1}{T_d} - \frac{1}{T_s}}
\]

This results in an eclipse season every 173.31 days, where at least one solar or lunar eclipse is possible.

### 4. Anomalistic Month

The **anomalistic month** is the time for the Moon to return to perigee (the point closest to Earth), which impacts whether a solar eclipse will be total or annular:

\[
T_a = 27.55455 \text{ days}
\]

### 5. Saros Cycle

The **Saros cycle** is a period after which similar eclipses will recur with almost identical geometry. It is approximately given by:

\[
T_{\text{Saros}} = 18 \times T_y + 10 + \frac{1}{3} \text{ days}
\]

where \( T_y \) represents the tropical year (365.2422 days). This means similar eclipses occur roughly every 18 years, 11 days, and 8 hours.

### 6. Angular Separation for Eclipse Occurrence

For an eclipse to occur, the angular separation between the Moon and the Sun, as viewed from Earth, must fall within a critical limit:

\[
\Delta \theta = \left| \theta_{\text{Sun}} - \theta_{\text{Moon}} \right| < \theta_{\text{limit}}
\]

where:

- \( \theta_{\text{Sun}} \) and \( \theta_{\text{Moon}} \) are the Sun’s and Moon’s angular positions relative to Earth,
- \( \theta_{\text{limit}} \) is the maximum separation within which an eclipse is possible (approximately \( 15^\circ \)).

### 7. Spherical Trigonometry for Celestial Positioning

Precise eclipse predictions require calculating the exact positions of the Sun, Moon, and Earth using spherical trigonometry:

\[
\cos(\theta) = \sin(\delta_1) \sin(\delta_2) + \cos(\delta_1) \cos(\delta_2) \cos(\alpha_1 - \alpha_2)
\]

where:

- \( \theta \) is the angle between two celestial objects,
- \( \delta_1 \) and \( \delta_2 \) are their declinations (angular distance from the celestial equator),
- \( \alpha_1 \) and \( \alpha_2 \) are their right ascensions (angular distance measured along the celestial equator).

### Summary

Combining these cycles—synodic, draconic, anomalistic months, and the Saros cycle—with precise geometry allows for accurate eclipse prediction.
