SYSTEMD-SOFT-REBOOT.SERVICE(8)					  systemd-soft-reboot.service					SYSTEMD-SOFT-REBOOT.SERVICE(8)

NAME
       systemd-soft-reboot.service - Userspace reboot operation

SYNOPSIS
       systemd-soft-reboot.service

DESCRIPTION
       systemd-soft-reboot.service is a system service that is pulled in by soft-reboot.target and is responsible for performing a userspace-only reboot
       operation. When invoked, it will send the SIGTERM signal to any processes left running (but does not wait for the processes to exit), and follow up
       with SIGKILL. If the /run/nextroot/ directory exists (which may be a regular directory, a directory mount point or a symlink to either) then it will
       switch the file system root to it. It then reexecutes the service manager off the (possibly now new) root file system, which will enqueue a new boot
       transaction as in a normal reboot.

       Such a userspace-only reboot operation permits updating or resetting the entirety of userspace with minimal downtime, as the reboot operation does not
       transition through:

       •   The second phase of regular shutdown, as implemented by systemd-shutdown(8).

       •   The third phase of regular shutdown, i.e. the return to the initrd context.

       •   The hardware reboot operation.

       •   The firmware initialization.

       •   The boot loader initialization.

       •   The kernel initialization.

       •   The initrd initialization.

       However this form of reboot comes with drawbacks as well:

       •   The OS update remains incomplete, as the kernel is not reset and continues running.

       •   Kernel settings (such as /proc/sys/ settings, a.k.a. "sysctl", or /sys/ settings) are not reset.

       These limitations may be addressed by various means, which are outside of the scope of this documentation, such as kernel live-patching and
       sufficiently comprehensive /etc/sysctl.d/ files.

RESOURCE PASS-THROUGH
       Various runtime OS resources can passed from a system runtime to the next, through the userspace reboot operation. Specifically:

       •   File descriptors placed in the file descriptor store of services that remain active until the very end are passed to the next boot, where they are
	   placed in the file descriptor store of the same unit. For this to work, units must declare DefaultDependencies=no (and avoid a manual
	   Conflicts=shutdown.target or similar) to ensure they are not terminated as usual during the system shutdown operation. Alternatively, use
	   FileDescriptorStorePreserve= to allow the file descriptor store to remain pinned even when the unit is down. See systemd.service(5) for details
	   about the file descriptor store.

       •   Similar to this, file descriptors associated with .socket units remain open (and connectible) if the units are not stopped during the transition.
	   (Achieved by DefaultDependencies=no.)

       •   The /run/ file system remains mounted and populated and may be used to pass state information between such userspace reboot cycles.

       •   Service processes may continue to run over the transition, past soft-reboot and into the next session, if they are placed in services that remain
	   active until the very end of shutdown (which again is achieved via DefaultDependencies=no). They must also be set up to avoid being killed by the
	   aforementioned SIGTERM and SIGKILL via SurviveFinalKillSignal=yes, and also be configured to avoid being stopped on isolate via
	   IgnoreOnIsolate=yes. They also have to be configured to be stopped on normal shutdown, reboot and maintenance mode. Finally, they have to be
	   ordered after basic.target to ensure correct ordeering on boot. Note that in case any new or custom units are used to isolate to, or that implement
	   an equivalent shutdown functionality, they will also have to be configured manually for correct ordering and conflicting. For example:

	       [Unit]
	       Description=My surviving service
	       SurviveFinalKillSignal=yes
	       IgnoreOnIsolate=yes
	       DefaultDependencies=no
	       After=basic.target
	       Conflicts=reboot.target
	       Before=reboot.target
	       Conflicts=kexec.target
	       Before=kexec.target
	       Conflicts=poweroff.target
	       Before=poweroff.target
	       Conflicts=halt.target
	       Before=halt.target
	       Conflicts=rescue.target
	       Before=rescue.target
	       Conflicts=emergency.target
	       Before=emergency.target

	       [Service]
	       Type=oneshot
	       ExecStart=sleep infinity

       •   File system mounts may remain mounted during the transition, and complex storage attached, if configured to remain until the very end of the
	   shutdown process. (Also achieved via DefaultDependencies=no, and by avoiding Conflicts=umount.target)

       •   If the unit publishes a service over D-Bus, the connection needs to be re-established after soft-reboot as the D-Bus broker will be stopped and
	   then started again. When using the sd-bus library this can be achieved by adapting the following example.

	       /* SPDX-License-Identifier: MIT-0 */

	       /* Implements a D-Bus service that automatically reconnects when the system bus is restarted.
		*
		* Compile with 'cc sd_bus_service_reconnect.c $(pkg-config --libs --cflags libsystemd)'
		*
		* To allow the program to take ownership of the name 'org.freedesktop.ReconnectExample',
		* add the following as /etc/dbus-1/system.d/org.freedesktop.ReconnectExample.conf
		* and then reload the broker with 'systemctl reload dbus':

	       <?xml version="1.0"?> <!--*-nxml-*-->
	       <!DOCTYPE busconfig PUBLIC "-//freedesktop//DTD D-BUS Bus Configuration 1.0//EN"
		       "http://www.freedesktop.org/standards/dbus/1.0/busconfig.dtd">
	       <busconfig>
		       <policy user="root">
			       <allow own="org.freedesktop.ReconnectExample"/>
			       <allow send_destination="org.freedesktop.ReconnectExample"/>
			       <allow receive_sender="org.freedesktop.ReconnectExample"/>
		       </policy>

		       <policy context="default">
			       <allow send_destination="org.freedesktop.ReconnectExample"/>
			       <allow receive_sender="org.freedesktop.ReconnectExample"/>
		       </policy>
	       </busconfig>

		*
		* To get the property via busctl:
		*
		* $ busctl --user get-property org.freedesktop.ReconnectExample \
		*			       /org/freedesktop/ReconnectExample \
		*			       org.freedesktop.ReconnectExample \
		*			       Example
		*   s "example"
		*/

	       #include <errno.h>
	       #include <stdio.h>
	       #include <stdlib.h>
	       #include <systemd/sd-bus.h>

	       #define _cleanup_(f) __attribute__((cleanup(f)))

	       #define check(x) ({			       \
		 int _r = (x);				       \
		 errno = _r < 0 ? -_r : 0;		       \
		 printf(#x ": %m\n");			       \
		 if (_r < 0)				       \
		   return EXIT_FAILURE;			       \
		 })

	       typedef struct object {
		 const char *example;
		 sd_bus **bus;
		 sd_event **event;
	       } object;

	       static int property_get(
			       sd_bus *bus,
			       const char *path,
			       const char *interface,
			       const char *property,
			       sd_bus_message *reply,
			       void *userdata,
			       sd_bus_error *error) {

		 object *o = userdata;

		 if (strcmp(property, "Example") == 0)
		   return sd_bus_message_append(reply, "s", o->example);

		 return sd_bus_error_setf(error,
					  SD_BUS_ERROR_UNKNOWN_PROPERTY,
					  "Unknown property '%s'",
					  property);
	       }

	       /* https://www.freedesktop.org/software/systemd/man/sd_bus_add_object.html */
	       static const sd_bus_vtable vtable[] = {
		 SD_BUS_VTABLE_START(0),
		 SD_BUS_PROPERTY(
		   "Example", "s",
		   property_get,
		   0,
		   SD_BUS_VTABLE_PROPERTY_CONST),
		 SD_BUS_VTABLE_END
	       };

	       static int setup(object *o);

	       static int on_disconnect(sd_bus_message *message, void *userdata, sd_bus_error *ret_error) {
		 check(setup((object *)userdata));
		 return 0;
	       }

	       /* Ensure the event loop exits with a clear error if acquiring the well-known service name fails */
	       static int request_name_callback(sd_bus_message *m, void *userdata, sd_bus_error *ret_error) {
		 if (!sd_bus_message_is_method_error(m, NULL))
		   return 1;

		 const sd_bus_error *error = sd_bus_message_get_error(m);

		 if (sd_bus_error_has_names(error, SD_BUS_ERROR_TIMEOUT, SD_BUS_ERROR_NO_REPLY))
		   return 1; /* The bus is not available, try again later */

		 printf("Failed to request name: %s\n", error->message);
		 object *o = userdata;
		 check(sd_event_exit(*o->event, -sd_bus_error_get_errno(error)));

		 return 1;
	       }

	       static int setup(object *o) {
		 /* If we are reconnecting, then the bus object needs to be closed, detached from
		  * the event loop and recreated.
		  * https://www.freedesktop.org/software/systemd/man/sd_bus_detach_event.html
		  * https://www.freedesktop.org/software/systemd/man/sd_bus_close_unref.html
		  */
		 if (*o->bus) {
		   check(sd_bus_detach_event(*o->bus));
		   *o->bus = sd_bus_close_unref(*o->bus);
		 }

		 /* Set up a new bus object for the system bus, configure it to wait for D-Bus to be available
		  * instead of failing if it is not, and start it. All the following operations are asyncronous
		  * and will not block waiting for D-Bus to be available.
		  * https://www.freedesktop.org/software/systemd/man/sd_bus_new.html
		  * https://www.freedesktop.org/software/systemd/man/sd_bus_set_address.html
		  * https://www.freedesktop.org/software/systemd/man/sd_bus_set_bus_client.html
		  * https://www.freedesktop.org/software/systemd/man/sd_bus_negotiate_creds.html
		  * https://www.freedesktop.org/software/systemd/man/sd_bus_set_watch_bind.html
		  * https://www.freedesktop.org/software/systemd/man/sd_bus_set_connected_signal.html
		  * https://www.freedesktop.org/software/systemd/man/sd_bus_start.html
		  */
		 check(sd_bus_new(o->bus));
		 check(sd_bus_set_address(*o->bus, "unix:path=/run/dbus/system_bus_socket"));
		 check(sd_bus_set_bus_client(*o->bus, 1));
		 check(sd_bus_negotiate_creds(*o->bus, 1, SD_BUS_CREDS_UID|SD_BUS_CREDS_EUID|SD_BUS_CREDS_EFFECTIVE_CAPS));
		 check(sd_bus_set_watch_bind(*o->bus, 1));
		 check(sd_bus_start(*o->bus));

		 /* Publish an interface on the bus, specifying our well-known object access
		  * path and public interface name.
		  * https://www.freedesktop.org/software/systemd/man/sd_bus_add_object.html
		  * https://dbus.freedesktop.org/doc/dbus-tutorial.html
		  */
		 check(sd_bus_add_object_vtable(*o->bus,
						NULL,
						"/org/freedesktop/ReconnectExample",
						"org.freedesktop.ReconnectExample",
						vtable,
						o));
		 /* By default the service is only assigned an ephemeral name. Also add a well-known
		  * one, so that clients know whom to call. This needs to be asynchronous, as
		  * D-Bus might not be yet available. The callback will check whether the error is
		  * expected or not, in case it fails.
		  * https://www.freedesktop.org/software/systemd/man/sd_bus_request_name.html
		  */
		 check(sd_bus_request_name_async(*o->bus,
						 NULL,
						 "org.freedesktop.ReconnectExample",
						 0,
						 request_name_callback,
						 o));
		 /* When D-Bus is disconnected this callback will be invoked, which will
		  * set up the connection again. This needs to be asynchronous, as D-Bus might not
		  * yet be available.
		  * https://www.freedesktop.org/software/systemd/man/sd_bus_match_signal_async.html
		  */
		 check(sd_bus_match_signal_async(*o->bus,
						 NULL,
						 "org.freedesktop.DBus.Local",
						 NULL,
						 "org.freedesktop.DBus.Local",
						 "Disconnected",
						 on_disconnect,
						 NULL,
						 o));
		 /* Attach the bus object to the event loop so that calls and signals are processed.
		  * https://www.freedesktop.org/software/systemd/man/sd_bus_attach_event.html
		  */
		 check(sd_bus_attach_event(*o->bus, *o->event, 0));

		 return 0;
	       }

	       int main(int argc, char **argv) {
		 /* The bus should be relinquished before the program terminates. The cleanup
		  * attribute allows us to do it nicely and cleanly whenever we exit the
		  * block.
		  */
		 _cleanup_(sd_bus_flush_close_unrefp) sd_bus *bus = NULL;
		 _cleanup_(sd_event_unrefp) sd_event *event = NULL;
		 object o = {
		   .example = "example",
		   .bus = &bus,
		   .event = &event,
		 };

		 /* Create an event loop data structure, with default parameters.
		  * https://www.freedesktop.org/software/systemd/man/sd_event_default.html
		  */
		 check(sd_event_default(&event));

		 /* By default the event loop will terminate when all sources have disappeared, so
		  * we have to keep it 'occupied'. Register signal handling to do so.
		  * https://www.freedesktop.org/software/systemd/man/sd_event_add_signal.html
		  */
		 check(sd_event_add_signal(event, NULL, SIGINT|SD_EVENT_SIGNAL_PROCMASK, NULL, NULL));
		 check(sd_event_add_signal(event, NULL, SIGTERM|SD_EVENT_SIGNAL_PROCMASK, NULL, NULL));

		 check(setup(&o));

		 /* Enter the main loop, it will exit only on sigint/sigterm.
		  * https://www.freedesktop.org/software/systemd/man/sd_event_loop.html
		  */
		 check(sd_event_loop(event));

		 /* https://www.freedesktop.org/software/systemd/man/sd_bus_release_name.html */
		 check(sd_bus_release_name(bus, "org.freedesktop.ReconnectExample"));

		 return 0;
	       }

       Even though passing resources from one soft reboot cycle to the next is possible this way, we strongly suggest to use this functionality sparingly
       only, as it creates a more fragile system as resources from different versions of the OS and applications might be mixed with unforeseen consequences.
       In particular it's recommended to avoid allowing processes to survive the soft reboot operation, as this means code updates will necessarily be
       incomplete, and processes typically pin various other resources (such as the file system they are backed by), thus increasing memory usage (as two
       versions of the OS/application/file system might be kept in memory). Leaving processes running during a soft-reboot operation requires disconnecting
       the service comprehensively from the rest of the OS, i.e. minimizing IPC and reducing sharing of resources with the rest of the OS. A possible
       mechanism to achieve this is the concept of Portable Services[1], but make sure no resource from the host's OS filesystems is pinned via BindPaths= or
       similar unit settings, otherwise the old, originating filesystem will remain mounted as long as the unit is running.

NOTES
       Note that because systemd-shutdown(8) is not executed, the executables in /usr/lib/systemd/system-shutdown/ are not executed either.

       Note that systemd-soft-reboot.service (and related units) should never be executed directly. Instead, trigger system shutdown with a command such as
       "systemctl soft-reboot".

       Note that if a new root file system has been set up on "/run/nextroot/", a soft-reboot will be performed when the reboot command is invoked.

SEE ALSO
       systemd(1), systemctl(1), systemd.special(7), systemd-poweroff.service(8), systemd-suspend.service(8), bootup(7)

NOTES
	1. Portable Services
	   https://systemd.io/PORTABLE_SERVICES

systemd 255															SYSTEMD-SOFT-REBOOT.SERVICE(8)
