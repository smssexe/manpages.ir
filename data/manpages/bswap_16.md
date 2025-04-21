bswap(3)							   Library Functions Manual							      bswap(3)

NAME
       bswap_16, bswap_32, bswap_64 - reverse order of bytes

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <byteswap.h>

       uint16_t bswap_16(uint16_t x);
       uint32_t bswap_32(uint32_t x);
       uint64_t bswap_64(uint64_t x);

DESCRIPTION
       These functions return a value in which the order of the bytes in their 2-, 4-, or 8-byte arguments is reversed.

RETURN VALUE
       These functions return the value of their argument with the bytes reversed.

ERRORS
       These functions always succeed.

STANDARDS
       GNU.

EXAMPLES
       The program below swaps the bytes of the 8-byte integer supplied as its command-line argument.  The following shell session demonstrates the use of the
       program:

	   $ ./a.out 0x0123456789abcdef
	   0x123456789abcdef ==> 0xefcdab8967452301

   Program source

       #include <byteswap.h>
       #include <inttypes.h>
       #include <stdint.h>
       #include <stdio.h>
       #include <stdlib.h>

       int
       main(int argc, char *argv[])
       {
	   uint64_t x;

	   if (argc != 2) {
	       fprintf(stderr, "Usage: %s <num>\n", argv[0]);
	       exit(EXIT_FAILURE);
	   }

	   x = strtoull(argv[1], NULL, 0);
	   printf("%#" PRIx64 " ==> %#" PRIx64 "\n", x, bswap_64(x));

	   exit(EXIT_SUCCESS);
       }

SEE ALSO
       byteorder(3), endian(3)

Linux man-pages 6.7							  2023-10-31								      bswap(3)
