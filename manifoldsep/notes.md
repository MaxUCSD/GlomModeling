I'm going to be borrowing a lot from this paper: 

Classification and Geometry of General Perceptual Manifolds; 

Authors: 

Chung, SueYeon and Lee, Daniel D. and Sompolinsky, Haim

# Motivation

So the rough motivation here is that intelligent systems are able to recognize objects as *invariant* despite massive variability. 

"Sensory systems are organized as hierarchies, consisting of multiple layers, transforming sensory signals into a sequence of distinct neural representations. Studies of high-level sensory systems, e.g., the inferotemporal cortex (IT) in vision [1], auditory cortex in audition [2], and piriform cortex in olfaction [3], reveal that even the late sensory stages exhibit significant sensitivity of neuronal responses to physical variables. This suggests that sensory hierarchies generate representations of objects that, although not entirely invariant to changes in physical features, are still readily decoded in an invariant manner by a downstream system. This hypothesis is formalized by the notion of the untangling of perceptual manifolds [4–6]. "


I'm not really getting this. If a representation is invariant to changes in physical attributes, then that seems to me to be good evidence of ability to be decoded in an invariant manner by a downstream region. Perhaps what they are saying is that that is what these systems are doing? 

**RESOLUTION OF ABOVE CONFUSION:** 

I think the answer is that theres two kinds of varaibility. Within and off manifold. The idea is that you want your representation to not be invariant to off manifold variation. I.e. You want to be able to recognize the difference between a cat and a dog. However, on-manifold variation, while important, is not nescessary for object recognition. A cat is a cat, not matter the lighting. This, I suppose leads to the manifold untangling hypothesis? 



# Manifold View

Consider the response of a population of N neurons to an object. This is a vector in $\mathbb{R}^N$, one can change aspects of the input (note here I'm using the word 'input' as opposed to 'object') without changing the underlying object. By changing aspects of the input, we move around our neural population vector. The set of all possible neural population vectors corresponding to the same object (different inputs) is the *Perceptual Manifold*. Object recognition  is thus the task of drawing some decision boundary between manifolds. They will study the case of a simple linear classifier. 

## Note
So we have: f(input) = neural response, g(neural response) = object. I'm not sure how important this is... But, I think it's important to note that there can be changes in the input which don't show up as changes in the neural response. (I don't think that there can be changes in the neural response without changes in the input?). 



# Classifying Line Segments

Consider $P$ line segments (indexed with $\mu$ lol) implicitly defined as follows and $P$ labels:

$$ \bold{x}^\mu + Rs\bold{u}^\mu $$

$\bold{x}^\mu$ and $\bold{u}^\mu$ are both in $\mathbb{R}^N$, $s$ goes from $-1, 1$ and $R$ is a scalar. (Essentially, it defines the full length of the vector). 

Okay, lets go over this with an example: 

## Example #1 (Line Segments)

Imagine we are in $\mathbb{R}^2$, and set $P = 1$. 

Lets set $\bold{x}^{1} = [0,0]$ for simplicity. This leaves $Rs\bold{u}^{1}$. Set  $\bold{u}^{1} = [2,3]$ and $R = 1$. We are left with $s[2, 3]$. Lets look at what happens when we set $s = -1,0,1$, respectively:

---
### $s=-1$
$s\bold{u}^{0}$

$s = -1$

$\bold{u}^{1} = [2, 3]$

$s\bold{u}^{1} = [-1(2), -1(3)] = [-2, -3]$

--- 

### $s=-0$

$s\bold{u}^{1}$

$s = 0$

$\bold{u}^{1} = [2, 3]$

$s\bold{u}^{1} = [0(2), 0(3)] = [0, 0]$

---

### $s=1$

$s\bold{u}^{1}$

$s = 1$

$\bold{u}^{1} = [2, 3]$

$s\bold{u}^{1} = [1(2), 1(3)] = [2, 3]$

---
Okay! So, as you can hopefully see, $s$ defines the line from the end point (here $[-2,-3]$) to the middle point (here $[0,0]$), to the other end point (here $[2,3]$).

The next steps are incorporating $\bold{x}$ and $R$, but thankfully those are quite easy. Remember back to when we computed $s\bold{u}^{1} = [0, 0]$, now think through what would have happened had we made $\bold{x}^{1} = [1, 1]$, well, now the midpoint of the line segment would be $[1,1]$ and everything else would be *translated* by that. The point (no pun intended) here is that $\bold{x}$ controls the midpoint of our line segment. 

Don't worry, I'm not forgetting about $R$. We already know what it does in the case where $R = 1$. The only difference when $R \neq 1$ is that length of the line segment is extended by $2R$. In the context of classification, $R$ will control how hard it is. 

## Example #2 (The Role of $R$)

Take two line segments:


set $\bold{x}^{1} = [1,0]$, and $\bold{u}^{1} = [0, 1]$

set $\bold{x}^{2} = [5,0]$, and $\bold{u}^{2} = [1, 0]$



For $R = 1$:

Computing $\bold{x}^{1} + Rs\bold{u}^{1}$

For $s = -1,1$

- $s = -1$

    - $[1,0] - 1[0, 1] = [1,0] + [0, -1] = [1, -1]$

- $s = 1$

    - $[1,0] + 1[0, 1] = [1,0] + [0,1] = [1,1]$

So for $\mu = 1$, the line segment goes from $[1, -1]$ to $[1,1]$


Computing $\bold{x}^{2} + Rs\bold{u}^{2}$

For $s = -1,1$

- $s = -1$

    - $[5,0] - 1[1, 0] = [5,0] + [-1, 0] = [4, 0]$


- $s = 1$

    - $[5,0] + 1[1, 0] = [5,0] + [1,0] = [6, 0]$


So for $\mu = 1$, the line segment goes from $[4, 0]$ to $[6, 0]$

Theyre is no overlap as of yet, but what if we increased $R$ by $5$.

For $R = 5$:

Computing $\bold{x}^{1} + Rs\bold{u}^{1}$

For $s = -1,1$

- $s = -1$

    - $[1,0] - 5[0, 1] = [1,0] + [0, -5] = [1, -5]$

- $s = 1$

    - $[1,0] + 5[0, 1] = [1,0] + [0,5] = [1,5]$

So for $\mu = 1$, the line segment goes from $[1, -5]$ to $[1,5]$


Computing $\bold{x}^{2} + Rs\bold{u}^{2}$

For $s = -1,1$

- $s = -1$

    - $[5,0] - 5[1, 0] = [5,0] + [-5, 0] = [0, 0]$


- $s = 1$

    - $[5,0] + 5[1, 0] = [5,0] + [5,0] = [10, 0]$


So for $\mu = 1$, the line segment goes from $[0, 0]$ to $[10, 0]$

**They Intersect!**

Consider the limit as $R \rightarrow \inf$, then, only parallel lines will be safe!

## The role of $\bold{u}$

Okay, so so far we have a few objects in our expression. We know the role of $\bold{x}$, $R$, and $s$. But what is $\bold{u}?$ In a sense, $\bold{u}$ defines a *direction*. 

Consider for a moment the simplified expression: 

$$s\bold{u}$$ 

Where $s$, is the same as before. Now consider this a function of $s$, so we have: 

$$f(s) = s\bold{u}$$

What is the role of $\bold{u}$ in this function? Lets play with some real numbers and see what happens. Before we start remember that $\bold{u}$ is a vector in $\mathbb{R}^N$. For visualization purposes let's set $N = 2$. Now, what happens to the resulting output if $\bold{u} = [1, 0]$, what happens as we move $s$?

$$f(s) = s[1,0] = [s, 0]$$

This is a horizontal line. 

What about if $\bold{u} = [0, 1]$

$$f(s) = s[0,1] = [0, s]$$

This a vertical line. 

Let's do one more, $\bold{u} = [2, 3]:$

$$f(s) = s[2,3] = [s2, s3]$$

This is telling us to move twice in the x direction and 3 times in the y direction. It is a slope! Of course, in $N$ dimensions, it's not really a slope, its more like a direction. 

Another way of seeing this is if we take the derivative of our function:

$$\frac{d}{ds}f(s) = \bold{u}$$

## Summary so far. 

Thus far we have been examinging the equation:

$$ \bold{x}^\mu + Rs\bold{u}^\mu $$

$\mu$ indexes $P$ line segments. $\bold{x}^\mu$ represents the center of the line, it is a point in $\mathbb{R}^N$. $R$ controls the length of each line. They motivate $R$ slightly differently "...measures the extent of the
segments relative to the distance between the centers". We parameterize the line segment with $s$, a scalar, $-1 \leq s \leq 1$, and $\bold{u}$, a vector in $\mathbb{R}^N$ controls the direction. 

## Adding $\bold{w}$ to the equation.
We are going to be building up the classification inequality that they use.

$$ y^\mu\bold{w} \cdot (\bold{x}^\mu + Rs\bold{u}^\mu ) \geq \kappa$$


Consider what it would mean to slightly change our expression (now into an equation):

$$ \bold{w} \cdot (\bold{x}^\mu + Rs\bold{u}^\mu ) = 0$$


Lets start by considering the case where $s = 0$, so we have: 

$$ \bold{w} \cdot (\bold{x}^\mu) = 0$$

Let $\bold{w} = [1,0]$ (and drop the $\mu$ index for now) 

$$
\begin{align}

[1,0] \cdot \bold{x}  &= 0 \\
1 \bold{x}_1 + 0 \bold{x}_2 &= 0 \\
\bold{x}_1 &= 0 \\

\end{align}
$$

Therefore, $\bold{x}$ must have the form: $\bold{x} = [0, \bold{x}_2]$ for any $\bold{x}_2$. In order to satisfy the constraint $\bold{w} \cdot \bold{x} = 0$, for some $\bold{w}$, $\bold{x}$ has to be perpendicular (orthogonal in higher dimensions) to $\bold{w}$! This is just the implicit form of something about the dot product we already knew: if two vectors dot products $=0$, they are orthogonal. The set of all vectors (while holding one fixed) which satisifes this constraint is a hyperplane. 

It might be helpful to see this in 3 dimensions. 

Let $\bold{w} = [1,0,1]$ (dropping the $\mu$ index for now) 

$$
\begin{align}

\bold{x} \cdot [1,0,1] &= 0 \\
\bold{x}_11 + \bold{x}_20 + \bold{x}_31 &= 0 \\
\bold{x}_1 + \bold{x}_3&= 0 \\
\bold{x}_3 &= -\bold{x}_1  \\

\end{align}
$$

Therefore, $\bold{x}$ must have the form: $\bold{x} = [\bold{x}_1, \bold{x}_2, -\bold{x}_1]$

This is a plane!

What we want to show is that $\bold{w}$ is normal to $\bold{x}$. Also, It is important to note that $\bold{x}$ right now just represents the input space, it is not (yet) the actual data points. We can pick two points on the hyperplane, $\bold{x}^1$ and $\bold{x}^2$

Our goal is to show that $\bold{w}$ is orthogonal to $y = \bold{x}^2 - \bold{x}^1$. $y$ is a vector which is totally on the hyperplane, it is a dispalcement vector. Recall that $\bold{w} \cdot \bold{x}$ = 0 is how we define a point $\bold{x}$, thus: 

$$
\bold{w} \cdot \bold{x}^1 = 0
$$
$$
\bold{w} \cdot \bold{x}^2 = 0
$$

Therefore, $\bold{w} \cdot(\bold{x}^2 - \bold{x}^1) = 0$

To see this, note that the dot product distributes over subtraction of two vectors. This also works in the case of a bias. 



$$
\bold{w} \cdot \bold{x}^1 + \kappa = 0
$$
$$
\bold{w} \cdot \bold{x}^2 + \kappa = 0
$$
$$
\bold{w} \cdot \bold{x}  = -\kappa

$$

 $$\bold{w} \cdot(\bold{x}^2 - \bold{x}^1) = (\bold{w} \cdot \bold{x}^2)
 -(\bold{w} \cdot \bold{x}^1) = (-\kappa - -\kappa) = 0
 $$



 **NOTE**

 $\bold{w}$ encodes a direction! 
 To see this, note that we have been working with the equation 


 $$
 \bold{w_1}\bold{x_1} + \bold{w_2}\bold{x_2} + \kappa = 0

 $$

 We can rearange this to slope intercept form $y = mx + b$ by solving for $x_2(y)$  in terms of $x_1(x)$:

 $$
 \begin{align} 
 \bold{w_1}\bold{x_1} + \bold{w_2}\bold{x_2} + \kappa &= 0 \\
 \bold{w_2}\bold{x_2} &= -\bold{w_1}\bold{x_1} - \kappa \\
 \bold{x_2} &= - \frac{\bold{w_1}\bold{x_1}}{\bold{w_2}} + \frac{\kappa}{\bold{w_2}}
\end{align}
 $$

 Thus, the slope of the hyperplane is $-\frac{{\bold{w_1}}}{{\bold{w_2}}}$ and the intercept is  $\frac{\kappa}{\bold{w_2}}$


 **NOTE #2**

 Do not confuse the above with the slope of the $\bold{w}$ vector. That slope we can derive as follows (by using point point slope form and remembering that $\bold{w}$ starts at the origin):

 $$
\begin{align}
slope &= (y_2 - y_1)/(x_2 - x_1) \\
slope &= (\bold{w_2} - 0)/(\bold{w_1} - 0) \\
slope &= \bold{w_2}/\bold{w_1} \\
\end{align}
 $$

 Recall that if two lines are perpendicular the product of their slopes = -1

 $$
 \frac{\bold{w_2}}{\bold{w_1}} (-\frac{{\bold{w_1}}}{{\bold{w_2}}}) = -1
 $$

 ## Summary so far

 Okay disregard everything, this is the important bit. We are going to work in $2d$ but the reasoning extends. The way I want to think of hyperplanes as defined by their normal is like this. Given some vector $w$, there is a set of vectors $x$, such that $w \cdot x = 0.$ This defines a hyperplane *through the origin* (anything dotted with the zero vector = $0$) which is gauranteed to be orthogonal to $x$. However, we do not need to go through the origin, we can shift the hyperplane by a constant factor, what we have been calling $\kappa$. We essentially just did a lot of work convincing ourselves that $w$ implicitly defines a hyperplane by orthogonality. 



<!-- 


Imagine for a moment we had 

$$ \bold{w} \cdot \bold{x} = \kappa$$
$$
\begin{align}

\bold{x} \cdot [1,1,1] &= \kappa \\
\bold{x}_11 + \bold{x}_21 + \bold{x}_31 &= \kappa \\
\bold{x}_1 + \bold{x}_2 + \bold{x}_3&= \kappa \\
\bold{x}_2 + \bold{x}_3 &= -\bold{x}_1 + \kappa  \\
\bold{x}_3 &= -\bold{x}_2 -\bold{x}_1 + \kappa  \\


\end{align}
$$

Therefore, $\bold{x}$ must have the form: $\bold{x} = [\bold{x}_1, \bold{x}_2, -\bold{x}_2 -\bold{x}_1 + \kappa]$

Lets pick some $\bold{x}'s$

$\bold{x} = [1, 2, -2 - 1 + \kappa]$

$\bold{x} = [1, 2, -3 + \kappa]$

$\bold{w} \cdot \bold{x}$

$[1,1,1] \cdot [1,2,-3 + \kappa]$

$ 1(1) + 1(2) + 1(-3 + \kappa)$

$ 3-3 + \kappa$ -->
