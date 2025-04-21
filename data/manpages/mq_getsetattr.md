mq_getsetattr(2)						      System Calls Manual						      mq_getsetattr(2)

NAME
       mq_getsetattr - get/set message queue attributes

SYNOPSIS
       #include <mqueue.h>	     /* Definition of struct mq_attr */
       #include <sys/syscall.h>	     /* Definition of SYS_* constants */
       #include <unistd.h>

       int syscall(SYS_mq_getsetattr, mqd_t mqdes,
		   const struct mq_attr *newattr, struct mq_attr *oldattr);

DESCRIPTION
       Do not use this system call.

       This  is the low-level system call used to implement mq_getattr(3) and mq_setattr(3).  For an explanation of how this system call operates, see the de‐
       scription of mq_setattr(3).

STANDARDS
       None.

NOTES
       Never call it unless you are writing a C library!

SEE ALSO
       mq_getattr(3), mq_overview(7)

Linux man-pages 6.7							  2023-10-31							      mq_getsetattr(2)
