motd(5)								      File Formats Manual							       motd(5)

NAME
       motd - message of the day

DESCRIPTION
       The contents of /etc/motd are displayed by pam_motd(8) after a successful login but just before it executes the login shell.

       The  abbreviation  "motd" stands for "message of the day", and this file has been traditionally used for exactly that (it requires much less disk space
       than mail to all users).

       On Debian GNU/Linux, dynamic content configured at /etc/pam.d/login is also displayed by pam_exec

FILES
       /etc/motd

SEE ALSO
       login(1), issue(5)

Linux man-pages 6.7							  2023-10-31								       motd(5)
