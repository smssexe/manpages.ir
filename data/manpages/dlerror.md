dlerror(3)							   Library Functions Manual							    dlerror(3)

NAME
       dlerror - obtain error diagnostic for functions in the dlopen API

LIBRARY
       Dynamic linking library (libdl, -ldl)

SYNOPSIS
       #include <dlfcn.h>

       char *dlerror(void);

DESCRIPTION
       The  dlerror() function returns a human-readable, null-terminated string describing the most recent error that occurred from a call to one of the func‐
       tions in the dlopen API since the last call to dlerror().  The returned string does not include a trailing newline.

       dlerror() returns NULL if no errors have occurred since initialization or since it was last called.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ dlerror()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       glibc 2.0.  POSIX.1-2001.

       SunOS.

NOTES
       The message returned by dlerror() may reside in a statically allocated buffer that is overwritten by subsequent dlerror() calls.

EXAMPLES
       See dlopen(3).

SEE ALSO
       dladdr(3), dlinfo(3), dlopen(3), dlsym(3)

Linux man-pages 6.7							  2023-10-31								    dlerror(3)
