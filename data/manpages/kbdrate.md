KBDRATE(8)							    System Manager's Manual							    KBDRATE(8)

NAME
       kbdrate - reset the keyboard repeat rate and delay time

SYNOPSIS
       kbdrate [options...]

DESCRIPTION
       kbdrate is used to change the keyboard repeat rate and delay time. The delay is the amount of time that a key must be depressed before it will start to
       repeat.

       Using  kbdrate without any options will reset the repeat rate to 10.9 characters per second (cps) and the delay to 250 milliseconds (ms) for Intel- and
       M68K-based systems.  These are the IBM defaults. On SPARC-based systems it will reset the repeat rate to 5 cps and the delay to 200 ms.

OPTIONS
       -r, --rate=NUMBER
	      Change the keyboard repeat rate to NUMBER cps. For Intel-based systems, the allowable range is from 2.0 to 30.0  cps.   Only  certain,  specific
	      values  are  possible, and the program will select the nearest possible value to the one specified. The possible values are given, in characters
	      per second, as follows: 2.0, 2.1, 2.3, 2.5, 2.7, 3.0, 3.3, 3.7, 4.0, 4.3, 4.6, 5.0, 5.5, 6.0, 6.7, 7.5, 8.0, 8.6, 9.2, 10.0, 10.9,  12.0,	 13.3,
	      15.0, 16.0, 17.1, 18.5, 20.0, 21.8, 24.0, 26.7, 30.0.  For SPARC-based systems, the allowable range is from 0 (no repeat) to 50 cps.

       -d, --delay=NUMBER
	      Change  the  delay to NUMBER milliseconds.  For Intel-based systems, the allowable range is from 250 to 1000 ms, in 250 ms steps. For SPARC sys‐
	      tems, possible values are between 10 ms and 1440 ms, in 10 ms steps.

       -s, --silent
	      Silent. No messages are printed.

       -h, --help
	      Display a help text.

       -V, --version
	      Display a version number and exit.

BUGS
       Not all keyboards support all rates.

       Not all keyboards have the rates mapped in the same way.

       Setting the repeat rate on the Gateway AnyKey keyboard does not work.  If someone with a Gateway figures out how to program the keyboard,  please  send
       mail to util-linux@math.uio.no.

       All  this  is  very architecture dependent.  Nowadays kbdrate first tries the KDKBDREP and KIOCSRATE ioctls.  (The former usually works on an m68k/i386
       machine, the latter for SPARC.)	When these ioctls fail an ioport interface.

FILES
       /etc/rc.local
       /dev/port

kbd									 22 June 1994								    KBDRATE(8)
