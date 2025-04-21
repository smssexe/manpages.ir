UPDATE-SHELLS(8)						    System Manager's Manual						      UPDATE-SHELLS(8)

NAME
       update-shells - update the list of valid login shells

SYNOPSIS
       update-shells [options]

DESCRIPTION
       update-shells  locates the shells provided by packages from /usr/share/debianutils/shells.d and updates /etc/shells with newly added or removed shells.
       To track changes made by the administrator, it consults a state file in /var/lib/shells.state .

OPTIONS
       --no-act
	      Do not actually perform the changes to /etc/shells .

       --root ROOT

	      Operate on a chroot at ROOT .  Defaults to the value of the environment variable DPKG_ROOT .

       --verbose
	      Print the shells that are being added or removed.

FILES
       /etc/shells /var/lib/shells.state /usr/share/debianutils/shells.d

SEE ALSO
       shells(5)

									  28 Jun 2021							      UPDATE-SHELLS(8)
