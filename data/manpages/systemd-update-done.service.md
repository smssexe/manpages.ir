SYSTEMD-UPDATE-DONE.SERVICE(8)					  systemd-update-done.service					SYSTEMD-UPDATE-DONE.SERVICE(8)

NAME
       systemd-update-done.service, systemd-update-done - Mark /etc/ and /var/ fully updated

SYNOPSIS
       systemd-update-done.service

       /usr/lib/systemd/systemd-update-done

DESCRIPTION
       systemd-update-done.service is a service that is invoked as part of the first boot after the vendor operating system resources in /usr/ have been
       updated. This is useful to implement offline updates of /usr/ which might require updates to /etc/ or /var/ on the following boot.

       systemd-update-done.service updates the file modification time (mtime) of the stamp files /etc/.updated and /var/.updated to the modification time of
       the /usr/ directory, unless the stamp files are already newer.

       Services that shall run after offline upgrades of /usr/ should order themselves before systemd-update-done.service, and use the ConditionNeedsUpdate=
       (see systemd.unit(5)) condition to make sure to run when /etc/ or /var/ are older than /usr/ according to the modification times of the files described
       above. This requires that updates to /usr/ are always followed by an update of the modification time of /usr/, for example by invoking touch(1) on it.

       Note that if the systemd.condition-needs-update= kernel command line option is used it overrides the ConditionNeedsUpdate= unit condition checks. In
       that case systemd-update-done.service will not reset the condition state until a follow-up reboot where the kernel switch is not specified anymore.

SEE ALSO
       systemd(1), systemd.unit(5), touch(1)

systemd 255															SYSTEMD-UPDATE-DONE.SERVICE(8)
