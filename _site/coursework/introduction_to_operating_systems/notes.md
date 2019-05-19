TODO:
- Look at session 3 (`C Programming Examples`) and go
  through each of the code listings.
- Look at session 2 (`C Programming`) and write blog
  posts on each of the C concepts.
- Look at session 5 (`Command Line Example`) and run
  the hello world program locally.
- Learn about `Makefile`.

I am impatient. I will begin course now.

Course instructor: Ada Gavrilovska.

This is to prepare for CS6210, `Advanced Operating
Systems`.

What are Operating Systems? Why are they needed? How
are Operating Systems designed and implemented.

## Lesson 3
An OS is a piece of software that abstracts and
arbitrates the underlying hardware system. In this
context, abstract means to simplify what the hardware
actually looks like. Arbitrate means to manage, to
oversee, to control the hardware use.

An operating system is like a toy shop manager:
- Directs operational resources
	* control use of CPU, memory, peripheral
	  devices and so on
- Enforce working policies
	* fair resource access, limits to resource
	  usage, etc.
- mitigate difficulty of complex tasks
	* abstract hardware details (system calls)

An operating system is a layer of systems software
that:
1. directly has privileged access to the underlying
   hardware;
2. hides the hardware complexity;
3. manages hardware on behalf of one of more
   applications according to some predefined policies;
4. ensures that applications are isolated and protected
   from one another

`cache memory` is not a component of OS like `file
system`, `scheduler` or `device driver`. The hardware
manages `cache`.

Distributing memory between multiple processes ->
Arbitration.  Supporting different types of speakers ->
Abstraction.  Interchangeable access of hard disk or
SSD -> Abstraction.

OS elements: 
- Abstractions: process, thread, file, socket, memory
  page
- Mechanisms: create, schedule, open, write, allocate
- Policies: least-recently used (LRU), earliest
  deadline first (EDF)

Design Principles:
- Separation of mechanism & policy:
	* implement flexible mechanisms to support many
	  policies, e.g. LRU, LFU, random
- Optimize for common case:
	* where will the OS be used?
	* what will the user want to execute on that
	  machine?
	* what are the workload requirements?

User/Kernel Protection Boundary:
- Unprivileged user-level: applications
- Privileged kernel-level: OS kernel, privileged direct
  hardware access.

User-Kernel switch is supported by harware:
- trap instructions
- system call, ex: open (file), send (socket), mmap
  (memory)
- signals

### System Call Flowchart

Executing a system call involves changing the execution
context from the user process to the execution context
of the OS kernel, also passing arguments, whatever
necessary for the system cooperation, and then jumping
somewhere in the memory of the kernel so that you can
go through the instruction sequence that corresponds to
that system call. With the system call, control is
passes to the operating system. The OS operates in
privileged mode, and it is allowed to perform whatever
operation was specified in the system call. Once the
system call completes, it returns the results and the
control back to the calling process. This involves
changing the execution context from the kernel mode
into the user mode, passing any arguments back into the
user address space, and then jumping to the exact same
location in the execution of the user process where the
system call was being made from.

To make a system call, an application must:
1. write arguments,
2. save all relevant data at a well-defined location,
3. make the actual system call using the specific
   system call number.

The well defined location is necessary so that the OS
kernel based on the system call number can determine
which, how many arguments should retrieve, and where
are they, at this well defined location.

The arguments can either be passed directly between the
user program and the OS, or they can be passed
indirectly by specifying their address.

In synchronous mode, the process will wait until the
system call completes. We can also issue asynchronous
system calls, but we will discuss it later.

### Crossing the OS Boundary

User/kernel transitions are a necessary step during
application execution. The hardware provides support
for performing user/kernel transitions. The hardware
will cause a trap if the application from unprivileged
mode tries to perform some instruction or a memory
access for which it does not have permission. For
example, the application cannot change the contents of
certain registers and give itself more CPU or more
memory. Only the OS can do that. The result of this
trap is that the hardware initiates transfer of the
control to the OS/kernel, and marks this by a special
privileged bit. Once control is passed over to the OS,
the OS can check what caused the trap and determine the
appropriate thing to do: whether to grant or deny the
specific request that caused the trap to occur in the
first place. This will depend on the policies that are
supported by the OS. Performing all of this despite of
the fact that hardware provides support still takes a
number of instructions. For instance, on a 2GHz machine
running Linux, it can take 50-100 ns to perform all of
the operations that are necessary around a user-kernel
transition. This is real overhead for the system. The
other problem with these transitions is that they
affect the hardware cache usage. The application
performance is very dependent on the ability to use the
hardware cache. Accessing cache is order of few cycles,
accessing memory can be order of hundreds of cycles.
When we perform a system call, or in general, when we
cross into the OS, the OS while executing will likely
bring content that it needs in the cache. This will
replace some of the application content that was in the
hardware cache before the transaction was performed.
And so this will have some impact on the application
performance because it will no longer be able to access
its data in cache, it will have to go to memory.

In summary, these user/kernel transitions are not
cheap.

Because context switches will swap the data/address
currently in cache, the performance of applications can
benefit or suffer based on how a context switch changes
what is in cache at the time they are accessing it.

A cache would be considered `hot` if an application is
accessing the cache when it contains the data/address
it needs.

A cache would be considered `cold` if an application is
accessing the cache when it does not contain the
data/addresses it needs -- forcing it to retrieve
data/addresses from main memory.

### OS Services

An operating system provides applications with access
to the underlying hardware. It does so by exporting a
number of services. At the most basic level, these
services are directly linked to some of the components
of the hardware. For instance, there is a scheduling
component that is responsible for controlling the
access to the CPU or maybe there are even multiple
CPUs. The memory manager is responsible for allocating
the underlying physical memory to one or more
co-running applications. And it also has to make sure
that multiple applications don't overwrite each others
accesses to memory. A block device driver is
responsible for access to a block device like disk. In
addition, the OS also exports higher level services
that are linked with higher level abstractions as
opposed to those that are linked with abstractions that
really map to the hardware. For instance, the file is a
useful abstraction that is supported by virtually all
OSs. In principle, OSs integrate file system as a
service.

In summary, an OS will have to incorporate a
number of services in order to provide applications
and application developers with a number of useful
types of functionality. This includes:
* process management,
* file management,
* device management,
* memory management,
* storage management,
* security, and so forth. 

OS make all of these services available via system
calls.

Examples:
- Process Control
	* Windows: CreateProcess(), ExitProcess(),
	  WaitForSingleObject()
	* Unix: fork(), exit(), wait()
- File Manipulation
	* Windows: CreateFile(), ReadFile(),
	  WriteFile(), CloseHandle()
	* Unix: open(), read(), write(), close()
- Device Manipulation
	* Windows: SetConsoleMode(), ReadConsole(),
	  WriteConsole()
	* Unix: ioctl(), read(), write()
- Information Maintenance
	* Windows: GetCurrentProcessID(), SetTime(),
	  Sleep()
	* Unix: getpid(), alarm(), sleep()
- Communication
	* Windows: CreatePipe(), CreateFileMapping(),
	  MapViewOfFile()
	* Unix: pipe(), shmget(), mmap()
- Protection:
	* Windows: SetFileSecurity(),
	  InitializeSecurityDescriptor(),
SetSecurityDescriptorGroup()
	* Unix: chmod(), umask(), chown()

Although Windows and Unix are very different OSs, the
types of system calls and the abstractions around those
system calls each provide are very similar.

For 64-bit linux based OS:
To send a signal to a process, `kill` is the system
call. To set the group identity of a process, there is
a system call `setgid`. For 16 bit and 32 bit systems
it could be `setgid16` or `setgid32`. Mounting a file
system is done via the `mount` system call. Reading or
writing system parameters is done via the `sysctl`
system call.

### Monolithic OS

Let's look at different types of OS organizations. We
will start with `Monolithic` OS. Historically, the OS
had a monolithic design. That's when every possible
service that any one of the applications can require or
that any type of hardware will demand is already part
of the OS. For instance, such a monolithic OS may
include several possible file systems, where one is
specialized for sequential workloads where the workload
is sequentially accessing files when reading and
writing them; and then maybe other file system that is
optimized for random I/O. For instance, this is common
with databases - there isn't necessarily sequential
access there, rather each database operation can
randomly access any portion of the backing file. This
would clearly make the OS potentially really, really
large. The benefit of this approach is that everything
is included in the OS - the abstractions, all the
services, and everything is packaged at the same time.
And because of that, there are some possibilities for
some compile-time optimizations. The downside is that
there is too much state, too much code that's hard to
maintain, debug, upgrade and then its large size also
poses large memory requirements, and that can always
impact the performance that the applications are able
to observe.

Pros:
- everything included
- inlining, compile-time optimizations

Cons:
- customization, portability, manageability
- memory footprint
- performance

### Modular OS

[`set tw=100`]

A more common approach today is the modular approach, as with the Linux OS. This kind of OS has a
number of basic services and APIs already part of it. But more importantly, as the name suggests,
everything can be added as a module.  With this approach, you can easily customize which particular
file system or scheduler the OS uses. This is possible because the OS specifies certain interfaces
that any module must implement in order to be part of the OS. And then dynamically, depending on the
workload, we can install a module that implements this interface in a way that makes sense for this
workload. Like, if these are database applications, we may run the file system that's optimized for
random file access. And if these are some other types of computations, we may run the file system
that's optimized for sequential access.

Most importantly, we can dynamically add new modules in the OS.

The benefits of this approach is:
- its easier to maintain and upgrade
- it also has a smaller code base
- less resource intensive, which means that it will leave more resources, more memory for the
  applications. This can lead to better performance as well.

The downside of this approach is:
- although modularity may be good for maintainability, the level of interaction that it requires,
  because we have to go through this interface specification before we actually go into the
implementation of a particular service. This can reduce some opportunities for optimizations.
Ultimately, this can have some impact on performance, though typically, not very significant.
- maintenance, however, can still be an issue given that these modules may come from completely
  disparate code bases and can be a source of bugs.

But overall, this approach delivers significant improvements over the monolithic approach, and it's
the one that's more commonly used today.

### Microkernel

Another example of OS design is what we call a microkernel. Microkernels only require the most basic
primitives at the OS level. For instance, at the OS level, the microkernel can support some basic
services such as to represent an executing application, its address space...
