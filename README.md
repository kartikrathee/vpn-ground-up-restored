[English](README.md)

# Build your own Zerotier

## Introduction

Implement a L2 VPN similar to Zerotier or a Virtual Switch.

It simulates the behavior of a physical switch, providing Ethernet frame exchange services for devices connected to the switch's ports.

The difference is that the ports of this virtual switch can be connected to devices all over the world through the Internet, making them appear to be in the same local area network for the operating system.

## Background Knowledge

### What is Network Switch?

A network switch is networking hardware that connects devices on a computer network by using packet switching to receive and forward data to the destination device.

A network switch is a multiport network bridge that uses MAC addresses to forward data at the data link layer (layer 2) of the OSI model. Some switches can also forward data at the network layer (layer 3) by additionally incorporating routing functionality. Such switches are commonly known as layer-3 switches or multilayer switches.

In this project, we focues on layer-2 switchs, which recognize and forward Ethernet frames. When forwarding packets, switches use a forwarding table to look up the port corresponding to the destination address.

In a switch, the forwarding table is generally called the MAC address table. This table maintains the MAC addresses known in the local network and their corresponding ports. When a switch receives a Ethernet frame, it looks up the port corresponding to the destination MAC address in the forwarding table, and forwards the data frame only to that port, thereby achieving data forwarding within the local area network. If the destination MAC address is not in the table, the switch forwards the Ethernet frame to all ports except the source port so that the target device can respond and update the forwarding table.

In this project, we will write a program called VSwitch as a virtual switch to achieve Ethernet frame exchange function.

### Virtual Network Device: TAP

TAP is a type of virtual network device that can simulate a physical network interface, allowing operating systems and applications to use it like a physical interface. TAP devices are commonly used to create virtual private network (VPN) connections between different computers for secure data transmission over public networks.

The TAP device is implemented in the operating system kernel. It looks like a regular network interface and can be used in applications like a regular physical network card. When packets are sent through the TAP device, they are passed to the TUN/TAP driver in the kernel, which passes the packets to the application. The application can process the packets and pass them to other devices or networks. Similarly, when applications send packets, they are passed to the TUN/TAP driver, which forwards them to the specified target device or network.

