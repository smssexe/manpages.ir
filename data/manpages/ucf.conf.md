UCF.CONF(5)							    Debian GNU/Linux manual							   UCF.CONF(5)

NAME
       ucf.conf - site-wide configuration file for ucf

SYNOPSIS
       /etc/ucf.conf

DESCRIPTION
       The  file /etc/ucf.conf is actually a Bourne Shell snippet included during the package build process, and hence you may put any shell directive in that
       file (just make very sure you know what you are doing).

       All the variables have reasonable default values, and some may be overridden on a per run or a per individual basis by using environment variables, and
       all configurable variables can be overridden by options to the scripts themselves.

       The value of a variable can be set so:

       a) Defaults exist in the rules file. These are the values used if no customization is done.

       b) Some variables can be set in the config file /etc/ucf.conf.  These values override the defaults.

       c) Some variables can also be set by setting a corresponding environment variable.  These values override the config file and the defaults.

       d) Using script command line options. All configurable variables may be set by this method, and will override the other methods above.

Configuration File options
       At the moment, the user modifiable variables supported are:

       DEBUG		 Debugging information: The default value is 0 (no debugging information is printed). To enable debugging output, set the value to 1.

       VERBOSE		 Verbosity: The default value is 0 (quiet). To change the default behavior, set the value to 1.

       conf_force_conffold
			 Force the installed file to be retained. The default is to have this variable unset, which makes the script ask  in  case  of	doubt.
			 This can be overridden by the environment variable UCF_FORCE_CONFFOLD

       conf_force_conffnew
			 Force	the  installed file to be overridden. The default is to have this variable unset, which makes the script ask in case of doubt.
			 This can be overridden by the environment variable UCF_FORCE_CONFFNEW

       conf_source_dir	 This is the directory where the historical md5sums for a file are looked for.	Specifically, the historical md5sums are looked for in
			 either the file ${filename}.md5sum, or the subdirectory ${filename}.md5sum.d/

       conf_old_mdsum_file
			 Force the historical md5sums to be read from this file, rather than defaulting to living in the source directory.  Setting  this  op‐
			 tion overrides settings in the environment variable UCF_OLD_MDSUM_FILE

Files
       System-wide defaults are placed in /etc/ucf.conf,

SEE ALSO
       ucf(1),

BUGS
       There are no bugs.  Any resemblance thereof is delirium. Really.

AUTHOR
       This manual page was written by Manoj Srivastava <srivasta@debian.org>, for the Debian GNU/Linux system.

Debian									  Feb 12 2002								   UCF.CONF(5)
