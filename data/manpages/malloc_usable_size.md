malloc_usable_size(3)						   Library Functions Manual						 malloc_usable_size(3)

NAME
       malloc_usable_size - obtain size of block of memory allocated from heap

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <malloc.h>

       size_t malloc_usable_size(void *_Nullable ptr);

DESCRIPTION
       This function can be used for diagnostics or statistics about allocations from malloc(3) or a related function.

RETURN VALUE
       malloc_usable_size() returns a value no less than the size of the block of allocated memory pointed to by ptr.  If ptr is NULL, 0 is returned.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ malloc_usable_size()													   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       GNU.

CAVEATS
       The value returned by malloc_usable_size() may be greater than the requested size of the allocation because of various internal implementation details,
       none  of	 which	the programmer should rely on.	This function is intended to only be used for diagnostics and statistics; writing to the excess memory
       without first calling realloc(3) to resize the allocation is not supported.  The returned value is only valid at the time of the call.

SEE ALSO
       malloc(3)

Linux man-pages 6.7							  2023-10-31							 malloc_usable_size(3)
