va_list(3type)																	va_list(3type)

NAME
       va_list - variable argument list

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <stdarg.h>

       typedef /* ... */  va_list;

DESCRIPTION
       Used by functions with a varying number of arguments of varying types.  The function must declare an object of type va_list which is used by the macros
       va_start(3), va_arg(3), va_copy(3), and va_end(3) to traverse the list of arguments.

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C89, POSIX.1-2001.

NOTES
       The following headers also provide va_list: <stdio.h> and <wchar.h>.

SEE ALSO
       va_start(3), va_arg(3), va_copy(3), va_end(3)

Linux man-pages 6.7							  2023-10-31								va_list(3type)
