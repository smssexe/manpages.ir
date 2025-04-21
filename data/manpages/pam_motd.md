PAM_MOTD(8)							       Linux-PAM Manual								   PAM_MOTD(8)

NAME
       pam_motd - Display the motd file

SYNOPSIS

       pam_motd.so [motd=/path/filename] [motd_dir=/path/dirname.d]

DESCRIPTION
       pam_motd is a PAM module that can be used to display arbitrary motd (message of the day) files after a successful login. By default, pam_motd shows
       files in the following locations:

	   /etc/motd
	   /run/motd
	   /usr/lib/motd
	   /etc/motd.d/
	   /run/motd.d/
	   /usr/lib/motd.d/

       Each message size is limited to 64KB.

       If /etc/motd does not exist, then /run/motd is shown. If /run/motd does not exist, then /usr/lib/motd is shown.

       Similar overriding behavior applies to the directories. Files in /etc/motd.d/ override files with the same name in /run/motd.d/ and /usr/lib/motd.d/.
       Files in /run/motd.d/ override files with the same name in /usr/lib/motd.d/.

       Files in the directories listed above are displayed in lexicographic order by name. Moreover, the files are filtered by reading them with the
       credentials of the target user authenticating on the system.

       To silence a message, a symbolic link with target /dev/null may be placed in /etc/motd.d with the same filename as the message to be silenced. Example:
       Creating a symbolic link as follows silences /usr/lib/motd.d/my_motd.

       ln -s /dev/null /etc/motd.d/my_motd

       The MOTD_SHOWN=pam environment variable is set after showing the motd files, even when all of them were silenced using symbolic links.

OPTIONS
       motd=/path/filename
	   The /path/filename file is displayed as message of the day. Multiple paths to try can be specified as a colon-separated list. By default this
	   option is set to /etc/motd:/run/motd:/usr/lib/motd.

       motd_dir=/path/dirname.d
	   The /path/dirname.d directory is scanned and each file contained inside of it is displayed. Multiple directories to scan can be specified as a
	   colon-separated list. By default this option is set to /etc/motd.d:/run/motd.d:/usr/lib/motd.d.

       noupdate
	   Don't run the scripts in /etc/update-motd.d to refresh the motd file.

       When no options are given, the default behavior applies for both options. Specifying either option (or both) will disable the default behavior for both
       options.

MODULE TYPES PROVIDED
       Only the session module type is provided.

RETURN VALUES
       PAM_ABORT
	   Not all relevant data or options could be obtained.

       PAM_BUF_ERR
	   Memory buffer error.

       PAM_IGNORE
	   This is the default return value of this module.

EXAMPLES
       The suggested usage for /etc/pam.d/login is:

	   session  optional  pam_motd.so

       To use a motd file from a different location:

	   session  optional  pam_motd.so motd=/elsewhere/motd

       To use a motd file from elsewhere, along with a corresponding .d directory:

	   session  optional  pam_motd.so motd=/elsewhere/motd motd_dir=/elsewhere/motd.d

SEE ALSO
       motd(5), pam.conf(5), pam.d(5), pam(7), update-motd(5)

AUTHOR
       pam_motd was written by Ben Collins <bcollins@debian.org>.

       The motd_dir= option was added by Allison Karlitskaya <allison.karlitskaya@redhat.com>.

Linux-PAM								  05/07/2023								   PAM_MOTD(8)
