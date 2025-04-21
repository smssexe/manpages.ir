epoll_event(3type)															    epoll_event(3type)

NAME
       epoll_event, epoll_data, epoll_data_t - epoll event

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <sys/epoll.h>

       struct epoll_event {
	   uint32_t	 events;  /* Epoll events */
	   epoll_data_t	 data;	  /* User data variable */
       };

       union epoll_data {
	   void	    *ptr;
	   int	     fd;
	   uint32_t  u32;
	   uint64_t  u64;
       };

       typedef union epoll_data	 epoll_data_t;

DESCRIPTION
       The epoll_event structure specifies data that the kernel should save and return when the corresponding file descriptor becomes ready.

VERSIONS
   C library/kernel differences
       The Linux kernel headers also provide this type, with a slightly different definition:

	   #include <linux/eventpoll.h>

	   struct epoll_event {
	       __poll_t	 events;
	       __u64	 data;
	   };

STANDARDS
       Linux.

SEE ALSO
       epoll_wait(2), epoll_ctl(2)

Linux man-pages 6.7							  2023-10-31							    epoll_event(3type)
