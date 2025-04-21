void(3type)																	   void(3type)

NAME
       void - abstract type

SYNOPSIS
       void *

DESCRIPTION
       A pointer to any object type may be converted to a pointer to void and back.  POSIX further requires that any pointer, including pointers to functions,
       may be converted to a pointer to void and back.

       Conversions  from  and  to  any	other  pointer type are done implicitly, not requiring casts at all.  Note that this feature prevents any kind of type
       checking: the programmer should be careful not to convert a void * value to a type incompatible to that of the underlying data, because that would  re‐
       sult in undefined behavior.

       This  type  is  useful  in function parameters and return value to allow passing values of any type.  The function will typically use some mechanism to
       know the real type of the data being passed via a pointer to void.

       A value of this type can't be dereferenced, as it would give a value of type void, which is not possible.  Likewise, pointer arithmetic is not possible
       with this type.	However, in GNU C, pointer arithmetic is allowed as an extension to the standard; this is done by treating the size of a void or of  a
       function as 1.  A consequence of this is that sizeof is also allowed on void and on function types, and returns 1.

   Use with printf(3) and scanf(3)
       The conversion specifier for void * for the printf(3) and the scanf(3) families of functions is p.

VERSIONS
       The POSIX requirement about compatibility between void * and function pointers was added in POSIX.1-2008 Technical Corrigendum 1 (2013).

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C89, POSIX.1-2001.

SEE ALSO
       malloc(3), memcmp(3), memcpy(3), memset(3), intptr_t(3type)

Linux man-pages 6.7							  2023-10-31								   void(3type)
