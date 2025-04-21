MPATHPERSIST(8)							    System Manager's Manual						       MPATHPERSIST(8)

NAME
       mpathpersist - Manages SCSI persistent reservations on dm multipath devices.

SYNOPSIS
       mpathpersist [OPTIONS] device

DESCRIPTION
       This  utility  is  used	to  manage SCSI persistent reservations on Device Mapper Multipath devices. To be able to use this functionality, the reserva‐
       tion_key attribute must be defined in the /etc/multipath.conf file. Otherwise the multipathd daemon will not check for persistent reservation for newly
       discovered paths or reinstated paths.

       mpathpersist supports the same command-line options as the sg_persist utility.  Consult the sg_persist (8) manual page for an  in-depth	discussion  of
       the various options.

OPTIONS
       -verbose|-v level
	      Verbosity:

	      0	   Critical messages.

	      1	   Error messages.

	      2	   Warning messages.

	      3	   Informational messages.

	      4	   Informational messages with trace enabled.

       --device=DEVICE|-d DEVICE
	      Query or change DEVICE.

       --batch-file=DEVICE|-f FILE
	      Read commands from FILE. See section "BATCH FILES" below. This option can be given at most once.

       --help|-h
	      Output this usage message.

       --hex|-H
	      Output response in hex.

       --in|-i
	      Request PR In command.

       --out|-o
	      Request PR Out command.

       --param-alltgpt|-Y
	      PR Out parameter 'ALL_TG_PT'.

       --param-aptpl|-Z
	      PR Out parameter 'APTPL'.

       --read-keys|-k
	      PR In: Read Keys.

       --param-rk=RK|-K RK
	      PR Out parameter reservation key (RK is in hex, up to 8 bytes).

       --param-sark=SARK|-S SARK
	      PR Out parameter service action reservation key (SARK is in hex).

       --preempt|-P
	      PR Out: Preempt.

       --clear|-C
	      PR Out: Clear registrations.

       --preempt-abort|-A
	      PR Out: Preempt and Abort.

       --prout-type=TYPE|-T TYPE
	      PR Out command type.

       --read-full-status|-s
	      PR In: Read Full Status.

       --read-keys|-k
	      PR In: Read Keys.

       --read-reservation|-r
	      PR In: Read Reservation.

       --register|-G
	      PR Out: Register.

       --register-ignore|-I
	      PR Out: Register and Ignore.

       --release|-L
	      PR Out: Release.

       --report-capabilities|-c
	      PR In: Report Capabilities.

       --reserve|-R
	      PR Out: Reserve.

       --transport-id=TIDS|-X TIDS
	      TransportIDs can be mentioned in several forms.

       --alloc-length=LEN|-l LEN
	      PR In: maximum allocation length. LEN is a decimal number between 0 and 8192.

EXAMPLE
       Register the key "123abc" for the /dev/mapper/mpath9 device:
	      mpathpersist --out --register --param-sark=123abc /dev/mapper/mpath9

       Read registered reservation keys for the /dev/mapper/mpath9 device:
	      mpathpersist -i -k /dev/mapper/mpath9

       Create a reservation for the /dev/mapper/mpath9 device with the given reservation key:
	      mpathpersist --out --reserve --param-rk=123abc --prout-type=8 -d /dev/mapper/mpath9

       Read the reservation status of the /dev/mapper/mpath9 device:
	      mpathpersist -i -s -d /dev/mapper/mpath9

       Release the previously created reservation (note that the prout-type needs to be the same as above):
	      mpathpersist --out --release --param-rk=123abc --prout-type=8 -d /dev/mapper/mpath9

       Remove the current key registered for this host (i.e. reset it to 0):
	      mpathpersist --out --register-ignore -K 123abc -S 0 /dev/mapper/mpath9

       Remove current reservation, and unregister all registered keys from all I_T nexuses:
	      mpathpersist -oCK 123abc /dev/mapper/mpath9

BATCH FILES
       The  option  --batch-file  (-f) sets an input file to be processed by mpathpersist. Grouping commands in batch files can provide a speed improvement in
       particular on large installments, because mpathpersist needs to scan existing paths and maps only once during startup.

       The input file is a text file that is parsed line by line. Every line of the file is interpreted as a command line (i.e. list of	 options  and  parame‐
       ters) for mpathpersist. Options and parameters are separated by one or more whitespace characters (space or TAB).  Lines can, but do not have to, begin
       with the word "mpathpersist".  The "#" character, either at the beginning of the line or following some whitespace, denotes the start of a comment that
       lasts until the end of the line. Empty lines are allowed. Continuation of mpathpersist commands over multiple lines is not supported.

       All options listed in this man page, except -f and -v, are allowed in batch files. Both short and long option formats may be used.  Using the -f option
       inside the batch file is an error. The -v option is ignored in batch files.

       The  multipath map on which to act must be specified on every input line, e.g. using the -d option.  Commands acting on different multipath maps may be
       combined in a batch file, and multiple commands may act on the same multipath map. Commands are executed one by one, so that commands further  down  in
       the  file  see  status  changes caused by previous commands.  If mpathpersist encounters an error while processing a line in the batch file, batch file
       processing is not aborted; subsequent commands are executed nonetheless. The exit status of mpathpersist is the status of the first failed command,  or
       0 if all commands succeeded.

       If  other options and parameters are used along with -f on the mpathpersist command line, the command line will be executed first, followed by the com‐
       mands from the batch file.

       Below is an example of a valid batch input file.

	      # This is an mpathpersist input file.
	      # Short and long forms of the same command
	      -i -k /dev/dm-1 # short form, this comment is ignored
	      mpathpersist --in --read-keys --device=/dev/dm-1

	      # Mixing of long and short options, variable white space
		--out  --register    -S	 abcde	   /dev/dm-1

	      # Mixing of commands for different maps
	      -ir /dev/dm-0
	      -ir /dev/dm-1

	      mpathpersist --out --param-rk abcde --reserve --prout-type 5 /dev/dm-1
	      # This should now show a reservation
	      -ir /dev/dm-1
	      -oCK abcde /dev/dm-1
	      --in --read-reservation /dev/dm-1

SEE ALSO
       multipath(8), multipathd(8), sg_persist(8).

AUTHORS
       multipath-tools was developed by Christophe Varoqui <christophe.varoqui@opensvc.com> and others.

Linux									  2021-11-12							       MPATHPERSIST(8)
