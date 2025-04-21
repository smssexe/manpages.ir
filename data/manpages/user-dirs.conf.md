USER-DIRS.CONF(5)							 File Formats							     USER-DIRS.CONF(5)

NAME
       user-dirs.conf - configuration for xdg-user-dirs-update

DESCRIPTION
       The /etc/xdg/user-dirs.conf file is a text file that controls the behavior of the xdg-user-dirs-update command. Users can have their own
       ~/.config/user-dirs.conf file, which overrides the system-wide configuration.

       The following keys are recognised:

       enabled=boolean
	   When set to False, xdg-user-dirs-update will not change the XDG user dirs configuration.

       filename_encoding=encoding
	   This sets the filename encoding to use.  encoding can be an explicit encoding name, such as UTF-8, or "locale", which means the encoding of the
	   users locale will be used.

       Lines beginning with a # character are ignored.

ENVIRONMENT
       XDG_CONFIG_DIRS
	   The system-wide user-dirs.conf file is located in this directory. The default is /etc/xdg.

       XDG_CONFIG_HOME
	   The per-user user-dirs.conf file is located in this directory. The default is $HOME/.config.

SEE ALSO
       xdg-user-dirs-update(1)

XDG																	     USER-DIRS.CONF(5)
