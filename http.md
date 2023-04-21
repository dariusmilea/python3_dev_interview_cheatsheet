# HTTP interview cheatsheet

# Table of contents

1. [HTTP Definition](#defintion)
2. [The client](#client)
3. [The server](#server)
4. [What HTTP can control](#http_control)
5. [Messages](#messages)
   1. [Requests](#requests)
   2. [Responses](#responses)
6. [Sessions](#sessions)
7. [CORS](#cors)
8. [Authentication](#authentication)
9. [Cookies](#cookies)
10. [Caching](#caching)

## 1. HTTP Definition <a name="definition"></a>

HTTP is a protocol for `fetching resources` such as HTML documents. It is the foundation of any data exchange on the Web and it is a `client-server protocol`, which means requests are initiated by the recipient, usually the Web browser.

## 2. The client <a name="client"></a>

The browser is always the entity initiating the request. It is never the server (though some mechanisms have been added over the years to simulate server-initiated messages).

To display a Web page, the browser sends an original request to fetch the `HTML` document that represents the page. It then parses this file, making additional requests corresponding to execution scripts, layout information `(CSS)` to display, and sub-resources contained within the page (usually images and videos). The Web browser then combines these resources to present the complete document, the Web page. Scripts executed by the browser can fetch more resources in later phases and the browser updates the Web page accordingly.

A Web page is a hypertext document. This means some parts of the displayed content are links, which can be activated (usually by a click of the mouse) to fetch a new Web page, allowing the user to direct their user-agent and navigate through the Web. The browser translates these directions into HTTP requests, and further interprets the HTTP responses to present the user with a clear response.

## 3. The server <a name="server"></a>

On the opposite side of the communication channel is the server, which serves the document as requested by the client. A server appears as only a single machine virtually; but it may actually be a collection of servers sharing the load (load balancing), or a complex piece of software interrogating other computers (like cache, a DB server, or e-commerce servers), totally or partially generating the document on demand.

A server is not necessarily a single machine, but several server software instances can be hosted on the same machine. With HTTP/1.1 and the Host header, they may even share the same IP address.

## 4.What HTTP can control <a name="http_control"></a>

| Feature             | Description                                                                                                                                                                                                                            |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Caching             | The server can instruct proxies and clients about what to cache and for how long. The client can instruct intermediate cache proxies to ignore the stored document.                                                                    |
| Security            | To prevent snooping and other privacy invasions, Web browsers enforce strict separation between Web sites. Only pages from the same origin can access all the information of a Web page.                                               |
| Authentication      | Some pages may be protected so that only specific users can access them. Basic authentication may be provided by HTTP, either using the `WWW-Authenticate` and similar headers, or by setting a specific session using `HTTP cookies`. |
| Proxy and tunneling | Servers or clients are often located on intranets and hide their true IP address from other computers. HTTP requests then go through proxies to cross this network barrier. Not all proxies are HTTP proxies.                          |
| Sessions            | Using HTTP cookies allows you to link requests with the state of the server. This creates sessions, despite basic HTTP being a state-less protocol.                                                                                    |

## 5. Messages <a name="messages"></a>

HTTP messages, as defined in HTTP/1.1 and earlier, are human-readable. In HTTP/2, these messages are embedded into a binary structure, a frame, allowing optimizations like compression of headers and multiplexing. Even if only part of the original HTTP message is sent in this version of HTTP, the semantics of each message is unchanged and the client reconstitutes (virtually) the original HTTP/1.1 request. It is therefore useful to comprehend HTTP/2 messages in the HTTP/1.1 format.

The most commonly used API based on HTTP is the `XMLHttpRequest` API, which can be used to exchange data between a user agent and a server. The modern Fetch API provides the same features with a more powerful and flexible feature set.

There are two types of HTTP messages, requests and responses, each with its own format.

### 5.1 Requests <a name="requests"></a>

Requests consist of the following elements:

- An HTTP method, usually a verb like `GET`, `POST`, or a noun like `OPTIONS `or `HEAD` that defines the operation the client wants to perform.
- The path of the resource to fetch; the URL of the resource stripped from elements that are obvious from the context, for example without the protocol (`http://`), the domain (here, `developer.mozilla.org`), or the TCP port (here, `80`).
- The version of the HTTP protocol.
- Optional headers that convey additional information for the servers.
- A body, for some methods like POST, similar to those in responses, which contain the resource sent.

### 5.2 Responses <a name="responses"></a>

Responses consist of the following elements:

- The version of the HTTP protocol they follow.
- A status code, indicating if the request was successful or not, and why.
- A status message, a non-authoritative short description of the status code.
- HTTP headers, like those for requests.
- Optionally, a body containing the fetched resource.

## 6. Sessions <a name="sessions"></a>

In client-server protocols, like HTTP, sessions consist of three phases:

- The client establishes a TCP connection (or the appropriate connection if the transport layer is not TCP).
- The client sends its request, and waits for the answer.
- The server processes the request, sending back its answer, providing a status code and appropriate data.

## 7. CORS <a name="cors"></a>

Cross-Origin Resource Sharing (CORS) is an HTTP-header based mechanism that allows a server to indicate any origins (domain, scheme, or port) other than its own from which a browser should permit loading resources. CORS also relies on a mechanism by which browsers make a "preflight" request to the server hosting the cross-origin resource, in order to check that the server will permit the actual request. In that preflight, the browser sends headers that indicate the HTTP method and headers that will be used in the actual request.

For security reasons, browsers restrict cross-origin HTTP requests initiated from scripts. For example, XMLHttpRequest and the Fetch API follow the same-origin policy. This means that a web application using those APIs can only request resources from the same origin the application was loaded from unless the response from other origins includes the right CORS headers.

The Cross-Origin Resource Sharing standard works by adding new HTTP headers that let servers describe which origins are permitted to read that information from a web browser. Additionally, for HTTP request methods that can cause side-effects on server data (in particular, HTTP methods other than GET, or POST with certain MIME types), the specification mandates that browsers "preflight" the request, soliciting supported methods from the server with the HTTP OPTIONS request method, and then, upon "approval" from the server, sending the actual request. Servers can also inform clients whether "credentials" (such as Cookies and HTTP Authentication) should be sent with requests.

## 8. Authentication <a name="authentication"></a>

`RFC 7235` defines the HTTP authentication framework, which can be used by a server to challenge a client request, and by a client to provide authentication information.

The challenge and response flow works like this:

- The server responds to a client with a 401 (Unauthorized) response status and provides information on how to authorize with a WWW-Authenticate response header containing at least one challenge.
- A client that wants to authenticate itself with the server can then do so by including an Authorization request header with the credentials.
- Usually a client will present a password prompt to the user and will then issue the request including the correct Authorization header.

The `WWW-Authenticate` and `Proxy-Authenticate` response headers define the authentication method that should be used to gain access to a resource. They must specify which authentication scheme is used, so that the client that wishes to authorize knows how to provide the credentials.

| Authentication scheme | Description                                                                                                      |
| --------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Basic                 | base64-encoded credentials                                                                                       |
| Bearer                | bearer tokens to access OAuth 2.0-protected resources                                                            |
| Digest                | Firefox 93 and later support the SHA-256 algorithm. Previous versions only support MD5 hashing (not recommended) |
| HOBA                  | HTTP Origin-Bound Authentication, digital-signature-based                                                        |
| AWS4-HMAC-SHA256      | This scheme is used for AWS3 server authentication.                                                              |

## 9. Cookies <a name="cookies"></a>

An HTTP cookie (web cookie, browser cookie) is a small piece of data that a server sends to a user's web browser. The browser may store the cookie and send it back to the same server with later requests. Typically, an HTTP cookie is used to tell if two requests come from the same browser—keeping a user logged in, for example. It remembers stateful information for the stateless HTTP protocol.

Cookies are mainly used for three purposes:

- Session management : Logins, shopping carts, game scores, or anything else the server should remember
- Personalization: User preferences, themes, and other settings
- Tracking: Recording and analyzing user behavior

## 10. Caching <a name="caching"></a>

The HTTP cache stores a response associated with a request and reuses the stored response for subsequent requests.

There are several advantages to reusability. First, since there is no need to deliver the request to the origin server, then the closer the client and cache are, the faster the response will be. The most typical example is when the browser itself stores a cache for browser requests.

Also, when a response is reusable, the origin server does not need to process the request — so it does not need to parse and route the request, restore the session based on the cookie, query the DB for results, or render the template engine. That reduces the load on the server.

There are two types of caches: Private and Shared.

A private cache is a cache tied to a specific client — typically a browser cache. Since the stored response is not shared with other clients, a private cache can store a personalized response for that user.
On the other hand, if personalized contents are stored in a cache other than a private cache, then other users may be able to retrieve those contents — which may cause unintentional information leakage.

If a response contains personalized content and you want to store the response only in the private cache, you must specify a private directive.

`Cache-Control: private`

The shared cache is located between the client and the server and can store responses that can be shared among users. And shared caches can be further sub-classified into proxy caches and managed caches.

In addition to the function of access control, some proxies implement caching to reduce traffic out of the network. This is usually not managed by the service developer, so it must be controlled by appropriate HTTP headers and so on.

Managed caches are explicitly deployed by service developers to offload the origin server and to deliver content efficiently. Examples include reverse proxies, CDNs, and service workers in combination with the Cache API.
