SYSTEMD-GETTY-GENERATOR(8)					    systemd-getty-generator					    SYSTEMD-GETTY-GENERATOR(8)

NAME
       systemd-getty-generator - Generator for enabling getty instances on the console

SYNOPSIS
       /usr/lib/systemd/system-generators/systemd-getty-generator

DESCRIPTION
       systemd-getty-generator is a generator that automatically instantiates serial-getty@.service on the kernel consoles, if they can function as ttys and
       are not provided by the virtual console subsystem. It will also instantiate serial-getty@.service instances for virtualizer consoles, if execution in a
       virtualized environment is detected. If execution in a container environment is detected, it will instead enable console-getty.service for
       /dev/console, and container-getty@.service instances for additional container pseudo TTYs as requested by the container manager (see Container
       Interface[1]). This should ensure that the user is shown a login prompt at the right place, regardless of which environment the system is started in.
       For example, it is sufficient to redirect the kernel console with a kernel command line argument such as console= to get both kernel messages and a
       getty prompt on a serial TTY. See The kernel's command-line parameters[2] for more information on the console= kernel parameter.

       systemd-getty-generator implements systemd.generator(7).

       Further information about configuration of gettys can be found in systemd for Administrators, Part XVI: Gettys on Serial Consoles (and Elsewhere)[3].

KERNEL COMMAND LINE
       systemd-getty-generator understands the following kernel-command-line(7) parameters:

       systemd.getty_auto=
	   this options take an optional boolean argument, and default to yes. The generator is enabled by default, and a false value may be used to disable
	   it.

	   Added in version 250.

ENVIRONMENT
       $SYSTEMD_GETTY_AUTO
	   This variable takes an optional boolean argument, and default to yes. The generator is enabled by default, and a false value may be used to disable
	   it.

	   Added in version 250.

SYSTEM CREDENTIALS
       getty.ttys.serial, getty.ttys.container
	   These system credentials may be used to spawn additional login prompts on selected TTYs. The two credentials should contain a newline-separated
	   list of TTY names to spawn instances of serial-getty@.service (in case of getty.ttys.serial) and container-getty@.service (in case of
	   getty.ttys.container) on.

	   Added in version 254.

SEE ALSO
       systemd(1), kernel-command-line(7), systemd.system-credentials(7), agetty(8)

NOTES
	1. Container
	       Interface
	   https://systemd.io/CONTAINER_INTERFACE

	2. The kernel's command-line parameters
	   https://docs.kernel.org/admin-guide/kernel-parameters.html

	3. systemd for Administrators, Part XVI: Gettys on Serial Consoles (and Elsewhere)
	   https://0pointer.de/blog/projects/serial-console.html

systemd 255															    SYSTEMD-GETTY-GENERATOR(8)
