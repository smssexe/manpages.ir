canonicalize_file_name(3)					   Library Functions Manual					     canonicalize_file_name(3)

NAME
       canonicalize_file_name - return the canonicalized absolute pathname

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #define _GNU_SOURCE	   /* See feature_test_macros(7) */
       #include <stdlib.h>

       char *canonicalize_file_name(const char *path);

DESCRIPTION
       The  canonicalize_file_name()  function	returns a null-terminated string containing the canonicalized absolute pathname corresponding to path.	In the
       returned string, symbolic links are resolved, as are .  and ..  pathname components.  Consecutive slash (/) characters are replaced by a single slash.

       The returned string is dynamically allocated by canonicalize_file_name() and the caller should deallocate it with free(3) when  it  is  no  longer  re‐
       quired.

       The call canonicalize_file_name(path) is equivalent to the call:

	   realpath(path, NULL);

RETURN VALUE
       On  success, canonicalize_file_name() returns a null-terminated string.	On error (e.g., a pathname component is unreadable or does not exist), canoni‐
       calize_file_name() returns NULL and sets errno to indicate the error.

ERRORS
       See realpath(3).

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ canonicalize_file_name()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       GNU.

SEE ALSO
       readlink(2), realpath(3)

Linux man-pages 6.7							  2023-10-31						     canonicalize_file_name(3)
