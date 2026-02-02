## ANN Basics
### 1. Basic Concepts:
People have developed fully connected neural networks to imitate the working of human neurons, which are once used to recognize digits and classify them. 

It works by first recognizing the grey-scale of each pixel of the whole input graph, then it go through all the pixels to identify patterns appeared, by one or multiple times of identifying patterns, it finally output 
a result which is limited between 0 - 9.

### 2. How It Works:
  i. **Flattening** :
   </br>
  Before processing the graph, we need to know ANN are **1-D machine**, like a single channel pipeline, each pixel of the graph input is extracted and entered the ANN input layer 
  **one by one** in a queue(bro never double swing--inside joke from Valorant :) ) and from top to bottom in a "queue". 
  The data set we use is **MNIST set** which are graphs of digits(28*28 pixels), so to ensure all pixel are going to enter the input layer, we should build a 728 
  neurons input layer.

  ii. **Weights and Bias** : 
   </br>
  Weights and Bias are designed to allow neuron "**_IDENTIFY/RECOGNISE_**" the patterns in the input graph. 
  Imagine you are looking at a loot item from a distance in Apex Legends. Your brain acts like a neuron to identify if it's a Sniper Rifle (Sentinel).

  **Weights** :
  Each feature has a different "importance".

  - Feature A (Long shape): Very important. Weight = 0.8.

  - Feature B (Thin body): Important. Weight = 0.6.

  - Feature C (Blue glow): Maybe it's just a common item. Weight = 0.1.

    The neuron calculates: $(Long \times 0.8) + (Thin \times 0.6) + (Glow \times 0.1)$. In the example of loot above, if the total score is high, the neuron screams: "That's a Sniper!"
    </br>
In our MNIST project, "Weights" represent how much the network cares about a specific pixel when identifying a digit.
  
  **Biases** :
    Bias is like your inner gut feeling or prejudice before even seeing the item. If you are currently in a "Snipers Only" game mode, your Bias for "It's a sniper" is very high ($+10$).
    Even if the shape is a bit blurry, you are inclined to believe it's a sniper. In our code, Bias allows the neuron to shift the activation function (I'll mention later). It's an extra number added to the sum 
    to help the model be more flexible.

  iii. Activation function:
  </br>
  Activation functions act like a trigger or a gatekeeper. They decide whether the information a neuron carries is significant enough to be passed to the next layer.
  
  Why we need it? For example, imagine you are playing Valorant and you are Jett, you saw a lot of stuff like smoke, flash, trap when your team is going to rush site. However, you don't report everything to your teammates. 
  If the enemy throws a standard smoke that everyone can clearly see, you remain silent to keep the voice channel clear.
  
  Here, the Activation Function is your brain's internal filter. It suppresses "obvious" or "low-value" signals (Output = 0) and only "activates" your microphone when you spot something critical, 
  like a hidden flanker or a specific trap.
  
  Basically, there are two main categories of activation function:
  - **ReLU** (Rectified Linear Unit):
    </br>
    ReLU is the most popular activation function in modern AI. Its logic is simple: $f(x) = \max(0, x)$.
    How it works: If the "evidence" for a pattern is 0 or negative, the neuron output is 0 (it stays silent). If the evidence is positive, it passes the value as-is.

    In Valorant terms: This is like having a confidence threshold. If you are only 10% sure you heard a footstep, you say nothing. But if your confidence is above the "zero line," you report it. The more certain you are, the louder/faster you report it.

    Why use it? It is computationally very fast and helps the network focus on only the most important features, effectively "turning off" neurons that don't find anything useful.
 
