strfry(3)							   Library Functions Manual							     strfry(3)

NAME
       strfry - randomize a string

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #define _GNU_SOURCE	   /* See feature_test_macros(7) */
       #include <string.h>

       char *strfry(char *string);

DESCRIPTION
       The strfry() function randomizes the contents of string by randomly swapping characters in the string.  The result is an anagram of string.

RETURN VALUE
       The strfry() functions returns a pointer to the randomized string.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ strfry()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       GNU.

SEE ALSO
       memfrob(3), string(3)

Linux man-pages 6.7							  2023-10-31								     strfry(3)
