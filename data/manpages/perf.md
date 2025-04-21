PERF(1)									  perf Manual								       PERF(1)

NAME
       perf - Performance analysis tools for Linux

SYNOPSIS
       perf [--version] [--help] [OPTIONS] COMMAND [ARGS]

OPTIONS
       -h, --help
	   Run perf help command.

       -v, --version
	   Display perf version.

       -vv
	   Print the compiled-in status of libraries.

       --exec-path
	   Display or set exec path.

       --html-path
	   Display html documentation path.

       -p, --paginate
	   Set up pager.

       --no-pager
	   Do not set pager.

       --buildid-dir
	   Setup buildid cache directory. It has higher priority than buildid.dir config file option.

       --list-cmds
	   List the most commonly used perf commands.

       --list-opts
	   List available perf options.

       --debugfs-dir
	   Set debugfs directory or set environment variable PERF_DEBUGFS_DIR.

       --debug
	   Setup debug variable (see list below) in value range (0, 10). Use like: --debug verbose # sets verbose = 1 --debug verbose=2 # sets verbose = 2

	       List of debug variables allowed to set:
		 verbose	  - general debug messages
		 ordered-events	  - ordered events object debug messages
		 data-convert	  - data convert command debug messages
		 stderr		  - write debug output (option -v) to stderr
				    in browser mode
		 perf-event-open  - Print perf_event_open() arguments and
				    return value

       --debug-file
	   Write debug output to a specified file.

DESCRIPTION
       Performance counters for Linux are a new kernel-based subsystem that provide a framework for all things performance analysis. It covers hardware level
       (CPU/PMU, Performance Monitoring Unit) features and software features (software counters, tracepoints) as well.

SEE ALSO
       perf-stat(1), perf-top(1), perf-record(1), perf-report(1), perf-list(1)

       perf-annotate(1),perf-archive(1),perf-arm-spe(1), perf-bench(1), perf-buildid-cache(1), perf-buildid-list(1), perf-c2c(1), perf-config(1), perf-
       data(1), perf-diff(1), perf-evlist(1), perf-ftrace(1), perf-help(1), perf-inject(1), perf-intel-pt(1), perf-iostat(1), perf-kallsyms(1), perf-kmem(1),
       perf-kvm(1), perf-lock(1), perf-mem(1), perf-probe(1), perf-sched(1), perf-script(1), perf-test(1), perf-trace(1), perf-version(1)

perf									  03/14/2025								       PERF(1)
