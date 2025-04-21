get_kernel_syms(2)						      System Calls Manual						    get_kernel_syms(2)

NAME
       get_kernel_syms - retrieve exported kernel and module symbols

SYNOPSIS
       #include <linux/module.h>

       [[deprecated]] int get_kernel_syms(struct kernel_sym *table);

DESCRIPTION
       Note: This system call is present only before Linux 2.6.

       If table is NULL, get_kernel_syms() returns the number of symbols available for query.  Otherwise, it fills in a table of structures:

	   struct kernel_sym {
	       unsigned long value;
	       char	     name[60];
	   };

       The  symbols  are interspersed with magic symbols of the form #module-name with the kernel having an empty name.	 The value associated with a symbol of
       this form is the address at which the module is loaded.

       The symbols exported from each module follow their magic module tag and the modules are returned in the reverse of the order in which they were loaded.

RETURN VALUE
       On success, returns the number of symbols copied to table.  On error, -1 is returned and errno is set to indicate the error.

ERRORS
       There is only one possible error return:

       ENOSYS get_kernel_syms() is not supported in this version of the kernel.

STANDARDS
       Linux.

HISTORY
       Removed in Linux 2.6.

       This obsolete system call is not supported by glibc.  No declaration is provided in glibc headers, but, through a quirk of history, glibc versions  be‐
       fore  glibc 2.23 did export an ABI for this system call.	 Therefore, in order to employ this system call, it was sufficient to manually declare the in‐
       terface in your code; alternatively, you could invoke the system call using syscall(2).

BUGS
       There is no way to indicate the size of the buffer allocated for table.	If symbols have been added to the kernel since the  program  queried  for  the
       symbol table size, memory will be corrupted.

       The length of exported symbol names is limited to 59 characters.

       Because	of these limitations, this system call is deprecated in favor of query_module(2) (which is itself nowadays deprecated in favor of other inter‐
       faces described on its manual page).

SEE ALSO
       create_module(2), delete_module(2), init_module(2), query_module(2)

Linux man-pages 6.7							  2023-10-31							    get_kernel_syms(2)
