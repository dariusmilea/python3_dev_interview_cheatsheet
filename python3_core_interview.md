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
What objects are coonsidered false:

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
|`abs(x)`|absolute value or magnitued of x|
|`int(x)`|x converted to integer|
|`float(x)`|x converted to floating point|
|`complex(re,im)`|a complex number with real part re, imaginary part im. im defaults to zero.|
|`c.conjucagate()`|conjugate of the complex number c|
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