# Web Server Gateway Interface

# Table of contents

1. [Definition](#definition)
2. [Specifications](#specifications)
3. [References](#references)

## 1. Definition <a name="definition"></a>

`WSGI` stands for `"Web Server Gateway Interface"`. It is used to `forward requests from a web server` (such as Apache or NGINX) to a `backend Python web application or framework`. From there, responses are then passed back to the `webserver` to reply to the requestor.

## 2. Specifications <a name="specifications"></a>

The `WSGI interface` has two sides: `the “server” or “gateway” side`, and `the “application” or “framework” side`. The server side **invokes a callable object that is provided by the application side**. The specifics of how that object is provided are up to the server or gateway. It is assumed that some servers or gateways will require an application’s deployer to write a short script to create an instance of the server or gateway, and supply it with the application object. Other servers and gateways may use configuration files or other mechanisms to specify where an application object should be imported from, or otherwise obtained.

In addition to “pure” servers/gateways and applications/frameworks, it is also possible to create “middleware” components that implement both sides of this specification. Such components act as an application to their containing server, and as a server to a contained application, and can be used to provide extended APIs, content transformation, navigation, and other useful functions.

Throughout this specification, we will use the term “a callable” to mean “a function, method, class, or an instance with a **call** method”. It is up to the server, gateway, or application implementing the callable to choose the appropriate implementation technique for their needs. Conversely, a server, gateway, or application that is invoking a callable must not have any dependency on what kind of callable was provided to it. Callables are only to be called, not introspected upon.

## 3. References <a name="references"></a>

This document was realised with the help of [liquidweb article on WSGI](https://www.liquidweb.com/kb/what-is-wsgi/) and the [PEP-3333 document](https://peps.python.org/pep-3333/).
