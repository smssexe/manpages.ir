SYSTEMD-ASK-PASSWORD-CONSOLE.SERVICE(8)			     systemd-ask-password-console.service		       SYSTEMD-ASK-PASSWORD-CONSOLE.SERVICE(8)

NAME
       systemd-ask-password-console.service, systemd-ask-password-console.path, systemd-ask-password-wall.service, systemd-ask-password-wall.path - Query the
       user for system passwords on the console and via wall

SYNOPSIS
       systemd-ask-password-console.service

       systemd-ask-password-console.path

       systemd-ask-password-wall.service

       systemd-ask-password-wall.path

DESCRIPTION
       systemd-ask-password-console.service is a system service that queries the user for system passwords (such as hard disk encryption keys and SSL
       certificate passphrases) on the console. It is intended to be used during boot to ensure proper handling of passwords necessary for boot.
       systemd-ask-password-wall.service is a system service that informs all logged in users for system passwords via wall(1). It is intended to be used
       after boot to ensure that users are properly notified.

       See the developer documentation[1] for more information about the system password logic.

       Note that these services invoke systemd-tty-ask-password-agent(1) with either the --watch --console or --watch --wall command line parameters.

SEE ALSO
       systemd(1), systemd-tty-ask-password-agent(1), wall(1)

NOTES
	1. developer documentation
	   https://systemd.io/PASSWORD_AGENTS/

systemd 255													       SYSTEMD-ASK-PASSWORD-CONSOLE.SERVICE(8)
