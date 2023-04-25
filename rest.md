# REST and REST APIs interview cheatsheet

# Table of contents

1. [REST Definition](#rest_definition)
2. [Principles of REST](#principles)
   1. [Uniform interface](#uniform_interface)
   2. [Client-Server](#client_server)
   3. [Stateless](#stateless)
   4. [Cacheable](#cacheable)
   5. [Layered system](#layered_system)
   6. [[Optional]Code on Demand](#code_on_demand)
3. [Resource](#resource)
4. [HTTP and REST](#http_rest)
5. [Refrences](#refrences)

## 1. REST Definition <a name="rest_definition"></a>

REST is an acronym for `RE`presentational `S`tate `T`ransfer and an architectural style for distributed hypermedia systems.

A Web API (or Web Service) conforming to the REST architectural style is a REST API.

## 2. Principles of REST <a name="principles"></a>

There's 6 guiding principles or constraints of the RESTful architecture.

### 2.1 Uniform Interface <a name="uniform_interface"></a>

A uniform REST interface is achieved following these principles:

An interface must uniquely identify each resource involved in the interaction between client and server.

The resources should have uniform representations in the server response. API consumers should use these representations to modify the resources state in the server.

Each resource representation should carry enough information to describe how to process the message. It should also provide information on the additional actions that the client can perform on the resource.

The client should have only the initial URI of the application. The client application should dynamically drive all other resources and interactions with the use of hyperlinks.

### 2.2 Client-Server <a name="client_server"></a>

The client-server design pattern enforces the separation of concerns, which helps the client and the server components evolve independently.

By separating the user interface concerns (client) from the data storage concerns (server), we improve the portability of the user interface across multiple platforms and improve scalability by simplifying the server components.

While the client and the server evolve, we have to make sure that the interface/contract between the client and the server does not break.

### 2.3 Stateless <a name="stateless"></a>

Statelessness mandates that each request from the client to the server must contain all of the information necessary to understand and complete the request.

The server cannot take advantage of any previously stored context information on the server.

For this reason, the client application must entirely keep the session state.

### 2.4 Cacheable <a name="cacheable"></a>

Caching is the ability to store copies of frequently accessed data in several places along the request-response path.

The `cacheable` constraint requires that a response should implicitly or explicitly label itself as cacheable or non-cacheable.

If the response is `cacheable`, the client application gets the `right to reuse the response data later for equivalent requests and a specified period`.

### 2.5 Layered System <a name="layered_system"></a>

The layered system style allows an architecture to be composed of hierarchical layers by constraining component behavior.
For example, in a layered system, each component cannot see beyond the immediate layer they are interacting with.

### 2.6 [Optional] Code on demand <a name="code_on_demand"></a>

REST also allows client functionality to extend by downloading and executing code in the form of applets or scripts.

## 3 Resource <a name="resource"></a>

The key abstraction of information in REST is a resource. Any information that we can name can be a resource.
The state of a resource at any particular time is know as a `resource representation`.

The resource representations are consist of:

- The data
- The metadata
- Hypermedia links that can help the clients in transition to the next desired state

REST uses resource `identifiers` to identify each resource involved in the interactions between the client and the server components.

Further, resource representations shall be self-descriptive: the client does not need to know if a resource is an employee or a device. It should act based on the media type associated with the resource.
So in practice, we will create lots of custom media types – usually one media type associated with one resource.

Another important thing associated with REST is `resource methods`. These resource methods are used to perform the desired transition between two states of any resource.

Ideally, everything needed to transition the resource state shall be part of the resource representation – including all the supported methods and what form they will leave the representation.

## 4 HTTP and REST <a name="http_rest"></a>

REST and HTTP are not the same.

Though REST also intends to make the web (internet) more streamlined and standard, Roy Fielding advocates using REST principles more strictly. And that’s from where people try to start comparing REST with the web.

Roy Fielding, in his dissertation, has nowhere mentioned any implementation direction – including any protocol preference or even HTTP. Till the time, we are honoring the six guiding principles of REST, which we can call our interface – `RESTful`.

## 5. References <a name="references"></a>

This document was created with the help of [RESTFULAPI.NET](https://restfulapi.net/).
