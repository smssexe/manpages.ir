strncat(3)							   Library Functions Manual							    strncat(3)

NAME
       strncat - append non-null bytes from a source array to a string, and null-terminate the result

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <string.h>

       char *strncat(char *restrict dst, const char src[restrict .ssize],
		     size_t ssize);

DESCRIPTION
       This  function appends at most ssize non-null bytes from the array pointed to by src, followed by a null character, to the end of the string pointed to
       by dst.	dst must point to a string contained in a buffer that is large enough, that is, the buffer size must be at least  strlen(dst)  +  strnlen(src,
       ssize) + 1.

       An implementation of this function might be:

	   char *
	   strncat(char *restrict dst, const char *restrict src, size_t ssize)
	   {
	       #define strnul(s)  (s + strlen(s))

	       stpcpy(mempcpy(strnul(dst), src, strnlen(src, ssize)), "");
	       return dst;
	   }

RETURN VALUE
       strncat() returns dst.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ strncat()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C89, SVr4, 4.3BSD.

CAVEATS
       The name of this function is confusing; it has no relation to strncpy(3).

       If  the	destination  buffer  does  not	already	 contain  a  string,  or  is not large enough, the behavior is undefined.  See _FORTIFY_SOURCE in fea‐
       ture_test_macros(7).

BUGS
       This function can be very inefficient.  Read about Shlemiel the painter.

EXAMPLES
       #include <err.h>
       #include <stdio.h>
       #include <stdlib.h>
       #include <string.h>

       #define nitems(arr)  (sizeof((arr)) / sizeof((arr)[0]))

       int
       main(void)
       {
	   size_t  n;

	   // Null-padded fixed-size character sequences
	   char	   pre[4] = "pre.";
	   char	   new_post[50] = ".foo.bar";

	   // Strings
	   char	   post[] = ".post";
	   char	   src[] = "some_long_body.post";
	   char	   *dest;

	   n = nitems(pre) + strlen(src) - strlen(post) + nitems(new_post) + 1;
	   dest = malloc(sizeof(*dest) * n);
	   if (dest == NULL)
	       err(EXIT_FAILURE, "malloc()");

	   dest[0] = '\0';  // There's no 'cpy' function to this 'cat'.
	   strncat(dest, pre, nitems(pre));
	   strncat(dest, src, strlen(src) - strlen(post));
	   strncat(dest, new_post, nitems(new_post));

	   puts(dest);	// "pre.some_long_body.foo.bar"
	   free(dest);
	   exit(EXIT_SUCCESS);
       }

SEE ALSO
       string(3), string_copying(7)

Linux man-pages 6.7							  2023-12-05								    strncat(3)
