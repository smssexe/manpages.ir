BYTEORDER(3)							   Library Functions Manual							  BYTEORDER(3)

NAME
       htonl, htons, ntohl, ntohs - convert values between host and network byte order

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <arpa/inet.h>

       uint32_t htonl(uint32_t hostlong);
       uint16_t htons(uint16_t hostshort);

       uint32_t ntohl(uint32_t netlong);
       uint16_t ntohs(uint16_t netshort);

DESCRIPTION
       The htonl() function converts the unsigned integer hostlong from host byte order to network byte order.

       The htons() function converts the unsigned short integer hostshort from host byte order to network byte order.

       The ntohl() function converts the unsigned integer netlong from network byte order to host byte order.

       The ntohs() function converts the unsigned short integer netshort from network byte order to host byte order.

       On  the	i386  the  host	 byte order is Least Significant Byte first, whereas the network byte order, as used on the Internet, is Most Significant Byte
       first.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ htonl(), htons(), ntohl(), ntohs()											   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

SEE ALSO
       bswap(3), endian(3), gethostbyname(3), getservent(3)

Linux man-pages 6.7							  2023-10-31								  BYTEORDER(3)
