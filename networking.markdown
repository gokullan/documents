# Networking

## How the internet works
-   By connecting computers to routers, then routers to routers, we are able to
    scale infinitely.
-   Your Home network -> Modem (connection to telephone infrastructure) -> ISP 
    -> Other network
-   An ISP is a company that manages some special routers that are all linked
    together and can also access other ISPs' routers

## HTTP
-   Response [codes](https://datatracker.ietf.org/doc/html/rfc7231#section-6)
    -   1xx : Informational
    -   2xx : Successful
    -   3xx : Redirection
        -   301 : Moved permanently
        -   307 : Moved temporarily
    -   4xx : Client error
        -   410 : Gone
    -   5xx : Server error
    -   HTTP status codes have consequences on caching, and handling of URIs on the client side
-   Methods
    -   GET
    -   POST
    -   PUT
    -   DELETE
    -   HEAD
    -   OPTIONS
    -   TRACE
    -   CONNECT
## Network Devices
-   Repeaters
-   Hub - multi-port repeaters
-   Bridge - only 2 ports; learns devices on each side
-   Switch - faciliates communication *within* a network
    -   3 actions: Learn, Flood, Forward
    -   Maintain Port No. to MAC mapping
    -   Broadcast is a type of *frame* in which the L2 header contains FF:FF:FF:FF:FF:FF as the destination MAC; Flooding is the action of duplicating and forwarding the frame to all hosts on the switch's network.
    -   Switch has both IP and MAC
        -  A switch sends a broadcast frame only if traffic is going *to* or *from* (**NOT** *through*) it, (i.e.), if the switch itself is a host (eg: logging into the switch for configuring it, etc.)
-   Router - faciliates communication *between* networks
    -   Has IP (gateway address) (and MAC?) associated at every interface

## OSI 
-   Segment (TCP header + data) -> Packet (Segment + IP) -> Frame (Packet + MAC)

## Address Resolution Protocol (ARP)
-  Maps IP to MAC

## Transport Layer
-   Addressing scheme: Ports
    -   Clients select random port to establish connection 
        (response traffic arrives on this port);
        server listens to specific port (client makes request to this specific port);
    -   0-65535 ($2^{16} = 65536$)

## Subnetting
-   [Reference](http://subnetipv4.com/)

## Proxies
-   Forward
-   Reverse

## CDN

## VPN
-   Site-to-site (IPSec)
-   Remote access (TLS)
-   [VPN vs. TLS](https://security.stackexchange.com/questions/1476/what-is-the-difference-in-security-between-a-vpn-and-a-ssl-connection)

## Doubts
-   Intranet example
-   Payload vs. traffic
-   NIC and Wifi-Access-Cards
-   Routers have MAC?
-   VLAN
-   URL vs. URI
-   CDN
-   Browser caching
-   Bridge vs. Router
-   Firewall
-   Switches
    -   MAC address table should include MAC to Port mapping? (or Port to MAC mapping?)
    -   When a switch floods a network, does it add its own MAC?
-   If I start, say a Hapi server, can other devices connected to the internet
    access it?

## References
-   MDN Documentation
