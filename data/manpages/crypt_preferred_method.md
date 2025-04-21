CRYPT_PREFERRED_METHOD(3)					    Library Functions Manual					     CRYPT_PREFERRED_METHOD(3)

NAME
       crypt_preferred_method — get the prefix of the preferred hash method

LIBRARY
       Crypt Library (libcrypt, -lcrypt)

SYNOPSIS
       #include <crypt.h>

       const char*
       crypt_preferred_method(void);

DESCRIPTION
       crypt_preferred_method is a convenience function to get the prefix of the preferred hash method.	 If a preferred method is available, it is the same as
       the one also used by the crypt_gensalt functions, if their given prefix parameter is NULL.

RETURN VALUES
       The  string  returned  equals  the  prefix  of the preferred hash method.  If no preferred hash method is available it is NULL.	It is safe to pass the
       string returned by crypt_preferred_method directly to crypt_gensalt without prior string-sanitizing nor NULL-pointer checks.

FEATURE TEST MACROS
       <crypt.h> will define the macro CRYPT_PREFERRED_METHOD_AVAILABLE if crypt_preferred_method is available in the current version of libxcrypt.

PORTABILITY NOTES
       The function crypt_preferred_method is not part of any standard.	 It was added to libxcrypt in version 4.4.0.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌────────────────────────┬───────────────┬─────────┐
       │ Interface		│ Attribute	│ Value	  │
       ├────────────────────────┼───────────────┼─────────┤
       │ crypt_preferred_method │ Thread safety │ MT-Safe │
       └────────────────────────┴───────────────┴─────────┘

SEE ALSO
       crypt_gensalt(3)

libxcrypt							       November 16, 2018					     CRYPT_PREFERRED_METHOD(3)
