wcsdup(3)							   Library Functions Manual							     wcsdup(3)

NAME
       wcsdup - duplicate a wide-character string

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wchar.h>

       wchar_t *wcsdup(const wchar_t *s);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       wcsdup():
	   Since glibc 2.10:
	       _POSIX_C_SOURCE >= 200809L
	   Before glibc 2.10:
	       _GNU_SOURCE

DESCRIPTION
       The  wcsdup()  function is the wide-character equivalent of the strdup(3) function.  It allocates and returns a new wide-character string whose initial
       contents is a duplicate of the wide-character string pointed to by s.

       Memory for the new wide-character string is obtained with malloc(3), and should be freed with free(3).

RETURN VALUE
       On success, wcsdup() returns a pointer to the new wide-character string.	 On error, it returns NULL, with errno set to indicate the error.

ERRORS
       ENOMEM Insufficient memory available to allocate duplicate string.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ wcsdup()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       libc5, glibc 2.0.

SEE ALSO
       strdup(3), wcscpy(3)

Linux man-pages 6.7							  2023-10-31								     wcsdup(3)
