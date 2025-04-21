MV(1)									 User Commands									 MV(1)

NAME
       mv - move (rename) files

SYNOPSIS
       mv [OPTION]... [-T] SOURCE DEST
       mv [OPTION]... SOURCE... DIRECTORY
       mv [OPTION]... -t DIRECTORY SOURCE...

DESCRIPTION
       Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.

       Mandatory arguments to long options are mandatory for short options too.

       --backup[=CONTROL]
	      make a backup of each existing destination file

       -b     like --backup but does not accept an argument

       --debug
	      explain how a file is copied.  Implies -v

       -f, --force
	      do not prompt before overwriting

       -i, --interactive
	      prompt before overwrite

       -n, --no-clobber
	      do not overwrite an existing file

       If you specify more than one of -i, -f, -n, only the final one takes effect.

       --no-copy
	      do not copy if renaming fails

       --strip-trailing-slashes
	      remove any trailing slashes from each SOURCE argument

       -S, --suffix=SUFFIX
	      override the usual backup suffix

       -t, --target-directory=DIRECTORY
	      move all SOURCE arguments into DIRECTORY

       -T, --no-target-directory
	      treat DEST as a normal file

       --update[=UPDATE]
	      control which existing files are updated; UPDATE={all,none,older(default)}.  See below

       -u     equivalent to --update[=older]

       -v, --verbose
	      explain what is being done

       -Z, --context
	      set SELinux security context of destination file to default type

       --help display this help and exit

       --version
	      output version information and exit

       UPDATE controls which existing files in the destination are replaced.  'all' is the default operation when an --update option is not specified, and re‐
       sults  in  all existing files in the destination being replaced.	 'none' is similar to the --no-clobber option, in that no files in the destination are
       replaced, but also skipped files do not induce a failure.  'older' is the default operation when --update is specified, and results in files being  re‐
       placed if they're older than the corresponding source file.

       The  backup  suffix  is	'~',  unless set with --suffix or SIMPLE_BACKUP_SUFFIX.	 The version control method may be selected via the --backup option or
       through the VERSION_CONTROL environment variable.  Here are the values:

       none, off
	      never make backups (even if --backup is given)

       numbered, t
	      make numbered backups

       existing, nil
	      numbered if numbered backups exist, simple otherwise

       simple, never
	      always make simple backups

AUTHOR
       Written by Mike Parker, David MacKenzie, and Jim Meyering.

REPORTING BUGS
       GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
       Report any translation bugs to <https://translationproject.org/team/>

COPYRIGHT
       Copyright © 2023 Free Software Foundation, Inc.	License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
       This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       rename(2)

       Full documentation <https://www.gnu.org/software/coreutils/mv>
       or available locally via: info '(coreutils) mv invocation'

GNU coreutils 9.4							  April 2024									 MV(1)
