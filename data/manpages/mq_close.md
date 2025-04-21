mq_close(3)							   Library Functions Manual							   mq_close(3)

NAME
       mq_close - close a message queue descriptor

LIBRARY
       Real-time library (librt, -lrt)

SYNOPSIS
       #include <mqueue.h>

       int mq_close(mqd_t mqdes);

DESCRIPTION
       mq_close() closes the message queue descriptor mqdes.

       If  the	calling	 process has attached a notification request (see mq_notify(3)) to this message queue via mqdes, then this request is removed, and an‐
       other process can now attach a notification request.

RETURN VALUE
       On success mq_close() returns 0; on error, -1 is returned, with errno set to indicate the error.

ERRORS
       EBADF  The message queue descriptor specified in mqdes is invalid.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ mq_close()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

NOTES
       All open message queues are automatically closed on process termination, or upon execve(2).

SEE ALSO
       mq_getattr(3), mq_notify(3), mq_open(3), mq_receive(3), mq_send(3), mq_unlink(3), mq_overview(7)

Linux man-pages 6.7							  2023-10-31								   mq_close(3)
