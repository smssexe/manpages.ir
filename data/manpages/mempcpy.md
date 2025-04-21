mempcpy(3)							   Library Functions Manual							    mempcpy(3)

NAME
       mempcpy, wmempcpy  - copy memory area

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #define _GNU_SOURCE	   /* See feature_test_macros(7) */
       #include <string.h>

       void *mempcpy(void dest[restrict .n], const void src[restrict .n],
		     size_t n);

       #define _GNU_SOURCE	   /* See feature_test_macros(7) */
       #include <wchar.h>

       wchar_t *wmempcpy(wchar_t dest[restrict .n],
		     const wchar_t src[restrict .n],
		     size_t n);

DESCRIPTION
       The mempcpy() function is nearly identical to the memcpy(3) function.  It copies n bytes from the object beginning at src into the object pointed to by
       dest.  But instead of returning the value of dest it returns a pointer to the byte following the last written byte.

       This function is useful in situations where a number of objects shall be copied to consecutive memory positions.

       The wmempcpy() function is identical but takes wchar_t type arguments and copies n wide characters.

RETURN VALUE
       dest + n.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ mempcpy(), wmempcpy()													   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       GNU.

HISTORY
       glibc 2.1.

EXAMPLES
       void *
       combine(void *o1, size_t s1, void *o2, size_t s2)
       {
	   void *result = malloc(s1 + s2);
	   if (result != NULL)
	       mempcpy(mempcpy(result, o1, s1), o2, s2);
	   return result;
       }

SEE ALSO
       memccpy(3), memcpy(3), memmove(3), wmemcpy(3)

Linux man-pages 6.7							  2023-10-31								    mempcpy(3)
