lsearch(3)							   Library Functions Manual							    lsearch(3)

NAME
       lfind, lsearch - linear search of an array

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <search.h>

       void *lfind(const void key[.size], const void base[.size * .nmemb],
		   size_t *nmemb, size_t size,
		   int(*compar)(const void [.size], const void [.size]));
       void *lsearch(const void key[.size], void base[.size * .nmemb],
		   size_t *nmemb, size_t size,
		   int(*compar)(const void [.size], const void [.size]));

DESCRIPTION
       lfind()	and  lsearch() perform a linear search for key in the array base which has *nmemb elements of size bytes each.	The comparison function refer‐
       enced by compar is expected to have two arguments which point to the key object and to an array member, in that order, and which returns	 zero  if  the
       key object matches the array member, and nonzero otherwise.

       If  lsearch() does not find a matching element, then the key object is inserted at the end of the table, and *nmemb is incremented.  In particular, one
       should know that a matching element exists, or that more room is available.

RETURN VALUE
       lfind() returns a pointer to a matching member of the array, or NULL if no match is found.  lsearch() returns a pointer to a matching member of the ar‐
       ray, or to the newly added member if no match is found.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ lfind(), lsearch()													   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001, SVr4, 4.3BSD.  libc-4.6.27.

BUGS
       The naming is unfortunate.

SEE ALSO
       bsearch(3), hsearch(3), tsearch(3)

Linux man-pages 6.7							  2023-10-31								    lsearch(3)
