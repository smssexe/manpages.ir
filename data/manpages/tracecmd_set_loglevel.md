LIBTRACECMD(3)							       libtracefs Manual							LIBTRACECMD(3)

NAME
       tracecmd_set_loglevel - Set log level of the library

SYNOPSIS
       #include <trace-cmd.h>

       int tracecmd_set_loglevel(enum tep_loglevel level);

DESCRIPTION
       The tracecmd_set_loglevel() function sets the level of the library logs that will be printed on the console. See libtraceevent(3) for detailed
       desciription of the log levels. Setting the log level to specific value means that logs from the previous levels will be printed too. For example
       TEP_LOG_WARNING will print any logs with severity TEP_LOG_WARNING, TEP_LOG_ERROR and TEP_LOG_CRITICAL. The default log level is TEP_LOG_CRITICAL. When
       a new level is set, it is also propagated to the libtracefs and libtraceevent.

EXAMPLE
	   #include <trace-cmd.h>
	   ...
	   tracecmd_set_loglevel(TEP_LOG_ALL);
	   ...
	   /* call libtracecmd, libtracefs or libtraceevent APIs and observe any logs they produce */
	   ...
	   tracecmd_set_loglevel(TEP_LOG_CRITICAL);

FILES
	   trace-cmd.h
		   Header file to include in order to have access to the library APIs.
	   -ltracecmd
		   Linker switch to add when building a program that uses the library.

SEE ALSO
       libtracefs(3), libtraceevent(3), trace-cmd(1) trace-cmd.dat(5)

AUTHOR
	   Steven Rostedt <rostedt@goodmis.org[1]>
	   Tzvetomir Stoyanov <tz.stoyanov@gmail.com[2]>

REPORTING BUGS
       Report bugs to <linux-trace-devel@vger.kernel.org[3]>

LICENSE
       libtracecmd is Free Software licensed under the GNU LGPL 2.1

RESOURCES
       https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/

COPYING
       Copyright (C) 2021 VMware, Inc. Free use of this software is granted under the terms of the GNU Public License (GPL).

NOTES
	1. rostedt@goodmis.org
	   mailto:rostedt@goodmis.org

	2. tz.stoyanov@gmail.com
	   mailto:tz.stoyanov@gmail.com

	3. linux-trace-devel@vger.kernel.org
	   mailto:linux-trace-devel@vger.kernel.org

libtracefs								  04/08/2024								LIBTRACECMD(3)
