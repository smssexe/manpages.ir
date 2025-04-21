POLKITD(8)								    polkitd								    POLKITD(8)

NAME
       polkitd - The polkit system daemon

SYNOPSIS

       polkitd

DESCRIPTION
       polkitd provides the org.freedesktop.PolicyKit1 D-Bus service on the system message bus. Users or administrators should never need to start this daemon
       as it will be automatically started by dbus-daemon(1) or systemd(1) whenever an application calls into the service.

       polkitd must be started with superuser privileges but drops privileges early by switching to the unprivileged polkitd system user.

       See the polkit(8) man page for more information.

AUTHOR
       Written by David Zeuthen <davidz@redhat.com> with a lot of help from many others.

BUGS
       Please send bug reports to either the distribution or the polkit-devel mailing list, see the link
       https://gitlab.freedesktop.org/polkit/polkit/-/issues/ on how to subscribe.

SEE ALSO
       polkit(8), pkaction(1), pkcheck(1), pkexec(1), pkttyagent(1), dbus-daemon(1), systemd(1)

polkit									   May 2009								    POLKITD(8)
