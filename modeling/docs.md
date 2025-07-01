So we want to model the population activity of the glomeruli. 

$P \in \mathbb{R}^{T\times N}$

Each glomeruli ($n$) responds to an input pulse $I$ (we can later extend this to different kinds of input stimuli and have different glomeruli respond to different inputs). We can model the response of each glomeruli as some spiking function where we can control two things: 

- Adapatation
- Decay time. 

Adaptation should work as follows. If I am a glomeruli and I spiked recently and I just recieved another input, then I should only add in a sublinear way. 

We can start without adaptation and just use a simple exponential different eq:

$$\frac{dr}{dt} = -\frac{r}{\tau} + I(t)$$

The solution of this diff eq, without input, is: 

$$ r(t) = r_0e^-{\frac{t}{\tau}}$$


adding adaption:
$$\frac{dr}{dt} = -\frac{r}{\tau} + I(t) * (1 - a(t))$$
$$ \frac{da}{dt} = -\frac{a}{\tau_{a}} + \beta * r(t)$$

**IMPORTANT:** These eq's will only adapt at the level of the firing rate, it seems likely that what we see is happening at the level of the *tap*. To change this we can modify $\frac{da}{dt}$ to be dependent on $I(t)$ instead of $r$.


# 6/26/25

We made some pretty significant changes. Now, we are using a depletion based model where we have some concentration of a receptor and that determines $a$. The eq for $a$ now looks like: 

$$\frac{da}{dt} = \frac{1-a}{\tau_a} - \chi \frac{I(odor, glom)}{I_{max}}$$ 

The idea is that at a = 0 and input = 0 then a is at its steady state? 

Where $\chi$ is an indicator function that tells you if I am currently tapping.: 

$$ \chi = \sum_{t_{tap}} \delta (t - t_{tap})$$

I haven't decided on the exact form of $I$ yet... Not sure how. It should be specific to each glomeruli type and we want it to be much higher when this glomeruli prefers this odor. If this g doesn't care about the odor then we shouldn't adapt, is the idea. 

Then we have $s$ which is the "synaptic current". This is what will determine the rate $r$ and is affected by the input and the adaptation.

$$\frac{ds}{dt} = -\frac{s}{\tau_{s}} + a\chi \frac{I(odor,glom)}{I_{max}}$$

Then finally we have: 

$$\frac{dr}{dt} = -\frac{r}{\tau_r} + s $$

We can clean up a little more by setting 

$$ \chi = \frac{I(odor,glom)}{I_{max}}\sum_{t_{tap}} \delta (t - t_{tap}) $$

Thus we have: 

$$\frac{da}{dt} = \frac{1-a}{\tau_a} + \chi$$ 
$$\frac{ds}{dt} = -\frac{s}{\tau_{s}} + a\chi$$
$$\frac{dr}{dt} = -\frac{r}{\tau_r} + s $$

One question, what does it mean to normalize I in the eq for S, I didn't originally do that. 

I think we need to change $\frac{da}{dt}$ to be $- \chi$ instead of $+ \chi$ because we want to decrease the amount of total input $\chi$ that matters. We should probably change a to be like c for concentration.

## **FINAL EQ'S** 
$$\frac{dc}{dt} = \frac{1-c}{\tau_c} - \chi$$ 
$$\frac{ds}{dt} = -\frac{s}{\tau_{s}} + c\chi$$
$$\frac{dr}{dt} = -\frac{r}{\tau_r} + s $$
$$ \chi = \frac{I(odor,glom)}{I_{max}}\sum_{t_{tap}} \delta (t - t_{tap}) $$


We can start the simulation testing by ignoring $I$ and just using like a simple binary input (1 if tap now or 0 otherwise).

**OMG WAIT** 

We had some weird steady state behavior with those eq's.. in particular 
$$\frac{dc}{dt} = \frac{1-c}{\tau_c} - \chi$$ 

setting $\frac{dc}{dt}$ = 0

$$\begin{align}
0 &= \frac{1-c}{\tau_c} - \chi \\ 
\chi &= \frac{1-c}{\tau_c} \\
\chi \tau_c &= 1 - c \\
1 -\chi \tau_c &= c

\end{align}$$

So if $\chi \tau_c  > 1 $, well then we get negative concentration! To fix this we can multiply $\chi$ by $c$ as well

$$\frac{dc}{dt} = \frac{1-c}{\tau_c} - \chi c$$ 

This means the rate of depletion will always be proportional to available concentration. 

Solving for the steady state:


$$\begin{align}
0 &= \frac{1-c}{\tau_c} - \chi c \\ 
\chi c &= \frac{1-c}{\tau_c} \\
\chi c \tau_c &= 1 - c \\
\chi c \tau_c + c &= 1 \\
c (\chi \tau_c + 1) &= 1 \\
c &= \frac{1}{(1 + \chi \tau_c)} 
\end{align}$$

Yay! this means if $\chi \tau_c$ is big then we go towards $0$!

# 6/27/25

Okay, after that final change we have:

$$\frac{dc}{dt} = \frac{1-c}{\tau_c} - c\chi$$ 
$$\frac{ds}{dt} = -\frac{s}{\tau_{s}} + c\chi$$
$$\frac{dr}{dt} = -\frac{r}{\tau_r} + s $$
$$ \chi = \frac{I(odor,glom)}{I_{max}}\sum_{t_{tap}} \delta (t - t_{tap}) $$

## Deriving the steady state solutions

### EQ 1 Capacity
$$\begin{align}
\frac{dc}{dt} &= \frac{1-c}{\tau_c} -c\chi\\
0 &= \frac{1-c}{\tau_c} -  c\chi \\ 
c\chi &= \frac{1-c}{\tau_c} \\
c\chi \tau_c &= 1 - c \\
c\chi \tau_c + c &= 1 \\
c (\chi \tau_c + 1) &= 1 \\
c &= \frac{1}{(1 + \chi \tau_c)} 
\end{align}$$

### EQ 2 Synaptic Input
$$\begin{align}
\frac{ds}{dt} &= -\frac{s}{\tau_{s}} + c\chi\\
0 &= -\frac{s}{\tau_{s}} + c\chi \\
\frac{s}{\tau_{s}} &= c\chi \\
s &= c\chi  \tau_{s}
\end{align}$$

### EQ 2 Synaptic Input
$$\begin{align}
\frac{dr}{dt} &= -\frac{r}{\tau_r} + s  \\
0 &= -\frac{r}{\tau_{r}} + s\\
\frac{r}{\tau_{r}} &= s \\
r &= s \tau_{r}
\end{align}$$

## TODO 
- I want to derive analytical expressions for the long term behavior of this system, given an infinite time spike train. At certain adaptation rates, given by the various $\tau$'s, $r$ never goes below a certain value. Also, what is the maximum value we can drive $r$? 
    - Ultimately, what's interesting about this is how it will affect the information capacity of the system. 
        - It's not clear how we should think about information capacity... Certainly in terms of $I$

- Next we will add a normalization layer in the Mitral Cells like in the main olfactory system and ask about their readout. 

- Some of these questions are still, as of yet, not super clear. 