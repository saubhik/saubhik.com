# Efficient Neural Architecture Search Via Parameter Sharing

## Methods
All of the graphs which NAS ends up iterating over can be viewed as sub-graphs
of a larger graph. We can represent NAS's search space using a single directed
acyclic graph (DAG). Nodes represent local computation and the edges represent
the flow of information. The local computations at each node have their own
parameters, which are used only when the particular computation is activated.
Therefore, ENAS's design allows parameters to be shared among all child models.
i.e. architectures, in the search space.

Topics:
* how to design a cell for RNN from a specified DAG and a controller
* how to train ENAS and how to derive architectures from ENAS's controller
* explain search space for designing convolutional architectures

### Designing Recurrent Cells
ENAS's controller is an RNN that decides:
* which edges are activated
* which computations are performed at each node in the DAG

To create a recurrent cell, the controller RNN samples $$N$$ blocks of
decisions.

An example illustation via a simple example recurrent cell with $$N=4$$
computational nodes:
Let \\( x_t \\) be the input signal for a recurrent cell, and \\(h_{t-1}\\) be the
output from the previous time step.

1. The controller first samples an activation function. If controller chooses
	 \\(tanh\\) activation function, which means node \\(1\\) of the recurrent
	 cell should compute \\(h_1=tanh(x_t \cdot W^{x} + h_{t-1} \cdot W_{1}^{h})\\).

2. At other nodes, the controller samples a previous index (say \\( j \\) ), and
	 an activation function, (say \\( ReLU \\) ). We have \\( h_i = ReLU(h_j \cdot
	 W^{h}_{i,j}) \\).

3. For output, we average the nodes that are not selected as previous index.

For each pair \\( (i,j) \\) of nodes, there is an independent parameter matrix
\\( W^{h}_{i,j} \\) which are shared by all recurrent cells in ENAS.

If the recurrent cell has \\( N \\) nodes, and we allow \\( 4 \\) activation
functions (like `tanh`, `ReLU`, `identity`, `sigmoid`), then the search space
has \\( 4^N \times N! \\) configurations, i.e. architectures.

The paper uses \\( N = 12 \\).

### Training ENAS and Deriving Architectures
