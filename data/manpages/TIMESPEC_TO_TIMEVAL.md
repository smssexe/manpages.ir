TIMEVAL_TO_TIMESPEC(3)						   Library Functions Manual						TIMEVAL_TO_TIMESPEC(3)

NAME
       TIMEVAL_TO_TIMESPEC, TIMESPEC_TO_TIMEVAL - convert between time structures

SYNOPSIS
       #define _GNU_SOURCE
       #include <sys/time.h>

       void TIMEVAL_TO_TIMESPEC(const struct timeval *tv, struct timespec *ts);
       void TIMESPEC_TO_TIMEVAL(struct timeval *tv, const struct timespec *ts);

DESCRIPTION
       These macros convert from a timeval(3type) to a timespec(3type) structure, and vice versa, respectively.

       This is especially useful for writing interfaces that receive a type, but are implemented with calls to functions that receive the other one.

STANDARDS
       GNU, BSD.

Linux man-pages 6.7							  2024-03-12							TIMEVAL_TO_TIMESPEC(3)
