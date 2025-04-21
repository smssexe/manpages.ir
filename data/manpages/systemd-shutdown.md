SYSTEMD-POWEROFF.SERVICE(8)					   systemd-poweroff.service					   SYSTEMD-POWEROFF.SERVICE(8)

NAME
       systemd-poweroff.service, systemd-halt.service, systemd-reboot.service, systemd-kexec.service, systemd-shutdown - System shutdown logic

SYNOPSIS
       systemd-poweroff.service

       systemd-halt.service

       systemd-reboot.service

       systemd-kexec.service

       /usr/lib/systemd/systemd-shutdown

       /usr/lib/systemd/system-shutdown/

DESCRIPTION
       systemd-poweroff.service is a system service that is pulled in by poweroff.target and is responsible for the actual system power-off operation.
       Similarly, systemd-halt.service is pulled in by halt.target, systemd-reboot.service by reboot.target and systemd-kexec.service by kexec.target to
       execute the respective actions.

       When these services are run, they ensure that PID 1 is replaced by the /usr/lib/systemd/systemd-shutdown tool which is then responsible for the actual
       shutdown. Before shutting down, this binary will try to unmount all remaining file systems (or at least remount them read-only), disable all remaining
       swap devices, detach all remaining storage devices and kill all remaining processes.

       It is necessary to have this code in a separate binary because otherwise rebooting after an upgrade might be broken — the running PID 1 could still
       depend on libraries which are not available any more, thus keeping the file system busy, which then cannot be re-mounted read-only.

       Shortly before executing the actual system power-off/halt/reboot/kexec systemd-shutdown will run all executables in /usr/lib/systemd/system-shutdown/
       and pass one arguments to them: either "poweroff", "halt", "reboot", or "kexec", depending on the chosen action. All executables in this directory are
       executed in parallel, and execution of the action is not continued before all executables finished. Note that these executables are run after all
       services have been shut down, and after most mounts have been detached (the root file system as well as /run/ and various API file systems are still
       around though). This means any programs dropped into this directory must be prepared to run in such a limited execution environment and not rely on
       external services or hierarchies such as /var/ to be around (or writable).

       Note that systemd-poweroff.service (and the related units) should never be executed directly. Instead, trigger system shutdown with a command such as
       "systemctl poweroff".

       Another form of shutdown is provided by the systemd-soft-reboot.service(8) functionality. It reboots only the OS userspace, leaving the kernel,
       firmware, and hardware as it is.

SEE ALSO
       systemd(1), systemctl(1), systemd.special(7), reboot(2), systemd-suspend.service(8), systemd-soft-reboot.service(8), bootup(7)

systemd 255															   SYSTEMD-POWEROFF.SERVICE(8)
