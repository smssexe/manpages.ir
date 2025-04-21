FAILLOCK(8)							       Linux-PAM Manual								   FAILLOCK(8)

NAME
       faillock - Tool for displaying and modifying the authentication failure record files

SYNOPSIS

       faillock [--dir /path/to/tally-directory] [--user username] [--reset]

DESCRIPTION
       The pam_faillock.so module maintains a list of failed authentication attempts per user during a specified interval and locks the account in case there
       were more than deny consecutive failed authentications. It stores the failure records into per-user files in the tally directory.

       The faillock command is an application which can be used to examine and modify the contents of the tally files. It can display the recent failed
       authentication attempts of the username or clear the tally files of all or individual usernames.

OPTIONS
       --conf /path/to/config-file
	   The file where the configuration is located. The default is /etc/security/faillock.conf.

       --dir /path/to/tally-directory
	   The directory where the user files with the failure records are kept.

	   The priority to set this option is to use the value provided from the command line. If this isn't provided, then the value from the configuration
	   file is used. Finally, if neither of them has been provided, then /var/run/faillock is used.

       --user username
	   The user whose failure records should be displayed or cleared.

       --reset
	   Instead of displaying the user's failure records, clear them.

FILES
       /var/run/faillock/*
	   the files logging the authentication failures for users

SEE ALSO
       pam_faillock(8), pam(8)

AUTHOR
       faillock was written by Tomas Mraz.

Linux-PAM								  05/07/2023								   FAILLOCK(8)
