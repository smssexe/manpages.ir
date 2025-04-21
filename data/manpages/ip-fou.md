IP-FOU(8)								     Linux								     IP-FOU(8)

NAME
       ip-fou - Foo-over-UDP receive port configuration

       ip-gue - Generic UDP Encapsulation receive port configuration

SYNOPSIS
       ip [ OPTIONS ] fou  { COMMAND | help }

       ip fou add port PORT { gue | ipproto PROTO  } [ local IFADDR  ] [ peer IFADDR  ] [ peer_port PORT  ] [ dev IFNAME  ]
       ip fou del port PORT [ local IFADDR  ] [ peer IFADDR  ] [ peer_port PORT	 ] [ dev IFNAME	 ]
       ip fou show

DESCRIPTION
       The ip fou commands are used to create and delete receive ports for Foo-over-UDP (FOU) as well as Generic UDP Encapsulation (GUE).

       Foo-over-UDP allows encapsulating packets of an IP protocol directly over UDP. The receiver infers the protocol of a packet received on a FOU UDP port
       to be the protocol configured for the port.

       Generic UDP Encapsulation (GUE) encapsulates packets of an IP protocol within UDP and an encapsulation header. The encapsulation header contains the IP
       protocol number for the encapsulated packet.

       When creating a FOU or GUE receive port, the port number is specified in PORT argument. If FOU is used, the IP protocol number associated with the port
       is specified in PROTO argument. You can bind a port to a local address/interface, by specifying the address in the local IFADDR argument or the device
       in the IFNAME argument. If you would like to connect the port, you can specify the peer address in the peer IFADDR argument and peer port in the
       peer_port PORT argument.

       A FOU or GUE receive port is deleted by specifying PORT in the delete command, as well as local address/interface or peer address/port (if set).

EXAMPLES
   Configure a FOU receive port for GRE bound to 7777
       # ip fou add port 7777 ipproto 47

   Configure a FOU receive port for IPIP bound to 8888
       # ip fou add port 8888 ipproto 4

   Configure a GUE receive port bound to 9999
       # ip fou add port 9999 gue

   Delete the GUE receive port bound to 9999
       # ip fou del port 9999

   Configure a FOU receive port for GRE bound to 1.2.3.4:7777
       # ip fou add port 7777 ipproto 47 local 1.2.3.4

SEE ALSO
       ip(8)

AUTHOR
       Tom Herbert <therbert@google.com>

iproute2								  2 Nov 2014								     IP-FOU(8)
