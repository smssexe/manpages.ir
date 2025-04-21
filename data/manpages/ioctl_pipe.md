ioctl_pipe(2)							      System Calls Manual							 ioctl_pipe(2)

NAME
       ioctl_pipe - ioctl() operations for General notification mechanism

SYNOPSIS
       #include <linux/watch_queue.h>  /* Definition of IOC_WATCH_QUEUE_* */
       #include <sys/ioctl.h>

       int ioctl(int pipefd[1], IOC_WATCH_QUEUE_SET_SIZE, int size);
       int ioctl(int pipefd[1], IOC_WATCH_QUEUE_SET_FILTER,
		 struct watch_notification_filter *filter);

DESCRIPTION
       The  following  ioctl(2)	 operations  are  provided  to	set up general notification queue parameters.  The notification queue is built on the top of a
       pipe(2) opened with the O_NOTIFICATION_PIPE flag.

       IOC_WATCH_QUEUE_SET_SIZE (since Linux 5.8)
	      Preallocates the pipe buffer memory so that it can fit size notification messages.  Currently, size must be between 1 and 512.

       IOC_WATCH_QUEUE_SET_FILTER (since Linux 5.8)
	      Watch queue filter can limit events that are received.  Filters are passed in a struct watch_notification_filter and each filter is described by
	      a struct watch_notification_type_filter structure.

		  struct watch_notification_filter {
			  __u32	  nr_filters;
			  __u32	  __reserved;
			  struct watch_notification_type_filter filters[];
		  };

		  struct watch_notification_type_filter {
			  __u32	  type;
			  __u32	  info_filter;
			  __u32	  info_mask;
			  __u32	  subtype_filter[8];
		  };

SEE ALSO
       pipe(2), ioctl(2)

Linux man-pages 6.7							  2023-10-31								 ioctl_pipe(2)
