# Core python3 interview cheatsheet

# Table of contents

1. [Python types](#python-types)
   1. [Truth Value Testing](#truth-value-testing)
   2. [Boolean operations](#boolean-operations)
   3. [Comparison](#comparison)
   4. [Numeric Types](#numeric-types)
   5. [Additional methods for Integer types](#additional-methods-for-integer-types)
   6. [Additional methods for Float types](#additional-methods-for-float-types)
   7. [Hashing of numeric types](#hashing-of-numeric-types)
   8. [Iterator types](#iterator-types)
   9. [Generator types](#generator-types)
   10. [Sequence Types](#sequence-types)
       1. [Lists](#lists)
       2. [Tuples and namedtuples](#tuples-and-namedtuples)
       3. [Ranges](#ranges)
       4. [Strings](#strings)
       5. [Bytes](#bytes)
       6. [Bytearrays](#bytearrays)
       7. [Sets and frozensets](#sets-and-frozensets)
       8. [Mapping objects (dictionaries)](#mapping-objects)
2. [Threading](#threading)
   1. [`Thread` Class](#thread-class)
   2. [Locks](#locks)
   3. [RLocks](#rlocks)
   4. [Conditions](#conditions)
   5. [Semaphores](#semaphores)
   6. [BoundedSemaphores](#bounded-semaphores)
   7. [Timers](#timers)
   8. [Barriers](#barriers)
   9. [Context manager](#threading-context-manager)
3. [Multiprocessing](#multiprocessing)
   1. [Pools](#pools)
   2. [The `Process` class](#process-class)
   3. [Starting a process](#starting-a-process)
   4. [Exchanging data between processes](#data-exchange-processes)
   5. [Syncing processes](#syncing-processes)
   6. [Sharing states between processes](#sharing-states-between-processes)
   7. [Multithreading vs multiprocessing](#threading-vs-mprocessing)
4. [AsyncIO](#asyncio)
   1. [asyncio.run()](#asyncio_run)
   2. [Runner](#runner)
   3. [Coroutines](#coroutines)
   4. [Awaitables](#awaitables)
   5. [Task groups](#task-groups)
   6. [Sleep](#asyncio-sleep)
   7. [Running coroutines in threads](#coroutine-thread)
5. [Generators](#generators)
6. [Decorators](#decorators)
7. [Garbage collection](#garbage-collection)
8. [Fluent python](#fluent-python)
9. [References](#references)

## 1. Python types <a name="python-types"></a>

**Mutable** data types are those whose values can be changed or new values can be assigned to them.
**Immutable** data types are those, whose values cannot be modified once they are created.

| Mutable types | Immutable types |
| ------------- | --------------- |
| Lists         | Numbers         |
| Sets          | Strings         |
| Dictionaries  | Tuples          |
| Bytearray     | Frozen Sets     |
|               | Bytes           |

```python
# You can use type(<SOMETHING>) to figure out what type is something
type(1) # int
type(2.8) # float
type("hello") # str
```

### 1.1 Truth Value Testing <a name="truth-value-testing"></a>

By default an object is True unless `__bool__()` method returns False or `__len__()` returns 0.
What objects are considered false:

- `None` and `False`
- 0 of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`
- empty sequences and collections: `''`, `()`, `[]`

### 1.2 Boolean operations <a name="boolean-operations"></a>

`and`, `or`, `not`

| Operation | Result                               |
| --------- | ------------------------------------ |
| `x or y`  | if x false, then y else x            |
| `x and y` | if x false, then x else y            |
| `not x`   | if x false, then `True` else `False` |

### 1.3 Comparison <a name="comparison"></a>

| Operation | Meaning                 |
| --------- | ----------------------- |
| `<`       | strictly less than      |
| `<=`      | less than or equal      |
| `>`       | strictly greater than   |
| `>=`      | greater than or equal   |
| `==`      | equal                   |
| `!=`      | not equal               |
| `is`      | object identity         |
| `is not`  | negated object identity |

Different object types (non numerical) always compare `False`.
Equality can be overwritten with use of `__eq__()`
Comparisons can be defined with the use of:

- `__lt__()` # <
- `__le__()` # <=
- `__gt__()` # >
- `__ge__()` # >=

Two more operations with the same syntactic priority, `in` and `not in`, are supported by types that are iterable or implement the `__contains__()` method.

### 1.4 Numeric Types <a name="numeric-types"></a>

There are three numeric types for Python

- integer : `int`
- floating-point : `float`
- complex : `complex`

Booleans are a subtype of integers.

Complex numbers have a `real` and `imaginary` part, which are each a floating point number. To extract these parts from a complex number z, use `z.real` and `z.imag`.

(The standard library includes the additional numeric types `fractions.Fraction`, for rationals, and `decimal.Decimal`, for floating-point numbers with user-definable precision.)

Know issue with float representation:

```python
>>>format(0.1, '.17f')
'0.10000000000000001'
```

Why is there a 1 at the end?
Because Python floats uses `IEEE-745` to map double precision which contains 53 bits of precision so the computer tries to converts `0.1` for example to the closest fraction it knows using an integer that contains exactly 53 bits.
In order to deal with this issue `decimal.Decimal` is used because it has custom rounding options and a lot higher precision than `float`.

Numeric Operations:

| Operation        | Result                                                                      |
| ---------------- | --------------------------------------------------------------------------- |
| `x+y`            | sum of x and y                                                              |
| `x-y`            | difference of x and y                                                       |
| `x*y`            | product of x and y                                                          |
| `x/y`            | quotient of x and y                                                         |
| `x//y`           | floored quotient of x and y                                                 |
| `x%y`            | remainder of `x/y`                                                          |
| `-x`             | negated x                                                                   |
| `+x`             | x unchanged                                                                 |
| `abs(x)`         | absolute value or magnitude of x                                            |
| `int(x)`         | x converted to integer                                                      |
| `float(x)`       | x converted to floating point                                               |
| `complex(re,im)` | a complex number with real part re, imaginary part im. im defaults to zero. |
| `c.conjugate()`  | conjugate of the complex number c                                           |
| `divmod(x,y)`    | pair `(x//y,x%y)`                                                           |
| `pow(x,y)`       | x to the power of y                                                         |
| `x**y`           | x to the power of y                                                         |

`x//y` known as integer division. The result is always rounded towards minus infinity and is an integer.

For additional numeric operations use `math` and `cmath` modules.

Bitwise Operations:

| Operation | Result                          |
| --------- | ------------------------------- |
| `x \| y`  | bitwise or of x and y           |
| `x \^ y`  | bitwise exclusive or of x and y |
| `x \& y`  | bitwise and of x and y          |
| `x << n`  | x shifted left by n bits        |
| `x >> n`  | x shifted right by n bits       |
| `~x`      | inverted bits of x              |

### 1.5 Additional methods for Integer types <a name="additional-methods-for-integer-types"></a>

```python
int.bit_length()
```

Returns the number of bits necessary to represent an integer in binary excluding sign and leading zeros

```python
int.bit_count()
```

Return the number of ones in the binary representation of the absolute value of the integer. This is also known as the population count.

```python
int.to_bytes()
```

Return an array of bytes representing an integer.

```python
#classmethod
int.from_bytes
```

Return the integer represented by the given array of bytes.

```python
int.as_integer_ratio()
```

Return a pair of integers whose ratio is exactly equal to the original integer and with a positive denominator.The integer ratio of integers (whole numbers) is always the integer as the numerator and 1 as the denominator.

### 1.6 Additional methods for Float types <a name="additional-methods-for-float-types"></a>

```python
float.as_integer_ratio()
```

Return a pair of integers whose ratio is exactly equal to the original float and with a positive denominator. Raises `OverflowError` on infinities and a `ValueError` on NaNs.

```python
float.is_integer()
```

Return True if the float instance is finite with integral value, and False otherwise.

```python
float.hex()
```

Return a representation of a floating-point number as a hexadecimal string. For finite floating-point numbers, this representation will always include a leading 0x and a trailing p and exponent.

```python
#classmethod
float.fromhex(s)
```

Class method to return the `float` represented by a hexadecimal string s. The string s may have leading and trailing whitespace. A hexadecimal string takes this form:

```
[sign] ['0x'] integer ['.' fraction] ['p' exponent]
```

### 1.7 Hashing of numeric types <a name="hashing-of-numeric-types"></a>

For numbers x and y, possibly of different types, it’s a requirement that `hash(x) == hash(y)` whenever `x == y`

### 1.8 Iterator types <a name="iterator-types"></a>

Python supports a concept of iteration over containers. This is implemented using two distinct methods; these are used to allow user-defined classes to support iteration. Sequences, described below in more detail, always support the iteration methods.

```python
container.__iter__()
```

Return an iterator object. The object is required to support the iterator protocol described below. If a container supports different types of iteration, additional methods can be provided to specifically request iterators for those iteration types.

The iterator objects themselves are required to support the following two methods, which together form the iterator protocol:

```python
iterator.__iter__()
```

Return the `iterator` object itself. This is required to allow both containers and iterators to be used with the `for` and `in` statements.

```python
iterator.__next__()
```

Return the next item from the iterator. If there are no further items, raise the `StopIteration` exception.

Python defines several iterator objects to support iteration over general and specific sequence types, dictionaries, and other more specialized forms. The specific types are not important beyond their implementation of the iterator protocol.

Once an iterator’s `__next__()` method raises `StopIteration`, it must continue to do so on subsequent calls. Implementations that do not obey this property are deemed broken.

### 1.9 Generator types <a name="generator-types"></a>

Python’s generators provide a convenient way to implement the iterator protocol. If a container object’s `__iter__()` method is implemented as a generator, it will automatically return an iterator object (technically, a generator object) supplying the `__iter__()` and `__next__()` methods.

### 1.10 Sequence Types <a name="sequence-types"></a>

There are three basic sequence types: `lists`, `tuples`, and `range` objects. They all inherit their common operations from `collections.abc.Sequence` which is an ABC.

Known sequence operations are
(s is the notation for a sequence):
| Operation | Result |
|-----------|--------|
|`x in s`| True if x is in the s|
|`x not in s`| True if x is not in the s|
|`s1 + s2`| concatenation of s1 and s2, concatenating immutable types will create a new sequence|
|`s * n or n * s`| adding s to itself n times, this only creates references to s, n times, not new sequences|
|`s[i]`| i'th element of s, starting from 0|
|`s[i:j]`|slice of s from i to j, without including j, this creates a new sequence|
|`s[i:j:k]`|slice of s from i to j with a step of k, without including j, this creates a new sequence|
|`len(s)`|length of s|
|`min(s)`|smallest item of s|
|`max(s)`|largest item of s|
|`s.index(x)`|index of value x in s|
|`s.count(x)`|number of instances of x in s|

The only operation that immutable sequence types generally implement that is not also implemented by mutable sequence types is support for the `hash()` built-in.

The operations in the following table are defined on mutable sequence types. The `collections.abc.MutableSequence` ABC is provided to make it easier to correctly implement these operations on custom sequence types.

| Operation               | Result                                                                                    |
| ----------------------- | ----------------------------------------------------------------------------------------- |
| `s[i] = x`              | item with index i from s is replaced by x                                                 |
| `s[i:j] = t`            | slice of s from i to j is replaced by iterable t                                          |
| `del s[i:j]`            | same as `s[i:j] = []`                                                                     |
| `s[i:j:k] = t`          | slice of s from i to j with a step of k is replaced by iterable t                         |
| `del s[i:j:k]`          | remove elements from i to j with a step of k from s                                       |
| `s.append(x)`           | appends x to the sequence                                                                 |
| `s.clear()`             | same as `del s[:]`                                                                        |
| `s.copy()`              | creates a shallow copy of s, same as `s[:]`                                               |
| `s.extend(t) or s += t` | extends s with the contents of t                                                          |
| `s *= n`                | updates s with its contents repeated n times, items are not copied but referenced n times |
| `s.insert(i, x)`        | inserts the x object at index i                                                           |
| `s.pop() or s.pop(i)`   | retrieves the item at index i and also removes it, default i is -1 (last item)            |
| `s.remove(x)`           | removes first occurrence of x in s                                                        |
| `s.reverse()`           | reverses s, it modifies the structure in place without creating a new one                 |

A **shallow copy** means constructing a new collection object and then populating it with **references to the child objects found in the original**. In essence, a shallow copy is only one level deep. The copying process does not recurse and therefore won’t create copies of the child objects themselves.

A **deep copy** makes the copying process **recursive**. It means **first constructing a new collection object and then recursively populating it with copies of the child objects found in the original**. Copying an object this way walks the whole object tree to create a **fully independent clone of the original object and all of its children**.

#### 1.10.1 Lists <a name="lists"></a>

**Lists** are **mutable** sequences used to store collections of items.

`class list([iterable])` is the list constructor. Constructor builds a list of items in the same order as iterable's items.

Lists implement all common and mutable sequence operations and also provide the method `sort(*, key=None, reverse=False)`. Key being the item of comparison and reverse is a boolean used to reverse the sorted list or not. This method modifies the sequence in place instead of creating a new one, use `sorted()` to generate a new sequence if needed.

#### 1.10.2 Tuples and namedtuples <a name="tuples-and-namedtuples"></a>

**Tuples** are **immutable** sequences used to store collections of heterogeneous data. Tuples are also used for cases where an immutable sequence of homogeneous data is needed.

`class tuple([iterable])` is the tuple constructor. Constructor builds a tuple of items in the same order as iterable's items. Note that it is actually the **comma which makes a tuple, not the parentheses**. The parentheses are optional, except in the empty tuple case, or when they are needed to avoid syntactic ambiguity.

For heterogeneous collections of data where access by name is clearer than access by index, `collections.namedtuple()` may be a more appropriate choice than a simple tuple object. `collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)`.
Example:

```python
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
```

#### 1.10.3 Ranges <a name="ranges"></a>

**Ranges** are **immutable** sequences of numbers and are commonly used for looping a specific number of times in for loops.

`class range(stop)` or `class range(start, stop[, step])`

The arguments to the range constructor must be integers (either built-in int or any object that implements the `__index__()` special method)

Ranges implement all of the common sequence operations **except concatenation and repetition** (due to the fact that range objects can only represent sequences that follow a strict pattern and repetition and concatenation will usually violate that pattern).The advantage of the range type over a regular list or tuple is that a range **object will always take the same (small) amount of memory**, no matter the size of the range it represents (as **it only stores the start, stop and step values**, calculating individual items and subranges as needed).

#### 1.10.4 Strings <a name="strings"></a>

Textual data in Python is handled with `str` objects, or **strings**. Strings are **immutable** sequences of Unicode code points.
The `r` (“raw”) prefix that disables most escape sequence processing.

`class str(object='')` or
`class str(object=b'', encoding='utf-8', errors='strict')` are the str constructors. If object does not have a `__str__()` method, then str() falls back to returning `repr(object)`.

#### 1.10.5 Bytes <a name="bytes"></a>

**Bytes** objects are **immutable** sequences of single bytes. Since many major binary protocols are based on the ASCII text encoding, bytes objects offer several methods that are only valid when working with ASCII compatible data and are closely related to string objects in a variety of other ways.

`class bytes([source[, encoding[, errors]]])`.

Firstly, the syntax for bytes literals is largely the same as that for string literals, except that a **b prefix is added**:

1.Single quotes: b'still allows embedded "double" quotes'

2.Double quotes: b"still allows embedded 'single' quotes"

3.Triple quoted: b'''3 single quotes''', b"""3 double quotes"""

#### 1.10.6 Bytearrays <a name="bytearrays"></a>

**Bytearray** objects are a **mutable** counterpart to bytes objects.

`class bytearray([source[, encoding[, errors]]])`.
There are no other ways then the constructor to create bytearray objects.

#### 1.10.7 Sets and frozensets <a name="sets-and-frozensets"></a>

A **set** object is an **unordered** collection of **distinct hashable objects**. Common uses include membership testing, removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference, and symmetric difference.

Like other collections, sets support `x in set`, `len(set)`, and `for x in set`. Being an **unordered collection**, sets **do not record element position or order of insertion**. Accordingly, sets do not support indexing, slicing, or other sequence-like behavior.

**set** is mutable, contents can be changed with methods like `add()` or `remove()`. Since it is mutable it has no hash value so it cannot be used as dictionary key or element of another set.
**frozenset** is immutable and hashable.

**sets** can be created like this:

```python
{'hello','world'}
```

or the constructor `class set([iterable])`
**frozenset** can be created like this:
`class frozenset([iterable])`

Return a new set or frozenset object whose elements are taken from iterable. The elements of a set **must be hashable**. To represent sets of sets, the inner sets must be frozenset objects. If iterable is not specified, a new empty set is returned.

**Set operations:**

`update(*others)`
`set |= other | ...`
Update the set, adding elements from all others.

`intersection_update(*others)`
`set &= other & ...`
Update the set, keeping only elements found in it and all others.

`difference_update(*others)`
`set -= other | ...`
Update the set, removing elements found in others.

`symmetric_difference_update(other)`
`set ^= other`
Update the set, keeping only elements found in either set, but not in both.

`add(elem)`
Add element elem to the set.

`remove(elem)`
Remove element elem from the set. Raises KeyError if elem is not contained in the set.

`discard(elem)`
Remove element elem from the set if it is present.

`pop()`
Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.

`clear()`
Remove all elements from the set.

#### 1.11 Mapping objects (dictionaries) <a name="mapping-objects"></a>

A **mapping object** maps **hashable** values to arbitrary objects. Mappings are **mutable** objects. There is currently only one standard mapping type, the **dictionary**.

Dictionaries preserve insertion order. Note that updating a key does not affect the order. Keys added after deletion are inserted at the end.

Dictionary view objects
The objects returned by dict.keys(), dict.values() and dict.items() are view objects. They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.

## 2.Threading <a name="threading"></a>

### 2.1 `Thread` Class <a name="thread-class"></a>

The Thread class represents an activity that is run in a separate thread of control. There are two ways to specify the activity: by passing a callable object to the constructor, or by overriding the `run()` method in a subclass. No other methods (except for the constructor) should be overridden in a subclass. In other words, only override the `__init__()` and `run()` methods of this class.

Once a thread object is created, its activity must be started by calling the thread’s `start()` method. This invokes the `run()` method in a separate thread of control.

Once the thread’s activity is started, the thread is considered ‘alive’. It stops being alive when its `run()` method terminates – either normally, or by raising an unhandled exception. The `is_alive()` method tests whether the thread is alive.

Other threads can call a thread’s `join()` method. This **blocks the calling thread** until the thread whose `join()` method is called is **terminated**.

A thread has a **name**. The name can be passed to the constructor, and read or changed through the `name` attribute.

If the `run()` method raises an exception, `threading.excepthook()` is called to handle it. By default, `threading.excepthook()` ignores silently `SystemExit`.

A thread can be flagged as a **“daemon thread”**. The significance of this flag is that **the entire Python program exits when only daemon threads are left**. The initial value is inherited from the creating thread. The flag can be set through the `daemon` property or the `daemon` constructor argument.

There is a **“main thread”** object; this corresponds to the **initial thread of control in the Python program**. It is not a daemon thread.

The Thread constructor is:

```python
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
```

**group** should be `None`; reserved for future extension when a `ThreadGroup` class is implemented.

**target** is the callable object to be invoked by the `run()` method. Defaults to `None`, meaning nothing is called.

**name** is the thread name. By default, a unique name is constructed of the form **“Thread-N”** where **N** is a small decimal number, or **“Thread-N (target)”** where “target” is `target.__name__` if the target argument is specified.

**args** is a list or tuple of arguments for the target invocation. Defaults to ().

**kwargs** is a dictionary of keyword arguments for the target invocation. Defaults to {}.

If not None, daemon explicitly sets whether the thread is daemonic. If None (the default), the daemonic property is inherited from the current thread.

Thread object methods and properties:

1. `start()` :
   Start the thread’s activity. It must be called at most once per thread object. It arranges for the object’s run() method to be invoked in a separate thread of control.

2. `run()` : Method representing the thread’s activity.
   The standard `run()` method invokes the callable object passed to the object’s constructor as the target argument, if any, with positional and keyword arguments taken from the args and kwargs arguments, respectively.
3. `join(timeout=None)` : Wait until the thread terminates. This blocks the calling thread until the thread whose `join()` method is called terminates – either normally or through an unhandled exception – or until the optional timeout occurs. When the timeout argument is present and not None, it should be a floating point number specifying a timeout for the operation in seconds (or fractions thereof). As `join()` always returns None, you must call `is_alive()` after `join()` to decide whether a timeout happened – if the thread is still alive, the `join()` call timed out. A thread can be joined many times.
4. `name` : Name of the thread
5. `ident` : Thread identifier
6. `native_id` : Thread ID from the OS
7. `is_alive()` : This method returns True just before the run() method starts until just after the run() method terminates.
8. `daemon` : A boolean value indicating whether this thread is a daemon thread (True) or not (False)

## 2.2 Locks <a name="locks"></a>

A primitive lock is in one of two states, **“locked”** or **“unlocked”**. It is created in the unlocked state. It has two basic methods, `acquire()` and `release()`. When the state is **unlocked**, `acquire()` changes the state to **locked** and returns immediately. When the state is **locked**, `acquire()` blocks until a call to `release()` in another thread changes it to **unlocked**, then the `acquire()` call resets it to **locked** and returns. The `release()` method should only be called in the **locked state**; it changes the state to **unlocked** and returns immediately. If an attempt is made to **release an unlocked lock**, a RuntimeError will be raised.

When more than one thread is blocked in `acquire()` waiting for the state to turn to unlocked, only one thread proceeds when a `release()` call resets the state to unlocked; which one of the waiting threads proceeds is not defined, and may vary across implementations.

Lock methods, all of them are executed atomically (meaning one at the time):

1. `acquire(blocking=True, timeout=-1)` : Acquire a lock, blocking or non-blocking. When invoked with the blocking argument set to True (the default), block until the lock is unlocked, then set it to locked and return True. When invoked with the blocking argument set to False, do not block. If a call with blocking set to True would block, return False immediately; otherwise, set the lock to locked and return True. When invoked with the floating-point timeout argument set to a positive value, block for at most the number of seconds specified by timeout and as long as the lock cannot be acquired. A timeout argument of -1 specifies an unbounded wait. It is forbidden to specify a timeout when blocking is False. The return value is True if the lock is acquired successfully, False if not (for example if the timeout expired).

2. `release()` : Release a lock. This can be called from any thread, not only the thread which has acquired the lock. When the lock is locked, reset it to unlocked, and return. If any other threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed. When invoked on an unlocked lock, a RuntimeError is raised. There is no return value.

3. `locked()` : Return True if the lock is acquired.

## 2.3 RLocks <a name="rlocks"></a>

A reentrant lock must be released by the thread that acquired it. Once a thread has acquired a reentrant lock, the same thread may acquire it again without blocking; the thread must release it once for each time it has acquired it.

An RLock can be acquired multiple times by a thread but also needs to be released for each time it is acquired in order to be available to other threads.

Note that RLock is actually a factory function which returns an instance of the most efficient version of the concrete RLock class that is supported by the platform.

RLock methods:

1. `acquire(blocking=True, timeout=-1)` : Acquire a lock, blocking or non-blocking. When invoked without arguments: if this thread already owns the lock, increment the recursion level by one, and return immediately. Otherwise, if another thread owns the lock, block until the lock is unlocked. Once the lock is unlocked (not owned by any thread), then grab ownership, set the recursion level to one, and return. If more than one thread is blocked waiting until the lock is unlocked, only one at a time will be able to grab ownership of the lock. There is no return value in this case. When invoked with the blocking argument set to True, do the same thing as when called without arguments, and return True. When invoked with the blocking argument set to False, do not block. If a call without an argument would block, return False immediately; otherwise, do the same thing as when called without arguments, and return True. When invoked with the floating-point timeout argument set to a positive value, block for at most the number of seconds specified by timeout and as long as the lock cannot be acquired. Return True if the lock has been acquired, False if the timeout has elapsed.

2. `release()` : Release a lock, decrementing the recursion level. If after the decrement it is zero, reset the lock to unlocked (not owned by any thread), and if any other threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed. If after the decrement the recursion level is still nonzero, the lock remains locked and owned by the calling thread.

## 2.4 Conditions <a name="conditions"></a>

A condition variable allows one or more threads to wait until they are notified by another thread.
Constructor: `class threading.Condition(lock=None)` : If the lock argument is given and not None, it must be a Lock or RLock object, and it is used as the underlying lock. Otherwise, a new RLock object is created and used as the underlying lock.

Condition methods:

1. `acquire(*args)` : Acquire the underlying lock. This method calls the corresponding method on the underlying lock; the return value is whatever that method returns.

2. `release()` : Release the underlying lock. This method calls the corresponding method on the underlying lock; there is no return value.

3. `wait(timeout=None)` : Wait until notified or until a timeout occurs. If the calling thread has not acquired the lock when this method is called, a RuntimeError is raised. This method releases the underlying lock, and then blocks until it is awakened by a `notify()` or `notify_all()` call for the same condition variable in another thread, or until the optional timeout occurs. Once awakened or timed out, it re-acquires the lock and returns.

4. `wait_for(predicate, timeout=None)` : Wait until a condition evaluates to true. predicate should be a callable which result will be interpreted as a boolean value. A timeout may be provided giving the maximum time to wait.

5. `notify(n=1)` : By default, wake up one thread waiting on this condition, if any. If the calling thread has not acquired the lock when this method is called, a RuntimeError is raised. This method wakes up at most n of the threads waiting for the condition variable; it is a no-op if no threads are waiting.

6. `notify_all()` : Wake up all threads waiting on this condition. This method acts like `notify()`, but wakes up all waiting threads instead of one.

## 2.5 Semaphores <a name="semaphores"></a>

A semaphore manages an internal counter which is decremented by each `acquire()` call and incremented by each `release()` call. The counter can never go below zero; when `acquire()` finds that it is zero, it blocks, waiting until some other thread calls `release()`.

Constructor: `class threading.Semaphore(value=1)` : This class implements semaphore objects. A semaphore manages an atomic counter representing the number of release() calls minus the number of acquire() calls, plus an initial value. The acquire() method blocks if necessary until it can return without making the counter negative. If not given, value defaults to 1. The optional argument gives the initial value for the internal counter; it defaults to 1. If the value given is less than 0, ValueError is raised.

Semaphore methods:

1. `acquire(blocking=True, timeout=None)` : If the internal counter is larger than zero on entry, decrement it by one and return True immediately. If the internal counter is zero on entry, block until awoken by a call to release(). Once awoken (and the counter is greater than 0), decrement the counter by 1 and return True. Exactly one thread will be awoken by each call to release(). The order in which threads are awoken should not be relied on.

2. `release(n=1)` : Release a semaphore, incrementing the internal counter by n. When it was zero on entry and other threads are waiting for it to become larger than zero again, wake up n of those threads.

## 2.6 BoundedSemaphores <a name="bounded-semaphores"></a>

Class implementing bounded semaphore objects. A bounded semaphore checks to make sure its current value doesn’t exceed its initial value. If it does, ValueError is raised. In most situations semaphores are used to guard resources with limited capacity. If the semaphore is released too many times it’s a sign of a bug. If not given, value defaults to 1.

## 2.7 Events <a name="events"></a>

This is one of the simplest mechanisms for communication between threads: one thread signals an event and other threads wait for it. An event object manages an internal flag that can be set to true with the set() method and reset to false with the clear() method. The wait() method blocks until the flag is true.

Event methods:

1. `is_set()` : Return True if and only if the internal flag is true.
2. `set()` : Sets the internal flag to True. All threads waiting for it to become true are awakened Threads that call wait() once the flag is true will not block at all.
3. `clear()` : Reset the internal flag to false. Subsequently, threads calling wait() will block until set() is called to set the internal flag to true again.
4. `wait(timeout=None)` : Block until the internal flag is set to True.

## 2.8 Timers <a name="timers"></a>

This class represents an action that should be run only after a certain amount of time has passed — a timer. Timer is a subclass of Thread and as such also functions as an example of creating custom threads.
Timers are started, as with threads, by calling their start() method. The timer can be stopped (before its action has begun) by calling the cancel() method. The interval the timer will wait before executing its action may not be exactly the same as the interval specified by the user.

Example:

```python
def hello():
    print("hello, world")

t = Timer(30.0, hello)
t.start()  # after 30 seconds, "hello, world" will be printed
```

Class constructor: `class threading.Timer(interval, function, args=None, kwargs=None)` : Create a timer that will run function with arguments args and keyword arguments kwargs, after interval seconds have passed. If args is None (the default) then an empty list will be used. If kwargs is None (the default) then an empty dict will be used.

Timer methods:

1. `start()` : Starts timer, at the end of the set time the function is executed
2. `cancel()` : Stop the timer, and cancel the execution of the timer’s action. This will only work if the timer is still in its waiting stage.

### 2.9 Barriers <a name="barriers"></a>

This class provides a simple synchronization primitive for use by a fixed number of threads that need to wait for each other. Each of the threads tries to pass the barrier by calling the wait() method and will block until all of the threads have made their wait() calls. At this point, the threads are released simultaneously.

The barrier can be reused any number of times for the same number of threads.

Barrier constructor: `class threading.Barrier(parties, action=None, timeout=None)`

Barrier methods and attributes:

1. `wait(timeout=None)` : Pass the barrier. When all the threads party to the barrier have called this function, they are all released simultaneously. If a timeout is provided, it is used in preference to any that was supplied to the class constructor. The return value is an integer in the range 0 to parties – 1, different for each thread. This can be used to select a thread to do some special housekeeping. If an action was provided to the constructor, one of the threads will have called it prior to being released. Should this call raise an error, the barrier is put into the broken state.
2. `reset()` : Return the barrier to the default, empty state. Any threads waiting on it will receive the BrokenBarrierError exception.
3. `abort()` : Put the barrier into a broken state. This causes any active or future calls to wait() to fail with the BrokenBarrierError.
4. `parties` : The number of threads required to pass the barrier.
5. `n_waiting` : The number of threads waiting to pass the barrier.
6. `broken` : A boolean that is True if the barrier is in the broken state.

### 2.10 Context manager <a name="threading-context-manager"></a>

All of the objects provided by this module that have acquire() and release() methods can be used as context managers for a with statement. Currently, Lock, RLock, Condition, Semaphore, and BoundedSemaphore objects may be used as with statement context managers. The acquire() method will be called when the block is entered, and release() will be called when the block is exited. Hence, the following snippet:

```python
with some_lock:
    # do something...
#Is equivalent to

some_lock.acquire()
try:
    # do something...
finally:
    some_lock.release()
```

## 3. Multiprocessing <a name="multiprocessing"></a>

multiprocessing is a package that supports spawning processes using an API similar to the threading module. The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine. It runs on both Unix and Windows.

### 3.1 Pools <a name="pools"></a>

A prime example of this is the Pool object which offers a convenient means of parallelizing the execution of a function across multiple input values, distributing the input data across processes (data parallelism). The following example demonstrates the common practice of defining such functions in a module so that child processes can successfully import that module. This basic example of data parallelism using Pool:

```python
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
```

Will print:

```python
[1, 4, 9]
```

### 3.2 The `Process` class <a name="process-class"></a>

In multiprocessing, processes are spawned by creating a Process object and then calling its start() method. Process follows the API of threading.Thread. A trivial example of a multiprocess program is:

```python
from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
```

### 3.3 Starting a process <a name="starting-a-process"></a>

Depending on the platform there are multiple ways to start a process:

1. **spawn** : The parent process starts a fresh Python interpreter process. The child process will only inherit those resources necessary to run the process object’s run() method. In particular, unnecessary file descriptors and handles from the parent process will not be inherited. Starting a process using this method is rather slow compared to using fork or forkserver. Available on Unix and Windows. The default on Windows and macOS.
2. **fork** : The parent process uses os.fork() to fork the Python interpreter. The child process, when it begins, is effectively identical to the parent process. All resources of the parent are inherited by the child process. Note that safely forking a multithreaded process is problematic. Available on Unix only. The default on Unix.
3. **forkserver** : When the program starts and selects the forkserver start method, a server process is started. From then on, whenever a new process is needed, the parent process connects to the server and requests that it fork a new process. The fork server process is single threaded so it is safe for it to use os.fork(). No unnecessary resources are inherited. Available on Unix platforms which support passing file descriptors over Unix pipes.

### 3.4 Exchanging data between processes <a name="data-exchange-processes"></a>

multiprocessing supports two types of communication channel between processes:

1. Queue :

```python
from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()
```

2. Pipe :
   The Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex (two-way). The two connection objects returned by Pipe() represent the two ends of the pipe. Each connection object has send() and recv() methods (among others). Note that data in a pipe may become corrupted if two processes (or threads) try to read from or write to the same end of the pipe at the same time. Of course there is no risk of corruption from processes using different ends of the pipe at the same time. For example:

```python
from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()
```

### 3.5 Syncing processes <a name="syncing-processes"></a>

Multiprocessing contains equivalents of all the synchronization primitives from threading. For instance one can use a lock to ensure that only one process prints to standard output at a time:

```python
from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()
```

### 3.6 Sharing states between processes <a name="sharing-states-between-processes"></a>

```python
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
```

or using a Manager

```python
from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)
```

### 3.7 Multithreading vs multiprocessing <a name="threading-vs-mprocessing"></a>

By formal definition, `multithreading` refers to the `ability of a processor to execute multiple threads concurrently`, where each `thread runs a process`. Whereas `multiprocessing` refers to the `ability of a system to run multiple processors concurrently`, where each `processor can run one or more threads`.

Multithreading works with multiple threads share the same code, data, and files but run on a different register and stack. Multiprocessing multiplies a single processor — replicating the code, data, and files, which incurs more overhead.

## 4. AsyncIO <a name="asyncio"></a>

asyncio is a library to write concurrent code using the async/await syntax.

asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.

asyncio is often a perfect fit for IO-bound and high-level structured network code.

### 4.1 `Asyncio.RUN` <a name="asyncio_run"></a>

`asyncio.run(coro, *, debug=None)`

Execute the coroutine `coro` and return the result.

If `debug` is `True`, the event loop will be `run in debug mode`. `False` disables debug mode explicitly. `None` is used to respect the `global Debug Mode settings`.

```python
async def main():
    await asyncio.sleep(1)
    print('hello')

asyncio.run(main())
```

### 4.2 Runner Context Manager <a name="runner"></a>

`class asyncio.Runner(*, debug=None, loop_factory=None)`

`loop_factory` could be used for overriding the `loop creation`. It is the responsibility of the `loop_factory` to set the `created loop` as the current one. By default `asyncio.new_event_loop()` is used and set as current event loop with `asyncio.set_event_loop()` if loop_factory is None.

```python
async def main():
    await asyncio.sleep(1)
    print('hello')

with asyncio.Runner() as runner:
    runner.run(main())
```

### 4.3 Coroutines <a name="coroutines"></a>

Coroutines declared with the async/await syntax is the preferred way of writing asyncio applications. For example, the following snippet of code prints “hello”, waits 1 second, and then prints “world”:

```python
import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())
```

Note that simply calling a coroutine will not schedule it to be executed:

To actually run a coroutine, asyncio provides the following mechanisms:

- The `asyncio.run()`
- Awaiting the coroutine.
- The `asyncio.create_task()` function to run coroutines concurrently as `asyncio Tasks`. `Tasks` are used to run coroutines in event loops. If a coroutine awaits on a Future, the Task suspends the execution of the coroutine and waits for the completion of the Future. When the Future is done, the execution of the wrapped coroutine resumes.
- The `asyncio.TaskGroup` class provides a more modern alternative to create_task(). Using this API:

```python
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1, 'hello'))

        task2 = tg.create_task(
            say_after(2, 'world'))

        print(f"started at {time.strftime('%X')}")
```

### 4.4 Awaitables <a name="awaitables"></a>

We say that an object is an awaitable object if it can be used in an await expression. Many asyncio APIs are designed to accept awaitables.

There are three main types of awaitable objects: `coroutines, Tasks, and Futures`.

Coroutines:

```python
import asyncio

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())
```

Important In this documentation the term “coroutine” can be used for two closely related concepts:

- `a coroutine function`: an async def function;
- `a coroutine object`: an object returned by calling a coroutine function.

Tasks

Tasks are used to schedule coroutines concurrently.

When a coroutine is wrapped into a `Task` with functions like `asyncio.create_task()` the `coroutine is automatically scheduled to run soon`:

```python
import asyncio

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task

asyncio.run(main())
```

Futures:

A `Future` is a special `low-level awaitable` object that represents an `eventual result of an asynchronous operation`.

When a `Future object` is awaited it means that the `coroutine will wait until the Future is resolved in some other place`.

Future objects in asyncio are needed to allow `callback-based code` to be used with async/await.

Normally `there is no need to create Future objects at the application level code`.

Future objects, sometimes exposed by libraries and some asyncio APIs, can be awaited:

```python
async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )
```

### 4.5 Task groups <a name="task-groups"></a>

Task groups combine a task creation API with a convenient and reliable way to wait for all tasks in the group to finish.

`class asyncio.TaskGroup`
An asynchronous context manager holding a group of tasks. Tasks can be added to the group using `create_task()`. All tasks are awaited when the context manager exits.

```python
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(some_coro(...))
        task2 = tg.create_task(another_coro(...))
    print("Both tasks have completed now.")
```

The `async with` statement will `wait for all tasks in the group to finish`. While waiting, `new tasks may still be added to the group` (for example, by passing tg into one of the coroutines and calling `tg.create_task()` in that coroutine).` Once the last task has finished and the async with block is exited, no new tasks may be added to the group`.

### 4.6 Sleep <a name="asyncio-sleep"></a>

`coroutine asyncio.sleep(delay, result=None)`

Block for delay seconds.

If result is provided, it is returned to the caller when the coroutine completes.

sleep() always suspends the current task, allowing other tasks to run.

Setting the delay to 0 provides an optimized path to allow other tasks to run. This can be used by long-running functions to avoid blocking the event loop for the full duration of the function call.

### 4.7 Running coroutines in threads <a name="coroutine-thread"></a>

`coroutine asyncio.to_thread(func, /, *args, **kwargs)`

Asynchronously run function func in a separate thread.

Any \*args and \*\*kwargs supplied for this function are directly passed to func. Also, the current `contextvars.Context` is propagated, allowing context variables from the event loop thread to be accessed in the separate thread.

Return a coroutine that can be awaited to get the eventual result of func.

This coroutine function is primarily intended to be used for executing IO-bound functions/methods that would otherwise block the event loop if they were run in the main thread.

`asyncio.run_coroutine_threadsafe(coro, loop)`

Submit a coroutine to the given event loop. Thread-safe.

Return a concurrent.futures.Future to wait for the result from another OS thread.

This function is meant to be called from a different OS thread than the one where the event loop is running.

## 5. Generators <a name="generators"></a>

A generator expression yields a new generator object. Its syntax is the same as for comprehensions, except that it is enclosed in parentheses instead of brackets or curly braces.

Example generator:

```python
generator = (x*y for x in range(10) for y in range(x, x+10))
```

Variables used in the generator expression are evaluated **lazily** when the `__next__()` method is called for the generator object (in the same fashion as normal generators). However, the **iterable expression in the leftmost for clause is immediately evaluated**, so that an error produced by it will be emitted at the point where the generator expression is defined, rather than at the point where the first value is retrieved.

### 5.1 Yield expression <a name="yield"></a>

The `yield` expression is used when defining a generator function or an asynchronous generator function and thus can only be used in the body of a function definition.

```python
def gen():  # defines a generator function
    yield 123

async def agen(): # defines an asynchronous generator function
    yield 123
```

When a `generator function` is called, it returns an `iterator` known as a `generator`. That generator then `controls the execution of the generator function`. The execution starts when one of the `generator’s methods is called`. At that time, `the execution proceeds to the first yield expression, where it is suspended again`, returning the value of `expression_list` to the generator’s caller, or `None if expression_list` is omitted. By `suspended`, we mean that **all local state is retained, including the current bindings of local variables, the instruction pointer, the internal evaluation stack, and the state of any exception handling**. When the execution is resumed by calling one of the generator’s methods, the function can proceed exactly as if the yield expression were just another external call. The value of the yield expression after resuming depends on the method which resumed the execution. If `__next__()` is used (typically via either a for or the `next()` builtin) then the result is None. Otherwise, if `send()` is used, then the result will be the value passed in to that method.

When `yield from <expr>` is used, the supplied `expression` **must be an iterable**. The values produced by iterating that iterable are passed directly to the caller of the current generator’s methods. Any values passed in with `send()` and any exceptions passed in with `throw()` are passed to the underlying iterator if it has the appropriate methods. If this is not the case, then `send()` will raise `AttributeError or TypeError`, while `throw()` will just raise the passed in exception immediately.

When the `underlying iterator` is **complete**, the value attribute of the raised `StopIteration` instance **becomes the value of the yield expression**. It can be either set explicitly when raising `StopIteration`, or automatically when the subiterator is a generator (by returning a value from the subgenerator).

## 6. Decorators <a name="decorators"></a>

A decorator in Python is a function that **accepts another function as an argument**. The decorator will usually **modify or enhance the function** it accepted and **return the modified function**.

Example of a decorator:

```python
def another_function(func):
    """
    A function that accepts another function
    """
    def other_func():
        val = f"The result of {func()} is {eval(func())}"
        return val
    return other_func

@another_function
def a_function():
    """A pretty useless function"""
    return "1+1"

if __name__ == "__main__":
    value = a_function()
    print(value)

# prints: The result of 1+1 is 2
```

## 8. Garbage collection <a name="garbage-collection"></a>

In C, C++, and Java we have variables and objects. Python has **names**, not variables. A Python object is stored in memory with **names and references**. A name is just a **label for an object**, so one object can have many names. A **reference is a name(pointer) that refers to an object**.

Python objects have three things: **Type**, **value**, and **reference count**. When we assign a name to a variable, its type is automatically detected by Python as we mentioned above. Value is declared while defining the object. Reference count is the number of **names pointing that object**.

Python has **two ways to delete the unused objects from the memory**.

When value **no longer has references it is deleted from the memory**, meaning the reference count has hit 0.
The problem arrives when a cyclical reference or reference cycle exists. An example of such reference is when a list is appended to itself. Reference counting alone can not destroy objects with cyclic references. If the reference count is not zero, the object cannot be deleted.

The solution to this problem is the second garbage collection method.

**Generational garbage collection** is a type of trace-based garbage collection. It can break cyclic references and delete the unused objects even if they are referred by themselves.

Python keeps track of every object in memory. 3 lists are created when a program is run. **Generation 0, 1, and 2 lists**.

The garbage collector is keeping track of all objects in memory. A new object starts its life in the **first generation of the garbage collector**. If Python executes a garbage collection process on a generation and **an object survives**, **it moves up into a second**, older generation. The Python garbage collector has **three generations** in total, and an object moves into an older generation whenever it survives a garbage collection process on its current generation.

For each generation, the **garbage collector module has a threshold number of objects**. If the number of objects **exceeds that threshold**, the garbage collector will trigger a **collection process**. For any objects that survive that process, they’re moved into an **older generation**.

## 8. Fluent python <a name="fluent-python"></a>

This is where I will store all the information I've gathered while reading [Fluent Python by Luciano Ramalho](https://www.amazon.com/Fluent-Python-Concise-Effective-Programming/dp/1491946008).

- In order to implement such things as `my_collection[key]` `my_collection.__getitem__(key)` is required to be implemented.
  The `__getitem__()` can also use a `slice` object as argument: `__getitem__(slice(start, stop, step))`. To implement the simplest possible collection it is enough to implement `__getitem__()` and `__len__()` for the collection class.

- When adding two objects in python such as 1 + 2 the framework calls the `__add__(other)` method of the `int` object looking in **pseudo-code** something like this: `1.__add__(2)` but this wouldn't be allowed by the python interpreter because:

```python
 1.__add__()
  File "<stdin>", line 1
    1.__add__()
     ^
SyntaxError: invalid decimal literal
```

- The expected behavior of infix operators such as `+` or `*` is to create new objects and not touch their operands.

- The `__repr__` special method is called by `repr()` built in to get the string representation of the object for inspection. If `__repr__` is not implemented a Vector object would be show in the console as: `<Vector object at 0x10e100070>`. The `__repr__` is also called by `%r` or `!r` in the `string.format()` or the `f-strings`. The `__repr__` should return a string that is unambiguous and match the source code of recreating the object.

- The contrast between `__repr__` and `__str__` is that `__str__` is called by `str()` constructor and implicitly used by the `print()` function. It should return a string suitable for end users. A simple explanation about the different use of these methods is that `__repr__` is used for debugging and `__str__` is used for end users. If the `__str__` is not implemented Python will fall back to `__repr__`.

- By default user-defined classes are considered **truthy**, unless either `__bool__` or `__len__` are implemented. Basically `bool(x)` calls `x.__bool__()` and uses the result. If `__bool__` is not implemented is falls back to `x.__len__()` and if that returns 0 it returns False, otherwise it returns True.

- The **Python data model** is the properties of objects in general in a Python.

- Container sequence is a sequence that can hold items of different types: `list`, `tuple` and `collections.deque`

- Flat sequence is a sequence that can hold items of one type: `str`, `bytes`, `bytearray`, `memoryview` and `array.array`

- List, set and dict comprehension and generator expressions have their own local scope (like functions), so variables cannot leak outside the scope.

- In order to create `tuples`, `arrays` or other types of sequences you can start from a list comprehension but generator expressions save memory because they yield information instead one by one using the iterator protocol instead of building a whole list to feed another constructor.

- Tuples hold records: each item in the tuple holds the data for one field and the position of the item give meaning.

- `*` can be used to grab arbitrary excess arguments.

```python
>>> a, b, *rest = range(5)
>>> a, b, rest
(0, 1, [2, 3, 4])
#or
>>> a, *body, c, d = range(5)
>>> a, body, c, d
(0, [1, 2], 3, 4)
```

## 9. References <a name="references"></a>

This document was created with the help of the:

- [official python3.11 documentation](https://docs.python.org/3/library/);
- [python101 website](https://python101.pythonlibrary.org/);
- [article on garbage collector in python](https://towardsdatascience.com/memory-management-and-garbage-collection-in-python-c1cb51d1612c);
- [Fluent Python by Luciano Ramalho](https://www.amazon.com/Fluent-Python-Concise-Effective-Programming/dp/1491946008).
