# SOLID Principles

# Table of contents

1. [**S**ingle Responsibility Principle](#srp)
2. [**O**pen-Closed Principle](#open_closed)
3. [**L**iskov substitution principle](#liskov)
4. [**I**nterface segregation principle](#interface_segregation)
5. [**D**ependency inversion principle](#dip)
6. [References](#references)

## 1. **S**ingle responsibility principle <a name="srp"></a>

A responsibility is considered a reason to change, so a class or module should have only one reason to be changed or rewritten.

As an example, consider a module that compiles and prints a report. Imagine such a module can be changed for two reasons. First, the content of the report could change. Second, the format of the report could change. These two things change for different causes. The single-responsibility principle says that these two aspects of the problem are really two separate responsibilities, and should, therefore, be in separate classes or modules.

## 2. **O**pen-Closed Principle <a name="open_closed"></a>

A module will be said to be open if it is still available for extension. For example, it should be possible to add fields to the data structures it contains, or new elements to the set of functions it performs.

A module will be said to be closed if it is available for use by other modules. This assumes that the module has been given a well-defined, stable description (the interface in the sense of information hiding).

A class is closed, since it may be compiled, stored in a library, baselined, and used by client classes. But it is also open, since any new class may use it as parent, adding new features. When a descendant class is defined, there is no need to change the original or to disturb its clients.

## 3. **L**iskov substitution principle <a name="liskov"></a>

It is based on the concept of "substitutability" – a principle in object-oriented programming stating that an object (such as a class) may be replaced by a sub-object (such as a class that extends the first class) without breaking the program.

Liskov's notion of a behavioral subtype defines a notion of substitutability for objects; that is, if S is a subtype of T, then objects of type T in a program may be replaced with objects of type S without altering any of the desirable properties of that program (e.g. correctness).

## 4. **I**nterface segregation principle <a name="interface_segregation"></a>

Interface segregation principle (ISP) states that no code should be forced to depend on methods it does not use. ISP splits interfaces that are very large into smaller and more specific ones so that clients will only have to know about the methods that are of interest to them. Such shrunken interfaces are also called role interfaces. ISP is intended to keep a system decoupled and thus easier to refactor, change, and redeploy.

## 5. **D**ependency inversion principle <a name="dip"></a>

The principle states:

- High-level modules should not import anything from low-level modules. Both should depend on abstractions (e.g., interfaces).
- Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions.

## 6. References <a name="references"></a>

This document was written with the help of the [Wikipedia SOLID page](https://en.wikipedia.org/wiki/SOLID).
