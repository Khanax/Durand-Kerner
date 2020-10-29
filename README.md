# Durand-Kerner

Python Implementation of Duran-Kerner algorithm that finds all the roots of a polynomial by Weierstrass' methodsimultaneously (or known in Abramowitz&Stegun as the Durand-Kerner method).
Note that there are limitations that have not beed resolved..such as exploding calculations on really big polynomials of 600 degrees for example.

# Example

To find the roots for $$5 x^4 + 3 x^3 + 4 x^2 + 8 x + 10$$

```python
args = [5, 3, 4, 8, 10]
ITERATIONS = 100

roots = Durand_Kerner(args, polyeval, ITERATIONS)

```

### Output

```
-0.8853-0.6337 j

-0.8853+0.6337 j

0.5853+1.1596 j

0.5853-1.1596 j

```

### API

```
from Durand_Kerner import DK

-0.8853+0.6337 j

0.5853+1.1596 j

0.5853-1.1596 j

```

# A Crazy Case

To find the roots for $$87x^{20} + 54 x^{19} -13 x^{18} + 120 x^{17} + 14 x^{16} + 23 x^{15} + 51 x^{14} - 312 x^{13}+ 35 x^{12} + 43 x^{11} + 3 x^{10}  $$
$$+ 213 x^{9} + 43 x^{8} + 1x^{7} + 32x^{6} +  98x^{5} + 123 x^{4} +  90x^{3} + 2x^{2} + 1x + 823$$

### Output

```
-1.237-0.3364j
-1.237+0.3364j
-1.1212-0.2629j
-1.1212+0.2629j
-0.7631-0.6657j
-0.7631+0.6657j
-0.42-0.9946j
-0.42+0.9946j
-0.2356+1.1398j
-0.2356-1.1398j
0.1538+1.0849j
0.1538-1.0849j
0.5973+0.858j
0.5973-0.858j
0.7262-1.026j
0.7262+1.026j
0.8988-0.4908j
0.8988+0.4908j
1.0904+0.2089j
1.0904-0.2089j

```

```
License

(c) 2020 Stergios Bachoumas. MIT License

```
