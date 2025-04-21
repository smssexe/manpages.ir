PERF-ARCHIVE(1)								  perf Manual							       PERF-ARCHIVE(1)

NAME
       perf-archive - Create archive with object files with build-ids found in perf.data file

SYNOPSIS
       perf archive [file]

DESCRIPTION
       This command runs perf-buildid-list --with-hits, and collects the files with the buildids found so that analysis of perf.data contents can be possible
       on another machine.

SEE ALSO
       perf-record(1), perf-buildid-list(1), perf-report(1)

perf									  03/14/2025							       PERF-ARCHIVE(1)
