ntp_gettime(3)							   Library Functions Manual							ntp_gettime(3)

NAME
       ntp_gettime, ntp_gettimex  - get time parameters (NTP daemon interface)

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <sys/timex.h>

       int ntp_gettime(struct ntptimeval *ntv);
       int ntp_gettimex(struct ntptimeval *ntv);

DESCRIPTION
       Both of these APIs return information to the caller via the ntv argument, a structure of the following type:

	   struct ntptimeval {
	       struct timeval time;    /* Current time */
	       long maxerror;	       /* Maximum error */
	       long esterror;	       /* Estimated error */
	       long tai;	       /* TAI offset */

	       /* Further padding bytes allowing for future expansion */
	   };

       The fields of this structure are as follows:

       time   The current time, expressed as a timeval structure:

		  struct timeval {
		      time_t	  tv_sec;   /* Seconds since the Epoch */
		      suseconds_t tv_usec;  /* Microseconds */
		  };

       maxerror
	      Maximum  error, in microseconds.	This value can be initialized by ntp_adjtime(3), and is increased periodically (on Linux: each second), but is
	      clamped to an upper limit (the kernel constant NTP_PHASE_MAX, with a value of 16,000).

       esterror
	      Estimated error, in microseconds.	 This value can be set via ntp_adjtime(3) to contain an estimate of the difference between  the	 system	 clock
	      and the true time.  This value is not used inside the kernel.

       tai    TAI (Atomic International Time) offset.

       ntp_gettime() returns an ntptimeval structure in which the time, maxerror, and esterror fields are filled in.

       ntp_gettimex() performs the same task as ntp_gettime(), but also returns information in the tai field.

RETURN VALUE
       The return values for ntp_gettime() and ntp_gettimex() are as for adjtimex(2).  Given a correct pointer argument, these functions always succeed.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ ntp_gettime(), ntp_gettimex()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       ntp_gettime()
	      NTP Kernel Application Program Interface.

       ntp_gettimex()
	      GNU.

HISTORY
       ntp_gettime()
	      glibc 2.1.

       ntp_gettimex()
	      glibc 2.12.

SEE ALSO
       adjtimex(2), ntp_adjtime(3), time(7)

       NTP "Kernel Application Program Interface"

Linux man-pages 6.7							  2023-10-31								ntp_gettime(3)
