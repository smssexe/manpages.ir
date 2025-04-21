open_how(2type)																       open_how(2type)

NAME
       open_how - how to open a pathname

LIBRARY
       Linux kernel headers

SYNOPSIS
       #include <linux/openat2.h>

       struct open_how {
	   u64	flags;	  /* O_* flags */
	   u64	mode;	  /* Mode for O_{CREAT,TMPFILE} */
	   u64	resolve;  /* RESOLVE_* flags */
	   /* ... */
       };

DESCRIPTION
       Specifies how a pathname should be opened.

       The fields are as follows:

       flags  This field specifies the file creation and file status flags to use when opening the file.

       mode   This field specifies the mode for the new file.

       resolve
	      This  is	a  bit mask of flags that modify the way in which all components of a pathname will be resolved (see path_resolution(7) for background
	      information).

VERSIONS
       Extra fields may be appended to the structure, with a zero value in a new field resulting in the kernel behaving as though that extension field was not
       present.	 Therefore, a user must zero-fill this structure on initialization.

STANDARDS
       Linux.

SEE ALSO
       openat2(2)

Linux man-pages 6.7							  2023-10-31							       open_how(2type)
