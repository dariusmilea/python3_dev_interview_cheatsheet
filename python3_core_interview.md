# A complete core python3 interview cheatsheet

## 1. Python types

```python
# You can use type(<SOMETHING>) to figure out what type is something
type(1) # int
type(2.8) # float
type("hello") # str
```

### 1.1 Truth Value Testing

By default an object is True unless `__bool__()` method returns False or `__len__()` returns 0.
What objects are considered false:

* `None` and `False`
* 0 of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`
* empty sequences and collections: `''`, `()`, `[]`

### 1.2 Boolean operations

`and`, `or`, `not`

| Operation | Result |
|-----------|--------|
| `x or y`  | if x false, then y else x|
| `x and y`  | if x false, then x else y|
| `not x`  | if x false, then `True` else `False`|


### 1.3 Comparison

| Operation | Meaning |
|-----------|---------|
|`<`|strictly less than|
|`<=`|less than or equal|
|`>`|strictly greater than|
|`>=`|greater than or equal|
|`==`|equal|
|`!=`|not equal|
|`is`|object identity|
|`is not`|negated object identity|

Different object types (non numerical) always compare `False`.
Equality can be overwritten with use of `__eq__()`
Comparisons can be defined with the use of:
*  `__lt__()` # <
*  `__le__()` # <=
*  `__gt__()` # >
*  `__ge__()` # >=

Two more operations with the same syntactic priority, `in` and `not in`, are supported by types that are iterable or implement the `__contains__()` method.

### 1.4 Numeric Types

There are three numeric types for Python

* integer : `int`
* floating-point : `float`
* complex : `complex`

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

| Operation | Result |
|-----------|--------|
|`x+y`|sum of x and y|
|`x-y`|difference of x and y|
|`x*y`|product of x and y|
|`x/y`|quotient of x and y|
|`x//y`|floored quotient of x and y|
|`x%y`|remainder of `x/y`|
|`-x`|negated x|
|`+x`|x unchanged|
|`abs(x)`|absolute value or magnitude of x|
|`int(x)`|x converted to integer|
|`float(x)`|x converted to floating point|
|`complex(re,im)`|a complex number with real part re, imaginary part im. im defaults to zero.|
|`c.conjugate()`|conjugate of the complex number c|
|`divmod(x,y)`|pair `(x//y,x%y)`|
|`pow(x,y)`|x to the power of y|
|`x**y`|x to the power of y|

`x//y` known as integer division. The result is always rounded towards minus infinity and is an integer.

For additional numeric operations use `math` and `cmath` modules.

Bitwise Operations:

| Operation | Result |
|-----------|--------|
|`x \| y`|bitwise or of x and y|
|`x \^ y`|bitwise exclusive or of x and y|
|`x \& y`|bitwise and of x and y|
|`x << n`|x shifted left by n bits|
|`x >> n`|x shifted right by n bits|
|`~x`|inverted bits of x|

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

There are three basic sequence types: `lists`, `tuples`, and `range` objects.