malloc_stats(3)							   Library Functions Manual						       malloc_stats(3)

NAME
       malloc_stats - print memory allocation statistics

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <malloc.h>

       void malloc_stats(void);

DESCRIPTION
       The  malloc_stats()  function prints (on standard error) statistics about memory allocated by malloc(3) and related functions.  For each arena (alloca‐
       tion area), this function prints the total amount of memory allocated and the total number of bytes consumed by in-use allocations.  (These two	values
       correspond  to  the arena and uordblks fields retrieved by mallinfo(3).)	 In addition, the function prints the sum of these two statistics for all are‐
       nas, and the maximum number of blocks and bytes that were ever simultaneously allocated using mmap(2).

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ malloc_stats()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       GNU.

HISTORY
       glibc 2.0.

NOTES
       More detailed information about memory allocations in the main arena can be obtained using mallinfo(3).

SEE ALSO
       mmap(2), mallinfo(3), malloc(3), malloc_info(3), mallopt(3)

Linux man-pages 6.7							  2023-10-31							       malloc_stats(3)
