# Networking knowledge for interview

# Table of contents

1. [LAN](#lan)
   1. [IP Address](#ip)
   2. [Switch](#switch)
   3. [Router](#router)
   4. [Subnet](#subnet)
   5. [Gateway](#gateway)
   6. [ICMP](#icmp)
   7. [OSI Model](#osi)
      1. [Physical layer](#osi-1)
      2. [Data link layer](#osi-2)
      3. [Network layer](#osi-3)
      4. [Transport layer](#osi-4)
      5. [Session layer](#osi-5)
      6. [Presentation layer](#osi-6)
      7. [Application layer](#osi-7)
   8. [ARP](#arp)
   9. [VLAN](#vlan)
   10. [IPv4](#ipv4)
   11. [IPv6](#ipv6)
   12. [Routing table](#routing-table)
   13. [OSPF](#ospf)
   14. [BGP](#bgp)
   15. [VxLAN](#vxlan)
   16. [EVPN](#evpn)
2. [WAN](#wan)
   1. [NAT](#nat)
   2. [Firewall](#firewall)
   3. [DMZ](#dmz)
   4. [Port forwarding](#port-forwarding)
3. [References](#references)

## 1. LAN (Local Area Network) <a name="lan"></a>

A local area network (LAN) is a collection of devices connected together in one physical location, such as a building, office, or home. A LAN can be small or large, ranging from a home network with one user to an enterprise network with thousands of users and devices in an office or school.

### 1.1 IP Address <a name="ip"></a>

An IP Address is a logical address of a device in the network, used to locate the device inside the network.

### 1.2 Switch <a name="switch"></a>

A switch is a device from the LAN that allows communication between the devices in the LAN. Based on the IP Addresses of the LAN devices, the switch can point the right package from one device to the desired device. Switches function on layer2. When a packet enters the switch, the switch reads its header, then matches the destination address or addresses and sends the packet out through the appropriate ports that lead to the destination devices.

### 1.3 Router <a name="router"></a>

A router is a networking device that forwards data packets between different LAN networks, part of a WAN (Wide area network). Routers operate at Layer 3 -- the network layer -- and are used to connect networks to other networks.

### 1.4 Subnet <a name="subnet"></a>

Subnet is a sub-network that is part of the LAN. It defines the range of the LAN. The practice of dividing a network into two or more networks is called subnetting. Computers that **belong to the same subnet are addressed** with **an identical most-significant bit-group in their IP addresses**. This results in the logical division of an IP address into two fields: **the network number or routing prefix** and **the rest field or host identifier**. The **rest field is an identifier for a specific host or network interface**. The routing prefix may be expressed in **Classless Inter-Domain Routing (CIDR)** notation written as the `first address of a network`, followed by a slash character (`/`), and **ending with the bit-length of the prefix**. For example, `198.51.100.0/24` is the prefix of the Internet Protocol version 4 network starting at the given address, having `24 bits allocated for the network prefix`, and the remaining `8 bits reserved for host addressing`. For IPv4, a network may also be characterized by its **subnet mask or netmask**, which is the **bitmask** that, when applied by a **bitwise AND operation to any IP address in the network, yields the routing prefix**. Subnet masks are also expressed in dot-decimal notation like an IP address. For example, the prefix `198.51.100.0/24` would have the subnet mask `255.255.255.0`.

### 1.5 Gateway <a name="gateway"></a>

IP Address of the router.

### 1.6 ICMP <a name="icmp"></a>

The **Internet Control Message Protocol** (ICMP) is a network layer protocol used by network devices to **diagnose network communication** issues. ICMP is mainly used to determine whether or not data is reaching its intended destination in a timely manner. Commonly, the ICMP protocol is used on network devices, such as routers. ICMP is crucial for error reporting and testing, but it can also be used in distributed denial-of-service (DDoS) attacks.
Normal IP traffic is sent using TCP, which means any two devices that exchange data will first carry out a TCP handshake to ensure both devices are ready to receive data. **ICMP does not open a connection in this way**. **The ICMP protocol also does not allow for targeting a specific port on a device**.
**ICMP packets include an ICMP header after a normal IP header**. When a router or server needs to send an error message, the **ICMP packet body or data section always contains a copy of the IP header of the packet that caused the error**.

### 1.7 OSI Model <a name="osi"></a>

Open Systems Interconnection model (OSI model) is a conceptual model from the International Organization for Standardization (ISO) that "provides a common basis for the coordination of standards development for the purpose of systems interconnection". It is a 7 layer architecture.

#### 1.7.1 Physical layer <a name="osi-1"></a>

The physical layer is responsible for the **transmission and reception of unstructured raw data between a device, such as a network interface controller, Ethernet hub, or network switch, and a physical transmission medium**. It converts the digital bits into electrical, radio, or optical signals.

#### 1.7.2 Data link layer <a name="osi-2"></a>

The data link layer provides **node-to-node data transfer—a link between two directly connected nodes**. It detects and possibly corrects errors that may occur in the physical layer. It defines the protocol to establish and terminate a connection between two physically connected devices. It also defines the protocol for flow control between them.

There are 2 data link layer sublayers:

- Medium access control (**MAC**):  responsible for controlling how devices in a network gain access to a medium and permission to transmit data.
- Logical link control (**LLC**): responsible for identifying and encapsulating network layer protocols, and controls error checking and frame synchronization.

#### 1.7.3 Network layer <a name="osi-3"></a>

The network layer provides the functional and procedural means of transferring packets from one node to another connected in "different networks". A network is a medium to which many nodes can be connected, on which every node has an address and which permits nodes connected to it to transfer messages to other nodes connected to it by merely providing the content of a message and the address of the destination node and letting the network find the way to deliver the message to the destination node, possibly routing it through intermediate nodes. If the message is too large to be transmitted from one node to another on the data link layer between those nodes, the network may implement message delivery by splitting the message into several fragments at one node, sending the fragments independently, and reassembling the fragments at another node. It may, but does not need to, report delivery errors.

#### 1.7.4 Transport layer <a name="osi-4"></a>

The transport layer provides the functional and procedural means of transferring variable-length data sequences from a source host to a destination host from one application to another across a network, while maintaining the quality-of-service functions. Transport protocols may be connection-oriented or connectionless.
This may require breaking large protocol data units or long data streams into smaller chunks called "segments", since the network layer imposes a maximum packet size called the maximum transmission unit (MTU), which depends on the maximum packet size imposed by all data link layers on the network path between the two hosts.

Some connection-oriented transport protocols, such as **TCP** and the OSI connection-oriented transport protocol (COTP), perform **segmentation and reassembly of segments on the receiving side**; **connectionless transport protocols, such as UDP and the OSI connectionless transport protocol (CLTP), usually do not**.

#### 1.7.5 Session layer <a name="osi-5"></a>

The session layer creates the setup, controls the connections, and ends the teardown, between two or more computers, which is called a "session". Since DNS and other Name Resolution Protocols operate in this part of the layer, common functions of the session layer include user logon (establishment), name lookup (management), and user logoff (termination) functions.

#### 1.7.6 Presentation layer <a name="osi-6"></a>

The presentation layer establishes data formatting and data translation into a format specified by the application layer during the encapsulation of outgoing messages while being passed down the protocol stack, and possibly reversed during the deencapsulation of incoming messages when being passed up the protocol stack. For this very reason, outgoing messages during encapsulation are converted into a format specified by the application layer, while the conversion for incoming messages during deencapsulation are reversed.

The presentation layer handles protocol conversion, data encryption, data decryption, data compression, data decompression, incompatibility of data representation between operating systems, and graphic commands.

#### 1.7.7 Application layer <a name="osi-7"></a>

The application layer is the layer of the OSI model that is closest to the end user, which means both the OSI application layer and the user interact directly with a software application that implements a component of communication between the client and server, such as File Explorer and Microsoft Word. Such application programs fall outside the scope of the OSI model unless they are directly integrated into the application layer through the functions of communication, as is the case with applications such as web browsers and email programs. Other examples of software are Microsoft Network Software for File and Printer Sharing and Unix/Linux Network File System Client for access to shared file resources.

### 1.8 ARP <a name="arp"></a>

The Address Resolution Protocol (ARP) is a communication protocol used for **discovering the link layer address**, such as a MAC address, associated with a given internet layer address, typically an IPv4 address. This mapping is a critical function in the Internet protocol suite.

The Address Resolution Protocol is a request-response protocol. Its messages are directly encapsulated by a link layer protocol. It is communicated within the boundaries of a single network, never routed across internetworking nodes.

The size of the ARP message depends on the link layer and network layer address sizes. The message header specifies the types of network in use at each layer as well as the size of addresses of each. The message header is completed with the operation code for request (1) and reply (2). The payload of the packet consists of four addresses, the hardware and protocol address of the sender and receiver hosts.

Example:

Two computers in an office (Computer 1 and Computer 2) are connected to each other in a local area network by Ethernet cables and network switches, with no intervening gateways or routers. Computer 1 has a packet to send to Computer 2. Through DNS, it determines that Computer 2 has the IP address 192.168.0.55.

To send the message, it also requires Computer 2's MAC address. First, Computer 1 uses a cached ARP table to look up 192.168.0.55 for any existing records of Computer 2's MAC address (00:EB:24:B2:05:AC). If the MAC address is found, it sends an Ethernet frame containing the IP packet onto the link with the destination address 00:EB:24:B2:05:AC. If the cache did not produce a result for 192.168.0.55, Computer 1 has to send a broadcast ARP request message (destination FF:FF:FF:FF:FF:FF MAC address), which is accepted by all computers on the local network, requesting an answer for 192.168.0.55.

Computer 2 responds with an ARP response message containing its MAC and IP addresses. As part of fielding the request, Computer 2 may insert an entry for Computer 1 into its ARP table for future use.

Computer 1 receives and caches the response information in its ARP table and can now send the packet.

### 1.9 VLAN <a name="vlan"></a>

A virtual local area network (VLAN) is a**ny broadcast domain that is partitioned and isolated in a computer network at the data link layer** (OSI layer 2).[2][3] In this context, virtual, refers to a physical object recreated and altered by additional logic, within the local area network. **VLANs work by applying tags to network frames and handling these tags in networking systems – creating the appearance and functionality of network traffic that is physically on a single network but acts as if it is split between separate networks**. In this way, VLANs can keep network applications separate despite being connected to the same physical network, and without requiring multiple sets of cabling and networking devices to be deployed.

### 1.10 IPv4 <a name="ipv4"></a>

Internet Protocol version 4 (IPv4) is the fourth version of the Internet Protocol (IP). It is one of the core protocols of standards-based internetworking methods in the Internet and other packet-switched networks. IPv4 uses 32-bit addresses.

IPv4 addresses may be represented in any notation expressing a 32-bit integer value. They are most often written in dot-decimal notation, which consists of four octets of the address expressed individually in decimal numbers and separated by periods.

For example, the quad-dotted IP address 192.0.2.235 represents the 32-bit decimal number 3221226219, which in hexadecimal format is 0xC00002EB.

IPv4 classes:

- **Class A** (addresses that start with **1 – 126; 8-bit network prefix**)

Class A is reserved for 126 large public networks and very large corporate networks. All of these network numbers have already been assigned. Each Class A network can contain almost 17 million (224-2) hosts.

Example: 10.4.5.1 (for host 4.5.1 on network number 10.0.0.0).

- **Class B** (addresses that start with **128 – 191; 16-bit network prefix**)

Class B can support 16,384 networks and is used by government agencies and very large corporations. Most of the 16,382 possible Class B addresses have already been assigned. Each Class B network can contain up to 65,534 (216-2) hosts.

Example: 172.16.5.1 (host 5.1 on network number 172.16.0.0).

- **Class C** (addresses that start with **192 – 223; 24-bit network prefix**)

Class C is intended for most users around the world. There are several million possible Class C networks. Each Class C network can contain up to 254 (28 -2) hosts.

Example: 192.139.25.1 (host 1 on network number 192.139.25.0).

- **Class D** (addresses that start with **224 - 239**)

Hosts can use Class D addresses to multicast messages to a specific group of nodes.

- **Class E** (addresses that start with **240 - 255**)

### 1.11 IPv6 <a name="ipv6"></a>

Internet Protocol version 6 (IPv6) is the most recent version of the Internet Protocol (IP), the communications protocol that provides an identification and location system for computers on networks and routes traffic across the Internet.
Devices on the Internet are assigned a unique IP address for identification and location definition. With the rapid growth of the Internet after commercialization in the 1990s, it became evident that far more addresses would be needed to connect devices than the IPv4 address space had available. By 1998, the IETF had formalized the successor protocol. IPv6 uses 128-bit addresses, theoretically allowing 2128, or approximately 3.4×1038 total addresses. The actual number is slightly smaller, as multiple ranges are reserved for special use or completely excluded from use. The two protocols are not designed to be interoperable, and thus direct communication between them is impossible, complicating the move to IPv6. However, several transition mechanisms have been devised to rectify this.

An IPv6 packet has two parts: a header and payload.

The header consists of a fixed portion with minimal functionality required for all packets and may be followed by optional extensions to implement special features.

The fixed header occupies the first 40 octets (320 bits) of the IPv6 packet. It contains the source and destination addresses, traffic class, hop count, and the type of the optional extension or payload which follows the header. This Next Header field tells the receiver how to interpret the data which follows the header. If the packet contains options, this field contains the option type of the next option. The "Next Header" field of the last option points to the upper-layer protocol that is carried in the packet's payload.

For convenience and clarity, the representation of an IPv6 address may be shortened with the following rules:

One or more leading zeros from any group of hexadecimal digits are removed, which is usually done to all of the leading zeros. For example, the group 0042 is converted to 42. The group 0000 is converted to 0.
Consecutive sections of zeros are replaced with two colons (::). This may only be used once in an address, as multiple use would render the address indeterminate. RFC 5952 requires that a double colon not be used to denote an omitted single section of zeros.

An example of application of these rules:

Initial address: **2001:0db8:0000:0000:0000:ff00:0042:8329**.
After removing all leading zeros in each group: **2001:db8:0:0:0:ff00:42:8329**.
After omitting consecutive sections of zeros: **2001:db8::ff00:42:8329**.

### 1.12 Routing table <a name="routing-table"></a>

In computer networking, a routing table, or routing information base (RIB), is a data table stored in a router or a network host that lists the routes to particular network destinations, and in some cases, metrics (distances) associated with those routes. The routing table contains information about the topology of the network immediately around it.

The routing table consists of at least three information fields:

- network identifier: The destination subnet and netmask
- metric: The routing metric of the path through which the packet is to be sent. The route will go in the direction of the gateway with the lowest metric.
- next hop: The next hop, or gateway, is the address of the next station to which the packet is to be sent on the way to its final destination

### 1.13 OSPF <a name="ospf"></a>

OSPF gathers link state information from available routers and constructs a topology map of the network. The topology is presented as a routing table to the Internet Layer for routing packets by their destination IP address. OSPF supports Internet Protocol Version 4 (IPv4) and Internet Protocol Version 6 (IPv6) networks and supports the Classless Inter-Domain Routing (CIDR) addressing model.

OSPF detects changes in the topology, such as link failures, and converges on a new loop-free routing structure within seconds.It computes the shortest-path tree for each route using a method based on Dijkstra's algorithm. The OSPF routing policies for constructing a route table are governed by link metrics associated with each routing interface. Cost factors may be the distance of a router (round-trip time), data throughput of a link, or link availability and reliability, expressed as simple unitless numbers. This provides a dynamic process of traffic load balancing between routes of equal cost.

### 1.14 BGP <a name="bgp"></a>

BGP neighbors, called peers, are established by manual configuration among routers to create a TCP session on port 179. A BGP speaker sends 19-byte keep-alive messages every 30 seconds (protocol default value, tunable) to maintain the connection. Among routing protocols, BGP is unique in using TCP as its transport protocol. Border Gateway Protocol (BGP) refers to a gateway protocol that enables the internet to exchange routing information between autonomous systems (AS). As networks interact with each other, they need a way to communicate. This is accomplished through peering.

### 1.15 VxLAN <a name="vxlan"></a>

VXLAN is an encapsulation protocol that provides data center connectivity using tunneling to stretch Layer 2 connections over an underlying Layer 3 network. In data centers, VXLAN is the most commonly used protocol to create overlay networks that sit on top of the physical network, enabling the use of virtual networks.
Data centers have rapidly increased their server virtualization over the past decade, resulting in dramatic increases in agility and flexibility. Virtualization of the network and decoupling the virtual network from the physical network makes it easier to manage, automate, and orchestrate.
The VXLAN tunneling protocol that encapsulates Layer 2 Ethernet frames in Layer 3 UDP packets, enables you to create virtualized Layer 2 subnets, or segments, that span physical Layer 3 networks. Each Layer 2 subnet is uniquely identified by a VXLAN network identifier (VNI) that segments traffic.

The entity that performs the encapsulation and decapsulation of packets is called a VXLAN tunnel endpoint (VTEP). To support devices that can’t act as a VTEP on their own, like bare-metal servers, a Juniper Networks device can encapsulate and de-encapsulate data packets. This type of VTEP is known as a hardware VTEP. VTEPs can also reside in hypervisor hosts, such as kernel-based virtual machine (KVM) hosts, to directly support virtualized workloads. This type of VTEP is known as a software VTEP.

### 1.16 EVPN <a name="evpn"></a>

Ethernet VPN-Virtual Extensible LAN (EVPN-VXLAN) provides large enterprises a common framework for managing their campus and data center networks. An EVPN-VXLAN architecture supports efficient Layer 2 and Layer 3 network connectivity with scale, simplicity, and agility, while also reducing OpEx costs.

The rapidly growing use of mobile devices (including the growing number of Internet of Things (IoT) devices), social media, and collaboration tools adds an increasing number of endpoints to a network. To provide endpoint flexibility, EVPN-VXLAN decouples the underlay network (physical topology) from the overlay network (virtual topology). By using overlays, you gain the flexibility of providing Layer 2 and Layer 3 connectivity between endpoints across campus and data centers, while maintaining a consistent underlay architecture.

EVPN is an extension to Border Gateway Protocol (BGP) that allows the network to carry endpoint reachability information such as Layer 2 MAC addresses and Layer 3 IP addresses. This control plane technology uses MP-BGP for MAC and IP address endpoint distribution, where MAC addresses are treated as routes.

## 2. WAN (Wide Area Network) <a name="wan"></a>

The router is the gateway through which a LAN device can communicate with a device that is part of the WAN.

### 2.1 NAT (Network area translation) <a name="nat"></a>

When a request comes from a LAN device it has it's LAN IP address which is only relevant inside the LAN. So for that device to communicate outside the LAN it is needed for the LAN IP address to be translated to a WAN IP address.

### 2.2 Firewall <a name="firewall"></a>

Is a set of passive rules to protect the network from unauthorized access.

### 2.3 DMZ (Demilitarized zone) <a name="dmz"></a>

A zone created within the LAN, which is specified to the router, so that when an external network device is trying to establish a connection to the LAN, that connection needs to be passed to the DMZ. If a device from the LAN is part of the DMZ it can talk to external network devices.

### 2.4 Port <a name="port"></a>

All devices from a LAN have communication ports in order to communicate with all the other devices. For example a port for a website webserver is 80, for a tomcat server 88 and so on.

### 2.5 Port forwarding <a name="port-forwarding"></a>

For a device from the LAN one of the ports becomes designated port for external communication from outside of the LAN connections.

## 3 References <a name="references"></a>

This document was generated with the help of:

- [Cisco article on LAN](https://www.cisco.com/c/en/us/products/switches/what-is-a-lan-local-area-network.html);
- [IT k Funde video on network basics](https://www.youtube.com/watch?v=_IOZ8_cPgu8);
- [Wikipedia article on subnetworks](https://en.wikipedia.org/wiki/Subnetwork);
- [Wikipedia article on OSI Model](https://en.wikipedia.org/wiki/OSI_model);
- [Wikipedia article on ARP](https://en.wikipedia.org/wiki/Address_Resolution_Protocol)
- [Wikipedia article on IPv4](https://en.wikipedia.org/wiki/Internet_Protocol_version_4)
- [Article about IPv4 classes](https://public.support.unisys.com/aseries/docs/ClearPath-MCP-20.0/37877693-226/section-000021666.html)
- [Wikipedia article on IPv6](https://en.wikipedia.org/wiki/IPv6)
- [Wikipedia article on routing tables](https://en.wikipedia.org/wiki/Routing_table)
- [Wikipedia article on BGP](https://en.wikipedia.org/wiki/Border_Gateway_Protocol)
- [Wikipedia article on OSPF](https://en.wikipedia.org/wiki/Open_Shortest_Path_First)
- [Juniper article on VxLAN](https://www.juniper.net/us/en/research-topics/what-is-vxlan.html)
- [Juniper article on EVPN](https://www.juniper.net/us/en/research-topics/what-is-evpn-vxlan.html)
