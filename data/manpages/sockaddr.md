sockaddr(3type)																       sockaddr(3type)

NAME
       sockaddr, sockaddr_storage, sockaddr_in, sockaddr_in6, sockaddr_un, socklen_t, in_addr, in6_addr, in_addr_t, in_port_t, - socket address

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <sys/socket.h>

       struct sockaddr {
	   sa_family_t	   sa_family;	   /* Address family */
	   char		   sa_data[];	   /* Socket address */
       };

       struct sockaddr_storage {
	   sa_family_t	   ss_family;	   /* Address family */
       };

       typedef /* ... */ socklen_t;
       typedef /* ... */ sa_family_t;

   Internet domain sockets
       #include <netinet/in.h>

       struct sockaddr_in {
	   sa_family_t	   sin_family;	   /* AF_INET */
	   in_port_t	   sin_port;	   /* Port number */
	   struct in_addr  sin_addr;	   /* IPv4 address */
       };

       struct sockaddr_in6 {
	   sa_family_t	   sin6_family;	   /* AF_INET6 */
	   in_port_t	   sin6_port;	   /* Port number */
	   uint32_t	   sin6_flowinfo;  /* IPv6 flow info */
	   struct in6_addr sin6_addr;	   /* IPv6 address */
	   uint32_t	   sin6_scope_id;  /* Set of interfaces for a scope */
       };

       struct in_addr {
	   in_addr_t s_addr;
       };

       struct in6_addr {
	   uint8_t   s6_addr[16];
       };

       typedef uint32_t in_addr_t;
       typedef uint16_t in_port_t;

   UNIX domain sockets
       #include <sys/un.h>

       struct sockaddr_un {
	   sa_family_t	   sun_family;	   /* Address family */
	   char		   sun_path[];	   /* Socket pathname */
       };

DESCRIPTION
       sockaddr
	      Describes a socket address.

       sockaddr_storage
	      A	 structure  at	least  as  large as any other sockaddr_* address structures.  It's aligned so that a pointer to it can be cast as a pointer to
	      other sockaddr_* structures and used to access its fields.

       socklen_t
	      Describes the length of a socket address.	 This is an integer type of at least 32 bits.

       sa_family_t
	      Describes a socket's protocol family.  This is an unsigned integer type.

   Internet domain sockets
       sockaddr_in
	      Describes an IPv4 Internet domain socket address.	 The sin_port and sin_addr members are stored in network byte order.

       sockaddr_in6
	      Describes an IPv6 Internet domain socket address.	 The sin6_addr.s6_addr array is used to contain a 128-bit IPv6 address, stored in network byte
	      order.

   UNIX domain sockets
       sockaddr_un
	      Describes a UNIX domain socket address.

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

       socklen_t was invented by POSIX.	 See also accept(2).

       These structures were invented before modern ISO C strict-aliasing rules.  If aliasing rules are applied strictly, these structures would be  extremely
       difficult  to  use  without invoking Undefined Behavior.	 POSIX Issue 8 will fix this by requiring that implementations make sure that these structures
       can be safely used as they were designed.

NOTES
       socklen_t is also defined in <netdb.h>.

       sa_family_t is also defined in <netinet/in.h> and <sys/un.h>.

SEE ALSO
       accept(2), bind(2), connect(2), getpeername(2), getsockname(2), getsockopt(2),  sendto(2),  setsockopt(2),  socket(2),  socketpair(2),  getaddrinfo(3),
       gethostbyaddr(3), getnameinfo(3), htonl(3), ipv6(7), socket(7)

Linux man-pages 6.7							  2023-10-31							       sockaddr(3type)
