# A complete core python3 interview cheatsheet

## 1. Python types

**Mutable** data types are those whose values can be changed or new values can be assigned to them.
**Immutable** data types are those, whose values cannot be modified once they are created.

| Mutable types | Immutable types |
| ------------- | --------------- |
| Lists         | Numbers         |
| Sets          | Strings         |
| Dictionaries  | Tuples          |
|               | Frozen Sets     |

```python
# You can use type(<SOMETHING>) to figure out what type is something
type(1) # int
type(2.8) # float
type("hello") # str
```

### 1.1 Truth Value Testing

By default an object is True unless `__bool__()` method returns False or `__len__()` returns 0.
What objects are considered false:

- `None` and `False`
- 0 of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`
- empty sequences and collections: `''`, `()`, `[]`

### 1.2 Boolean operations

`and`, `or`, `not`

| Operation | Result                               |
| --------- | ------------------------------------ |
| `x or y`  | if x false, then y else x            |
| `x and y` | if x false, then x else y            |
| `not x`   | if x false, then `True` else `False` |

### 1.3 Comparison

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

### 1.4 Numeric Types

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

### 1.5 Additional methods for Integer types

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

### 1.6 Additional methods for Float types

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

### 1.7 Hashing of numeric types

For numbers x and y, possibly of different types, it’s a requirement that `hash(x) == hash(y)` whenever `x == y`

### 1.8 Iterator types

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

### 1.9 Generator types

Python’s generators provide a convenient way to implement the iterator protocol. If a container object’s `__iter__()` method is implemented as a generator, it will automatically return an iterator object (technically, a generator object) supplying the `__iter__()` and `__next__()` methods.

### 1.10 Sequence Types

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
