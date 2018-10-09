# Some Topics on Deep Learning

This is an assignment for External Internship Programme in Deep Learning Techniques in Computer Vision, by MLBLR group in Bangalore.

## Topics

### Convolution
A convolution is an operation applied in convolutional layers in convolutional neural networks. Strictly speaking, this operation is a cross-correlation as a convolution means a different operation in mathematics. 

<<<<<<< HEAD
A convolution layer accepts as input a volume of size $w_1 x h_1 x d_1$. Typically, this requires 4 hyper-parameters:
=======
A convolution layer accepts as input a volume of size $w_1 \times h_1 \times d_1$. Typically, this requires 4 hyper-parameters:

>>>>>>> 02b9961e847d9fd89ecae34597b7a4f4d879913a
1. the number of filters, $k$
2. the filter size, $f$
3. the stride, $s$
4. the amount of zero padding, $p$

<<<<<<< HEAD
This convolution layer produces a volume of size $w_2 x h_2 x d_2$, where:
$w_2 = (w_1 - f + 2 * p) / s + 1$
$h2 = $
=======
This convolution layer produces a volume of size $w_2 \times h_2 \times d_2$, where:
$w_2 = (w_1 - f + 2 \times p) / s + 1$, $h_2 = (h_1 - f + 2 \times p) / s + 1$, and $d_2 = k$.

The size of each filter is $f \times f \times d_1$.

The operation performed is a sum of element-wise multiplications between the filter (also known as kernel) & the input volume, with the filter shifting by stride $s$, to the right & then bottom (starting from the left again) when it reached the right end of the input volume.

The values $f = 3$, $s = 1$, $p = 1$ are commonly used.

![A 5x5 convolution](https://i.stack.imgur.com/f2RiP.gif)

So, convolution is the process of adding each element of an image with its neighboring elements, weighted by the kernel.
>>>>>>> 02b9961e847d9fd89ecae34597b7a4f4d879913a


### Filters/Kernels

Also known as mask or a convolution matrix. This is used in convolutional layers to carry out the convolution operation with the input volumes. A kernel is used for detecting features in an image which is useful for minimizing the loss between the truth value & the predicted outputs. These features could be edges, colours, shapes, more complex objects like eyes, nose etc. For this reason, they are also known as feature detectors.

In a convolutional layer, the values in a filter are initialised randomly and then updated during back-propagation to minimize the network's loss. Generally, $3 \times 3$ filters are used in convolutional layers.


### Epochs

An epoch is the number of times a deep learning model goes through the entire training set. One can do a backpropagation step after every epoch. But in mini-batch optimization algorithms, a backpropagation step is carried out, after every batch of training examples and hence, before a single epoch is completed. A backpropagation step is called a backward pass. In full batch algorithms, a forward pass consists of all training examples, whereas in mini-batch algorithms a forward pass consists of a batch of training examples. An iteration is a single forward and a single backward pass. So, we see that the concepts of an epoch and an iteration are different.


### 1x1 convolution

A 1x1 convolution is mainly used to decrease the depth (dimensionality reduction) of the input image. This can help in speeding up the computation as it reduces the number of channels, and also may help in diminishing the effect of "unnecessary" features in the final prediction. It can also learn temporal dependencies in images, connecting different channels: like a pair of eyes.

Suppose a convolution layer outputs an image of dimension $(h, w, f)$ where 
1. $h, w$ are the height & weight respectively (spatial dimensions)
2. $f$ is the number of convolution filters in the layer.

Now if this output is fed into a convolution layer with $f_1$ $1 \times 1$ filters, then the output image will be of dimension $(h, w, f_1)$. So $1 \times 1$ convolutions changes the dimension in the filter space. If $f_1 < f$, this can be used for dimensionality reduction. So $1 \times 1$ convolutions can be used before computationally expensive $3 \times 3$ convolutions.


### 3x3 convolution

Using $3 \times 3$ convolution filters is very common in deep learning architectures. If we use $3 \times 3$ convolution twice, to get the same output as we would get from a single $5 \times 5$ convolution, we would be actually using $3 \times 3 + 3 \times 3 = 18$ weights as compared to $5 \times 5 = 25$ weights. This increases computational efficiency. Also, since the number of layers increases, it learns more complex non-linear features. Also $3 \times 3$ kernel is preferred since $3$ is odd number, and with odd-sized kernels, the previous layer pixels would be symmetrically around the output pixel & we can prevent the distortions across the layers.


### Feature Maps

A feature map is also known as activation map. This is the output activations for a given filter. This is the result of the activation function applied on the output of a convolution process. A rectified feature map is the result of the activation function when $ReLU$ is used. Sometimes, the term feature map is used to denote the output of a convolution operation, but this usage is rare.


### Feature Engineering (older Computer Vision concept)

Feature engineering is manual selection & transformation of the features (the $x$'s) in a model. In computer vision, if you provide something other than image pixels into the algorithm, we are doing feature engineering. The new features we might add could be edge orientations, color histograms etc. This could help in building a better classifier. Computer vision researchers used to do a lot of feature engineering before deep learning.


### Activation Function

Activation function defines the output of a neuron or node or layer, given a set of inputs. In artificial neural networks, activations are used generally after every fully connected layer or convolution layers to learn non-linearity in the data. Usually $tanh(x)$ or $\sigma(x)$, the sigmoid function, or $softmax(x)$, or $ReLU(x)$ are used as activation functions. In the presence of a non-linear activation function, a 2-layer neural network can be proven to be a universal function approximator.


### How to create an account on GitHub and upload a sample project

Steps:
1. Go inside the project folder using `cd` and type in `git init`. Install `git` if not present.
2. Create a empty repository in github.
3. Get a link for the remote repository you just created. It will be something like:
`https://github.com/your_username/your_repo.git`.
4. Back in the command line or terminal type in `git remote add origin [above_link]`.
5. Type `git add .` to add all content inside the folder to git.
6. Type `git commit -m "give your commit message here"` to commit the changes.
7. Finally do `git push -u origin master` to push the changes in local repository to the remote repository on github.


### Receptive Field

Receptive field could be thought of as the range of vision. In a convolution operation, if we apply a convolution filter of size $3 \times 3$ then we say that the receptive field of the kernel or filter is $3 \times 3$, since the kernel will only see a $3 \times 3$ block of the input image while computing one pixel value of the output. Notice that we only talk about the width & height of the kernel and not the depth, since the depth is fixed to the depth of input image.


### 10 examples of use of [MathJax](https://support.typora.io/Markdown-Reference/#math-blocks) in Markdown

Example 1: Use double dollar `$$` and press return for math block and single `$` for inline math. 
$$
y = {-b \pm \sqrt{b^2-4ac} \over 2a} 
$$
Example 2: $exp(i \pi) = -1$

Example 3: $x^n + y^n = z^n$

Example 4: $P(E) = {n \choose k} p^{k} (1 - p)^{n- k}$

Example 5: $A\cos \frac{2\pi}{\lambda} (x) + i A\sin \frac{2\pi}{\lambda} (x)$

Example 6: $y \sim N(\mu, \sigma^{2})$

Example 7: $ (x+y)^m = \sum_{k=0}^{m} {m \choose k} x^{m - k} y^k $

Example 8: $ P(C \mid D) = \frac{P(D \mid C) \, P(C)}{P(D)} $

Example 9:
$$
\left( \sum_{m=1}^n a_m b_m \right)^2 \leq
\left( \sum_{m=1}^n a_m^2 \right)
\left( \sum_{m=1}^n b_m^2 \right)
$$


Example 10:
$$
\sum_{y < n \le x} f(n) = \int_y^x f(t) dt +  \\
\int_y^x (t - [t]) f'(t) dt + f(x)([x] - x) - f(y)([y] - y)
$$
