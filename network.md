# Networking knowledge for interview.

# Table of contents

1. [LAN](#lan)
   1. [IP Address](#ip)
   2. [Switch](#switch)
   3. [Router](#router)
   4. [Subnet](#subnet)
   5. [Gateway](#gateway)
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

A switch is a device from the LAN that allows communication between the devices in the LAN. Based on the IP Addresses of the LAN devices, the switch can point the right package from one device to the desired device.

### 1.3 Router <a name="router"></a>

A router is a networking device that forwards data packets between different LAN networks, part of a WAN (Wide area network).

### 1.4 Subnet <a name="subnet"></a>

Subnet is a sub-network that is part of the LAN. It defines the range of the LAN. The practice of dividing a network into two or more networks is called subnetting. Computers that **belong to the same subnet are addressed** with **an identical most-significant bit-group in their IP addresses**. This results in the logical division of an IP address into two fields: **the network number or routing prefix** and **the rest field or host identifier**. The **rest field is an identifier for a specific host or network interface**. The routing prefix may be expressed in **Classless Inter-Domain Routing (CIDR)** notation written as the `first address of a network`, followed by a slash character (`/`), and **ending with the bit-length of the prefix**. For example, `198.51.100.0/24` is the prefix of the Internet Protocol version 4 network starting at the given address, having `24 bits allocated for the network prefix`, and the remaining `8 bits reserved for host addressing`. For IPv4, a network may also be characterized by its **subnet mask or netmask**, which is the **bitmask** that, when applied by a **bitwise AND operation to any IP address in the network, yields the routing prefix**. Subnet masks are also expressed in dot-decimal notation like an IP address. For example, the prefix `198.51.100.0/24` would have the subnet mask `255.255.255.0`.

### 1.5 Gateway <a name="gateway"></a>

IP Address of the router.

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
