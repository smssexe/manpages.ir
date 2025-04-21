DELUSER.CONF(5)							      File Formats Manual						       DELUSER.CONF(5)

NAME
       /etc/deluser.conf - configuration file for deluser(8) and delgroup(8).

DESCRIPTION
       The  file  /etc/deluser.conf  contains  defaults for the programs deluser(8) and delgroup(8).  Each line holds a single value pair in the form option =
       value.  Double or single quotes are allowed around the value, as is whitespace around the equals sign.  Comment lines must have a hash sign (#) in  the
       first column.

       deluser(8) and delgroup(8) also read /etc/adduser.conf, see adduser.conf(5); settings in deluser.conf may overwrite settings made in adduser.conf.

       The valid configuration options are:

       BACKUP If  REMOVE_HOME  or REMOVE_ALL_FILES is activated, all files are backed up before they are removed.  The backup file that is created defaults to
	      username.tar(.gz|.bz2) in the directory specified by the BACKUP_TO option.  The compression method is chosen to  the  best  that	is  available.
	      Values may be 0 or 1. Defaults to 0.

       BACKUP_SUFFIX
	      Select compression algorithm for a home directory backup.	 Can be set to any suffix recognized by tar --auto-compress.  Defaults to .gz.

       BACKUP_TO
	      If BACKUP is activated, BACKUP_TO specifies the directory the backup is written to.  Defaults to the current directory.

       EXCLUDE_FSTYPES
	      A	 regular  expression which describes all filesystem types which should be excluded when looking for files of a user to be deleted. Defaults to
	      "(proc|sysfs|usbfs|devtmpfs|devpts|afs)".

       NO_DEL_PATHS
	      A list of regular expressions, space separated.  All files to be deleted in course of deleting the home directory or user-owned files  elsewhere
	      are  checked against each of these regular expressions.  If a match is detected, the file is not deleted.	 Defaults to a list of system directo‐
	      ries, leaving only /home.	 Therefore only files below /home belonging to that specific user are going to be deleted.

       ONLY_IF_EMPTY
	      Only delete a group if there are no users belonging to this group.  Defaults to 0.

       REMOVE_ALL_FILES
	      Removes all files on the system owned by the user to be removed.	If this option is activated REMOVE_HOME has no effect.	Values may be 0 or  1.
	      Defaults to 0.

       REMOVE_HOME
	      Removes the home directory and mail spool of the user to be removed.  Value may be 0 (don't delete) or 1 (do delete). Defaults to 0.

FILES
       /etc/deluser.conf

SEE ALSO
       adduser.conf(5), delgroup(8), deluser(8)

Debian GNU/Linux															       DELUSER.CONF(5)
