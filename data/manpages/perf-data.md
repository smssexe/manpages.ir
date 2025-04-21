PERF-DATA(1)								  perf Manual								  PERF-DATA(1)

NAME
       perf-data - Data file related processing

SYNOPSIS
       perf data [<common options>] <command> [<options>]",

DESCRIPTION
       Data file related processing.

COMMANDS
       convert
	   Converts perf data file into another format. It’s possible to set data-convert debug variable to get debug messages from conversion, like: perf
	   --debug data-convert data convert ...

OPTIONS FOR CONVERT
       --to-ctf
	   Triggers the CTF conversion, specify the path of CTF data directory.

       --to-json
	   Triggers JSON conversion. Specify the JSON filename to output.

       --tod
	   Convert time to wall clock time.

       -i
	   Specify input perf data file path.

       -f, --force
	   Don’t complain, do it.

       -v, --verbose
	   Be more verbose (show counter open errors, etc).

       --all
	   Convert all events, including non-sample events (comm, fork, ...), to output. Default is off, only convert samples.

SEE ALSO
       perf(1) [1] Common Trace Format - http://www.efficios.com/ctf

perf									  03/14/2025								  PERF-DATA(1)
