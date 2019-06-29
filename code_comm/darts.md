# Understanding DARTS code

Here is the [source](https://github.com/quark0/darts).
I want to understand the `DARTS` code for `cnn`.

I start with the `train_search.py` script. Let's start with the entry point, `main()` method:

## train_search.py
Methods:

### main()
```python
def main():
  if not torch.cuda.is_available():
    logging.info('no gpu device available')
    sys.exit(1)

  np.random.seed(args.seed)
  torch.cuda.set_device(args.gpu)
  cudnn.benchmark = True
  torch.manual_seed(args.seed)
  cudnn.enabled=True
  torch.cuda.manual_seed(args.seed)
  logging.info('gpu device = %d' % args.gpu)
  logging.info("args = %s", args)
	...
```
This partly mostly deals with setting numpy & torch seeds from the argument `args.seed`.
TODO: Fair enough, notice the `cudnn.enabled=True`.
Moving on,
```python
criterion = nn.CrossEntropyLoss()
criterion = criterion.cuda()
model = Network(args.init_channels, CIFAR_CLASSES, args.layers, criterion)
model = model.cuda()
logging.info("param size = %fMB", utils.count_parameters_in_MB(model))
```
`Network(...)` returns a model based on `CIFAR_CLASSES=10`, `args.init_channels`
which is 16 by default, `args.layers` which is 8 by default, and
`criterion=nn.CrossEntropyLoss()`.
> We have to understand `model_search.Network`

Moving on,
```python
optimizer = torch.optim.SGD(
  model.parameters(),
  args.learning_rate,
  momentum=args.momentum,
  weight_decay=args.weight_decay
)
```

This is our standard SGD optimizer with `args.learning_rate=0.025`,
`args.momentum=0.9`, `args.weight_decay=3e-4` as default values.

```python
train_transform, valid_transform = utils._data_transforms_cifar10(args)
train_data = dset.CIFAR10(root=args.data, train=True, download=True, transform=train_transform)
```

> We have to understand `utils._data_transforms_cifar10()`

We get `train_data` from `torchvision.datasets.CIFAR10`. I am hoping there are
some transformations in `train_transform` & `valid_transform`.

Then we split the `train_data` based on `args.train_portion` which is 0.5 by
default. We split into training set and validation set.

```python
num_train = len(train_data)
indices = list(range(num_train))
split = int(np.floor(args.train_portion * num_train))
```

We get the `train_queue` and `valid_queue` using the
`sampler.SubsetRandomSampler`. Notice `pin_memory=True`. We also set
`lr_scheduler.CosineAnnealingLR()` with `args.epochs` as 50 by default and
`args.learning_rate_min` 0.001 by default:

```python
num_train = len(train_data)
indices = list(range(num_train))
split = int(np.floor(args.train_portion * num_train))

train_queue = torch.utils.data.DataLoader(
  train_data, batch_size=args.batch_size,
  sampler=torch.utils.data.sampler.SubsetRandomSampler(indices[:split]),
  pin_memory=True, num_workers=2
)

valid_queue = torch.utils.data.DataLoader(
  train_data, batch_size=args.batch_size,
  sampler=torch.utils.data.sampler.SubsetRandomSampler(indices[split:num_train]),
  pin_memory=True, num_workers=2
)

scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
  optimizer, float(args.epochs), eta_min=args.learning_rate_min
)
```
> What is `CosineAnnealingLR`?

Then we have our usual training `for` loop:

```python
for epoch in range(args.epochs):
  scheduler.step()
  lr = scheduler.get_lr()[0]
  logging.info('epoch %d lr %e', epoch, lr)

  genotype = model.genotype()
  logging.info('genotype = %s', genotype)

  print(F.softmax(model.alphas_normal, dim=-1))
  print(F.softmax(model.alphas_reduce, dim=-1))

  # training
  train_acc, train_obj = train(train_queue, valid_queue, model, architect, criterion, optimizer, lr)
  logging.info('train_acc %f', train_acc)

  # validation
  valid_acc, valid_obj = infer(valid_queue, model, criterion)
  logging.info('valid_acc %f', valid_acc)

  utils.save(model, os.path.join(args.save, 'weights.pt'))
```

### train()

