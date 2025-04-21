getloadavg(3)							   Library Functions Manual							 getloadavg(3)

NAME
       getloadavg - get system load averages

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <stdlib.h>

       int getloadavg(double loadavg[], int nelem);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       getloadavg():
	   Since glibc 2.19:
	       _DEFAULT_SOURCE
	   In glibc up to and including 2.19:
	       _BSD_SOURCE

DESCRIPTION
       The  getloadavg()  function returns the number of processes in the system run queue averaged over various periods of time.  Up to nelem samples are re‐
       trieved and assigned to successive elements of loadavg[].  The system imposes a maximum of 3 samples, representing averages over the last 1, 5, and  15
       minutes, respectively.

RETURN VALUE
       If the load average was unobtainable, -1 is returned; otherwise, the number of samples actually retrieved is returned.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ getloadavg()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       BSD.

HISTORY
       4.3BSD-Reno, Solaris.  glibc 2.2.

SEE ALSO
       uptime(1), proc(5)

Linux man-pages 6.7							  2023-10-31								 getloadavg(3)
