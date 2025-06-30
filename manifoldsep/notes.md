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


So for $\mu = 1$, the line segment goes from $[4, 0]$ to $[7, 0]$

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

