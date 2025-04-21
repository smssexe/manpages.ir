PAM_ISSUE(8)							       Linux-PAM Manual								  PAM_ISSUE(8)

NAME
       pam_issue - PAM module to add issue file to user prompt

SYNOPSIS

       pam_issue.so [noesc] [issue=issue-file-name]

DESCRIPTION
       pam_issue is a PAM module to prepend an issue file to the username prompt. It also by default parses escape codes in the issue file similar to some
       common getty's (using \x format).

       Recognized escapes:

       \d
	   current day

       \l
	   name of this tty

       \m
	   machine architecture (uname -m)

       \n
	   machine's network node hostname (uname -n)

       \o
	   domain name of this system

       \r
	   release number of operating system (uname -r)

       \t
	   current time

       \s
	   operating system name (uname -s)

       \u
	   number of users currently logged in

       \U
	   same as \u except it is suffixed with "user" or "users" (eg. "1 user" or "10 users")

       \v
	   operating system version and build date (uname -v)

OPTIONS
       noesc
	   Turns off escape code parsing.

       issue=issue-file-name
	   The file to output if not using the default.

MODULE TYPES PROVIDED
       Only the auth module type is provided.

RETURN VALUES
       PAM_BUF_ERR
	   Memory buffer error.

       PAM_IGNORE
	   The prompt was already changed.

       PAM_SERVICE_ERR
	   A service module error occurred.

       PAM_SUCCESS
	   The new prompt was set successfully.

EXAMPLES
       Add the following line to /etc/pam.d/login to set the user specific issue at login:

		   auth optional pam_issue.so issue=/etc/issue

SEE ALSO
       pam.conf(5), pam.d(5), pam(7)

AUTHOR
       pam_issue was written by Ben Collins <bcollins@debian.org>.

Linux-PAM								  05/07/2023								  PAM_ISSUE(8)
