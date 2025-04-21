ADJTIME_CONFIG(5)							 File formats							     ADJTIME_CONFIG(5)

NAME
       adjtime_config - information about hardware clock setting and drift factor

SYNOPSIS
       /etc/adjtime

DESCRIPTION
       The file /etc/adjtime contains descriptive information about the hardware mode clock setting and clock drift factor. The file is read and write by
       hwclock(8); and read by programs like rtcwake to get RTC time mode.

       The file is usually located in /etc, but tools like hwclock(8) or rtcwake(8) can use alternative location by command line options if write access to
       /etc is unwanted. The default clock mode is "UTC" if the file is missing.

       The Hardware Clock is usually not very accurate. However, much of its inaccuracy is completely predictable - it gains or loses the same amount of time
       every day. This is called systematic drift. The util hwclock(8) keeps the file /etc/adjtime, that keeps some historical information. For more details
       see "The Adjust Function" and "The Adjtime File" sections from hwclock(8) man page.

       The adjtime file is formatted in ASCII.

   First line
       Three numbers, separated by blanks:

       drift factor
	   the systematic drift rate in seconds per day (floating point decimal)

       last adjust time
	   the resulting number of seconds since 1969 UTC of most recent adjustment or calibration (decimal integer)

       adjustment status
	   zero (for compatibility with clock(8)) as a floating point decimal

   Second line
       last calibration time
	   The resulting number of seconds since 1969 UTC of most recent calibration. Zero if there has been no calibration yet or it is known that any
	   previous calibration is moot (for example, because the Hardware Clock has been found, since that calibration, not to contain a valid time). This is
	   a decimal integer.

   Third line
       clock mode
	   Supported values are UTC or LOCAL. Tells whether the Hardware Clock is set to Coordinated Universal Time or local time. You can always override
	   this value with options on the hwclock(8) command line.

FILES
       /etc/adjtime

SEE ALSO
       hwclock(8), rtcwake(8)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       adjtime_config is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-10-23							     ADJTIME_CONFIG(5)
