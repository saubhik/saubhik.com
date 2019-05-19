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

To create a recurrent cell, the controller RNN samples $$a^2 = b^2 + c^2$$ blocks of decisions.

$$ P_{ni} = \int L_{ni}(\beta)f(\beta)d\beta $$
