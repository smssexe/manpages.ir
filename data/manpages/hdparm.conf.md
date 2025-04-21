hdparm.conf(5)							   hdparm configuration file							hdparm.conf(5)

NAME
       hdparm.conf - Debian configuration file for hdparm

DESCRIPTION
       This  is the default configuration for hdparm for Debian.  It is a rather simple script, so please follow the following guidelines :) Any line that be‐
       gins with a comment is ignored - add as many as you like.

       Since hdparm doesn't use init script anymore, this configuration is mainly used by udev.	 Still one can re-apply settings from the config file by call‐
       ing either

       /usr/lib/pm-utils/power.d/95hdparm-apm resume

       or by calling

       DEVNAME=/dev/<disk> /lib/udev/hdparm

       Note that an in-line comment is not supported.  If a line consists of whitespace only (tabs, spaces, carriage return), it will be ignored, so  you  can
       space control fields as you like.  ANYTHING ELSE IS PARSED!!

       This means that lines with stray characters or lines that use non # comment characters will be interpreted by the initscript.  This has probably minor,
       but potentially serious, side effects for your hard drives, so please follow the guidelines.  Patches to improve flexibilty welcome.

       Note that if the init script causes boot problems, you can pass 'nohdparm' on the kernel command line, and the script will not be run.

       Setting an option outside of one of the stanzas enables it for all drives.

       If an option is listed twice, the second instance replaces the first.

       /sbin/hdparm is not run unless a block of the form:

       DEV {

       option

       option

       }

       exists.	 This blocks will cause /sbin/hdparm OPTIONS DEV to be run.  Where OPTIONS is the concatenation of all options previously defined outside of a
       block and all options defined with in the block.

OPTIONS
       See man 8 hdparm

AUTHOR
       hdparm was written by Mark Lord <mlord@pobox.com>.  The initial manual page was created by Stephen Gran <sgran@debian.org>  for	the  Debian  GNU/Linux
       system (but may be used by others).

Stephen Gran								August 10, 2005								hdparm.conf(5)
