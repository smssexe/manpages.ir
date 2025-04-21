memfrob(3)							   Library Functions Manual							    memfrob(3)

NAME
       memfrob - frobnicate (obfuscate) a memory area

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #define _GNU_SOURCE	       /* See feature_test_macros(7) */
       #include <string.h>

       void *memfrob(void s[.n], size_t n);

DESCRIPTION
       The  memfrob()  function obfuscates the first n bytes of the memory area s by exclusive-ORing each character with the number 42.	 The effect can be re‐
       versed by using memfrob() on the obfuscated memory area.

       Note that this function is not a proper encryption routine as the XOR constant is fixed, and is suitable only for hiding strings.

RETURN VALUE
       The memfrob() function returns a pointer to the obfuscated memory area.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ memfrob()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       GNU.

SEE ALSO
       bstring(3), strfry(3)

Linux man-pages 6.7							  2023-10-31								    memfrob(3)
