overlayroot-chroot(8)						  initramfs-tools-overlayroot						 overlayroot-chroot(8)

NAME
       overlayroot-chroot - chroot into the lower filesystem in a writable mode

SYNOPSIS
       overlayroot-chroot [COMMAND [ARG]...]

DESCRIPTION
       overlayroot-chroot  is  a program that sets up bind mounts for /proc, /run, and /sys, remounts the lower directory in an overlayfs with write capabili‐
       ties and will chroot(8) into it.	 Upon exit, the bind mounts are unmounted.

       Any [COMMAND [ARG]...] are passed directly through to chroot(8).

SEE ALSO
       chroot(8)

AUTHOR
       This manpage and the utility were written by Dustin Kirkland <kirkland@ubuntu.com> for Ubuntu systems (but may  be  used	 by  others).	Permission  is
       granted	to  copy, distribute and/or modify this document and the utility under the terms of the GNU General Public License, Version 3 published by the
       Free Software Foundation.

       The complete text of the GNU General Public License can be found	 in  /usr/share/common-licenses/GPL  on	 Debian/Ubuntu	systems,  or  on  the  web  at
       http://www.gnu.org/licenses/gpl.txt.

overlayroot-chroot							 20 July 2012							 overlayroot-chroot(8)
