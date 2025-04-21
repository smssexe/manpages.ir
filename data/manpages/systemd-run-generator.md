SYSTEMD-RUN-GENERATOR(8)					     systemd-run-generator					      SYSTEMD-RUN-GENERATOR(8)

NAME
       systemd-run-generator - Generator for invoking commands specified on the kernel command line as system service

SYNOPSIS
       /usr/lib/systemd/system-generators/systemd-run-generator

DESCRIPTION
       systemd-run-generator is a generator that reads the kernel command line and understands three options:

       If the systemd.run= option is specified and followed by a command line, a unit named kernel-command-line.service is generated for it and booted into.
       The service has Type=oneshot set, and has SuccessAction=exit and FailureAction=exit configured by default, thus ensuring that the system is shut down
       as soon as the command completes. The exit status of the command line is propagated to the invoking container manager, if this applies (which might
       propagate this further, to the calling shell — e.g.  systemd-nspawn(7) does this). If this option is used multiple times the unit file will contain
       multiple ExecStart= lines, to execute all commands in order. The command is started as regular service, i.e. with DefaultDependencies= on.

       Use systemd.run_success_action= and systemd.run_failure_action= to tweak how to react to the process completing. In particular assigning "none" will
       leave the system running after the command completes. For further details on supported arguments, see systemd.unit(5).

       systemd-run-generator implements systemd.generator(7).

EXAMPLE
       Use a command like the following to add a user to the user database inside a container run with systemd-nspawn(7):

	   # systemd-nspawn -D mycontainer -b systemd.run='"adduser test"'

       (Note the requirement for double quoting in the command line above. The first level of quoting ('') is processed and removed by the command shell used
       to invoke systemd-nspawn. The second level of quoting ("") is propagated to the kernel command line of the container and processed and removed by
       systemd-run-generator. Both together make sure both words of the specified command line adduser test end up in the generated unit file together and are
       neither split apart by the command shell nor by the generator.)

SEE ALSO
       systemd(1), systemctl(1), kernel-command-line(7), systemd-nspawn(7), systemd.unit(5), systemd.service(5)

systemd 255															      SYSTEMD-RUN-GENERATOR(8)
