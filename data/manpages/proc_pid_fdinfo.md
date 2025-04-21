proc_pid_fdinfo(5)						      File Formats Manual						    proc_pid_fdinfo(5)

NAME
       /proc/pid/fdinfo/ - information about file descriptors

DESCRIPTION
       /proc/pid/fdinfo/ (since Linux 2.6.22)
	      This is a subdirectory containing one entry for each file which the process has open, named by its file descriptor.  The files in this directory
	      are  readable  only  by  the owner of the process.  The contents of each file can be read to obtain information about the corresponding file de‐
	      scriptor.	 The content depends on the type of file referred to by the corresponding file descriptor.

	      For regular files and directories, we see something like:

		  $ cat /proc/12015/fdinfo/4
		  pos:	  1000
		  flags:  01002002
		  mnt_id: 21

	      The fields are as follows:

	      pos    This is a decimal number showing the file offset.

	      flags  This is an octal number that displays the file access mode and file status flags (see open(2)).  If  the  close-on-exec  file  descriptor
		     flag is set, then flags will also include the value O_CLOEXEC.

		     Before Linux 3.1, this field incorrectly displayed the setting of O_CLOEXEC at the time the file was opened, rather than the current set‐
		     ting of the close-on-exec flag.

	      mnt_id This field, present since Linux 3.15, is the ID of the mount containing this file.	 See the description of /proc/pid/mountinfo.

	      For eventfd file descriptors (see eventfd(2)), we see (since Linux 3.8) the following fields:

		  pos: 0
		  flags:    02
		  mnt_id:   10
		  eventfd-count:	       40

	      eventfd-count is the current value of the eventfd counter, in hexadecimal.

	      For epoll file descriptors (see epoll(7)), we see (since Linux 3.8) the following fields:

		  pos: 0
		  flags:    02
		  mnt_id:   10
		  tfd:	      9 events:	      19 data: 74253d2500000009
		  tfd:	      7 events:	      19 data: 74253d2500000007

	      Each  of	the lines beginning tfd describes one of the file descriptors being monitored via the epoll file descriptor (see epoll_ctl(2) for some
	      details).	 The tfd field is the number of the file descriptor.  The events field is a hexadecimal mask of the events being  monitored  for  this
	      file descriptor.	The data field is the data value associated with this file descriptor.

	      For signalfd file descriptors (see signalfd(2)), we see (since Linux 3.8) the following fields:

		  pos: 0
		  flags:    02
		  mnt_id:   10
		  sigmask:  0000000000000006

	      sigmask  is the hexadecimal mask of signals that are accepted via this signalfd file descriptor.	(In this example, bits 2 and 3 are set, corre‐
	      sponding to the signals SIGINT and SIGQUIT; see signal(7).)

	      For inotify file descriptors (see inotify(7)), we see (since Linux 3.8) the following fields:

		  pos: 0
		  flags:    00
		  mnt_id:   11
		  inotify wd:2 ino:7ef82a sdev:800001 mask:800afff ignored_mask:0 fhandle-bytes:8 fhandle-type:1 f_handle:2af87e00220ffd73
		  inotify wd:1 ino:192627 sdev:800001 mask:800afff ignored_mask:0 fhandle-bytes:8 fhandle-type:1 f_handle:27261900802dfd73

	      Each of the lines beginning with "inotify" displays information about one file or directory that is being monitored.  The fields	in  this  line
	      are as follows:

	      wd     A watch descriptor number (in decimal).

	      ino    The inode number of the target file (in hexadecimal).

	      sdev   The ID of the device where the target file resides (in hexadecimal).

	      mask   The mask of events being monitored for the target file (in hexadecimal).

	      If  the  kernel  was  built  with exportfs support, the path to the target file is exposed as a file handle, via three hexadecimal fields: fhan‐
	      dle-bytes, fhandle-type, and f_handle.

	      For fanotify file descriptors (see fanotify(7)), we see (since Linux 3.8) the following fields:

		  pos: 0
		  flags:    02
		  mnt_id:   11
		  fanotify flags:0 event-flags:88002
		  fanotify ino:19264f sdev:800001 mflags:0 mask:1 ignored_mask:0 fhandle-bytes:8 fhandle-type:1 f_handle:4f261900a82dfd73

	      The fourth line displays information defined when the fanotify group was created via fanotify_init(2):

	      flags  The flags argument given to fanotify_init(2) (expressed in hexadecimal).

	      event-flags
		     The event_f_flags argument given to fanotify_init(2) (expressed in hexadecimal).

	      Each additional line shown in the file contains information about one of the marks in the fanotify group.	 Most of these fields are as for  ino‐
	      tify, except:

	      mflags The flags associated with the mark (expressed in hexadecimal).

	      mask   The events mask for this mark (expressed in hexadecimal).

	      ignored_mask
		     The mask of events that are ignored for this mark (expressed in hexadecimal).

	      For details on these fields, see fanotify_mark(2).

	      For timerfd file descriptors (see timerfd(2)), we see (since Linux 3.17) the following fields:

		  pos:	  0
		  flags:  02004002
		  mnt_id: 13
		  clockid: 0
		  ticks: 0
		  settime flags: 03
		  it_value: (7695568592, 640020877)
		  it_interval: (0, 0)

	      clockid
		     This  is  the numeric value of the clock ID (corresponding to one of the CLOCK_* constants defined via <time.h>) that is used to mark the
		     progress of the timer (in this example, 0 is CLOCK_REALTIME).

	      ticks  This is the number of timer expirations that have occurred, (i.e., the value that read(2) on it would return).

	      settime flags
		     This field lists the flags with which the timerfd was last armed (see timerfd_settime(2)), in octal (in this example, both	 TFD_TIMER_AB‐
		     STIME and TFD_TIMER_CANCEL_ON_SET are set).

	      it_value
		     This  field contains the amount of time until the timer will next expire, expressed in seconds and nanoseconds.  This is always expressed
		     as a relative value, regardless of whether the timer was created using the TFD_TIMER_ABSTIME flag.

	      it_interval
		     This field contains the interval of the timer, in seconds and nanoseconds.	 (The it_value and it_interval fields contain the values  that
		     timerfd_gettime(2) on this file descriptor would return.)

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							    proc_pid_fdinfo(5)
