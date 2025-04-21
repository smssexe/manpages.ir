INIT-D-SCRIPT(5)						      File Formats Manual						      INIT-D-SCRIPT(5)

NAME
       init-d-script — interpreter for short and simple init.d scripts

DESCRIPTION
       Generic init.d script framework to reduce the redundant code in /etc/init.d/.  The goal is to create an init.d script that is Debian and LSB compliant.
       When the Debian policy conflicts with the LSB, the Debian policy takes precedence.

       This is a simple example on how init-d-script can be used to start and stop a daemon with PID file support:

	     #!/bin/sh /lib/init/init-d-script
	     ### BEGIN INIT INFO
	     # Provides:	  atd
	     # Required-Start:	  $syslog $time $remote_fs
	     # Required-Stop:	  $syslog $time $remote_fs
	     # Default-Start:	  2 3 4 5
	     # Default-Stop:	  0 1 6
	     # Short-Description: run at jobs
	     # Description:	  Debian init script to start the daemon
	     #			  running at jobs.
	     ### END INIT INFO
	     DAEMON=/usr/sbin/atd

       The following variables affect behaviour of an init script:

       DAEMON	      Path  to daemon being started.  If the init script is not supposed to start any kind of daemon, it should be set to “none” and the func‐
		      tions do_start_override(), do_stop_override() and do_status_override() should be defined instead.

       DAEMON_ARGS    Additional arguments, passed to daemon during start.

       DESC	      Full name or short description of the daemon, printed on screen.	If unset, this variable defaults to the “NAME” value.

       NAME	      Additional environment variables are sourced from /etc/default/${NAME}.  If unset,  this	variable  defaults  to	the  basename  of  the
		      “DAEMON” value.

       COMMAND_NAME   If  this	variable  is  set,  it is used as argument to the --name option of start-stop-daemon(8).  It may be useful if the value of the
		      “NAME” variable is longer than the command name length supported by the running kernel.  If the value is verbatim	 “none”,  the  command
		      name will not be used to match the processes.  If unset, this variable defaults to the “NAME” value.

       PIDFILE	      Path  to	file  where  the  process  identifier of the started daemon will be stored during start.  If the value is verbatim “none”, the
		      process identifier will not be stored in any file.  If this variable is not set, it gets a sensible default value, so it is rarely  nec‐
		      essary to set this variable explicitly.

       RELOAD_SIGNAL  Signal  number  or  name (without the SIG prefix) that will be sent to the process on reload.  If the daemon performs reload action upon
		      receiving a SIGHUP signal, this variable should be set to “1” or “HUP”.

       The variables RELOAD_ARGS, START_ARGS and STOP_ARGS are additional arguments, passed to start-stop-daemon(8) during reload, start and stop actions,  to
       override the default options.

       Additionally,  it  is  possible	to  change the behaviour of the resulting shell script by overriding some of the internal functions.  To do so, define
       function with an _override suffix.  So, for example, to override the do_status() function, one should  define  a	 do_status_override()  function.   The
       exception to this rule is the do_reload() function, whose override should be defined as-is, without the above-mentioned suffix.

       Here is a control flow chart that explains what functions are called and when:

	     /etc/init.d/script start
	       do_start
		 do_start_prepare # no-op
		 do_start_cmd	  # start-stop-daemon is called here
		 do_start_cleanup # no-op

	     /etc/init.d/script stop
	       do_stop
		 do_stop_prepare # no-op
		 do_stop_cmd	 # start-stop-daemon is called here
		 do_stop_cleanup # no-op

	     /etc/init.d/script status
	       do_status

	     /etc/init.d/script reload
	       do_reload
		 do_usage
		 exit 3

	     /etc/init.d/script force-reload
	       do_force_reload
		 do_reload   # if overridden
		 do_restart
		   do_restart_prepare
		   do_stop_cmd
		   do_start_cmd
		   do_restart_cleanup

	     /etc/init.d/script restart
	       do_force_restart
	     /etc/init.d/script try-restart
	       if do_status; then
		 do_restart
		   do_restart_prepare
		   do_stop_cmd	# start-stop-daemon is called here
		   do_start_cmd # start-stop-daemon is called here
		   do_restart_cleanup

	     /etc/init.d/script <arg>
	       do_unknown <arg>
		 exit 3

	     /etc/init.d/script
	       do_usage

       As  can	be  seen,  by  default, the script does not support the reload action; it should be implemented by the script writer by defining a do_reload()
       function.

       If do_reload() is not defined but do_reload_cmd() is, the latter will be called on reload, after do_reload_prepare() and before do_reload_cleanup().

SEE ALSO
       inittab(8), service(8), update-rc.d(8).

AUTHORS
       Petter Reinholdtsen <pere@debian.org>

Debian									August 5, 2019							      INIT-D-SCRIPT(5)
