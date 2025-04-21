SYSTEMD-LOGIND.SERVICE(8)					    systemd-logind.service					     SYSTEMD-LOGIND.SERVICE(8)

NAME
       systemd-logind.service, systemd-logind - Login manager

SYNOPSIS
       systemd-logind.service

       /usr/lib/systemd/systemd-logind

DESCRIPTION
       systemd-logind is a system service that manages user logins. It is responsible for:

       •   Keeping track of users and sessions, their processes and their idle state. This is implemented by allocating a systemd slice unit for each user
	   below user.slice, and a scope unit below it for each concurrent session of a user. Also, a per-user service manager is started as system service
	   instance of user@.service for each logged in user.

       •   Generating and managing session IDs. If auditing is available and an audit session ID is already set for a session, then this ID is reused as the
	   session ID. Otherwise, an independent session counter is used.

       •   Providing polkit[1]-based access for users for operations such as system shutdown or sleep

       •   Implementing a shutdown/sleep inhibition logic for applications

       •   Handling of power/sleep hardware keys

       •   Multi-seat management

       •   Session switch management

       •   Device access management for users

       •   Automatic spawning of text logins (gettys) on virtual console activation and user runtime directory management

       •   Scheduled shutdown

       •   Sending "wall" messages

       User sessions are registered with logind via the pam_systemd(8) PAM module.

       See logind.conf(5) for information about the configuration of this service.

       See sd-login(3) for information about the basic concepts of logind such as users, sessions and seats.

       See org.freedesktop.login1(5) and org.freedesktop.LogControl1(5) for information about the D-Bus APIs systemd-logind provides.

       For more information on the inhibition logic see the Inhibitor Lock Developer Documentation[2].

       If you are interested in writing a display manager that makes use of logind, please have look at Writing Display Managers[3]. If you are interested in
       writing a desktop environment that makes use of logind, please have look at Writing Desktop Environments[4].

SEE ALSO
       systemd(1), systemd-user-sessions.service(8), loginctl(1), logind.conf(5), pam_systemd(8), sd-login(3)

NOTES
	1. polkit
	   https://www.freedesktop.org/wiki/Software/polkit

	2. Inhibitor Lock Developer Documentation
	   https://www.freedesktop.org/wiki/Software/systemd/inhibit

	3. Writing Display Managers
	   https://www.freedesktop.org/wiki/Software/systemd/writing-display-managers

	4. Writing Desktop Environments
	   https://www.freedesktop.org/wiki/Software/systemd/writing-desktop-environments

systemd 255															     SYSTEMD-LOGIND.SERVICE(8)
