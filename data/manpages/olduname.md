uname(2)							      System Calls Manual							      uname(2)

NAME
       uname - get name and information about current kernel

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <sys/utsname.h>

       int uname(struct utsname *buf);

DESCRIPTION
       uname() returns system information in the structure pointed to by buf.  The utsname struct is defined in <sys/utsname.h>:

	   struct utsname {
	       char sysname[];	  /* Operating system name (e.g., "Linux") */
	       char nodename[];	  /* Name within communications network
				     to which the node is attached, if any */
	       char release[];	  /* Operating system release
				     (e.g., "2.6.28") */
	       char version[];	  /* Operating system version */
	       char machine[];	  /* Hardware type identifier */
	   #ifdef _GNU_SOURCE
	       char domainname[]; /* NIS or YP domain name */
	   #endif
	   };

       The length of the arrays in a struct utsname is unspecified (see NOTES); the fields are terminated by a null byte ('\0').

RETURN VALUE
       On success, zero is returned.  On error, -1 is returned, and errno is set to indicate the error.

ERRORS
       EFAULT buf is not valid.

VERSIONS
       The domainname member (the NIS or YP domain name) is a GNU extension.

       The  length  of the fields in the struct varies.	 Some operating systems or libraries use a hardcoded 9 or 33 or 65 or 257.  Other systems use SYS_NMLN
       or _SYS_NMLN or UTSLEN or _UTSNAME_LENGTH.  Clearly, it is a bad idea to use any of these constants; just use sizeof(...).  SVr4 uses 257, "to  support
       Internet hostnames" — this is the largest value likely to be encountered in the wild.

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001, SVr4, 4.4BSD.

   C library/kernel differences
       Over  time,  increases  in  the size of the utsname structure have led to three successive versions of uname(): sys_olduname() (slot __NR_oldolduname),
       sys_uname() (slot __NR_olduname), and sys_newuname() (slot __NR_uname).	The first one used length 9 for all fields; the second used 65; the third also
       uses 65 but adds the domainname field.  The glibc uname() wrapper function hides these details from applications, invoking the most recent  version  of
       the system call provided by the kernel.

NOTES
       The  kernel  has the name, release, version, and supported machine type built in.  Conversely, the nodename field is configured by the administrator to
       match the network (this is what the BSD historically calls the "hostname", and is set via sethostname(2)).  Similarly, the domainname field is set  via
       setdomainname(2).

       Part of the utsname information is also accessible via /proc/sys/kernel/{ostype, hostname, osrelease, version, domainname}.

SEE ALSO
       uname(1), getdomainname(2), gethostname(2), uts_namespaces(7)

Linux man-pages 6.7							  2023-10-31								      uname(2)
