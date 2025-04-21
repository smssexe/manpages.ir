SYSTEMD-FSCKD.SERVICE(8)					     systemd-fsckd.service					      SYSTEMD-FSCKD.SERVICE(8)

NAME
       systemd-fsckd.service, systemd-fsckd.socket, systemd-fsckd - File system check progress reporting

SYNOPSIS
       systemd-fsckd.service

       systemd-fsckd.socket

       /usr/lib/systemd/systemd-fsckd

DESCRIPTION
       systemd-fsckd.service is a service responsible for receiving file system check progress, and communicating some consolidated data to console and
       plymouth (if running). It also handles possible check cancellations.

       systemd-fsckd receives messages about file system check progress from fsck through an UNIX domain socket. It can display the progress of the least
       advanced fsck as well as the total number of devices being checked in parallel to the console. It will also send progress messages to plymouth. Both
       the raw data and translated messages are sent, so compiled plymouth themes can use the raw data to display custom messages, and scripted themes, not
       supporting i18n, can display the translated versions.

       systemd-fsckd will instruct plymouth to grab Control+C keypresses. When the key is pressed, running checks will be terminated. It will also cancel any
       newly connected fsck instances for the lifetime of systemd-fsckd.

PROTOCOL FOR COMMUNICATION WITH PLYMOUTH
       systemd-fsckd passes the following messages to the theme:

       Progress update, sent as a plymouth update message: "fsckd:<num_devices>:<progress>:<string>"

       "<num_devices>"
	   the current number of devices being checked (int)

       "<progress>"
	   the current minimum percentage of all devices being checking (float, from 0 to 100)

       "<string>"
	   a translated message ready to be displayed by the plymouth theme displaying the data above. It can be overridden by themes supporting i18n.

       Cancel message, sent as a traditional plymouth message: "fsckd-cancel-msg:<string>"

       "<strings>"
	   a translated string ready to be displayed by the plymouth theme indicating that Control+C can be used to cancel current checks. It can be
	   overridden (matching only "fsckd-cancel-msg" prefix) by themes supporting i18n.

OPTIONS
       The following options are understood:

       -h, --help
	   Print a short help text and exit.

       --version
	   Print a short version string and exit.

EXIT STATUS
       On success, 0 is returned, a non-zero failure code otherwise. Note that the daemon stays idle for a while to accept new fsck connections before
       exiting.

SEE ALSO
       systemd(1), systemd-fsck(8), fsck(8), systemd-quotacheck.service(8), fsck.btrfs(8), fsck.cramfs(8), fsck.ext4(8), fsck.fat(8), fsck.hfsplus(8),
       fsck.minix(8), fsck.ntfs(8), fsck.xfs(8)

systemd 255															      SYSTEMD-FSCKD.SERVICE(8)
