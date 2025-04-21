USER-DIRS.DEFAULT(5)							 File Formats							  USER-DIRS.DEFAULT(5)

NAME
       user-dirs.defaults - default settings for XDG user dirs

DESCRIPTION
       The /etc/xdg/user-dirs.defaults file is a text file that contains the default values for the XDG user dirs which are used by the xdg-user-dirs-update
       command.

       This file contains lines of the form

	   NAME=VALUE

       The following names are recognised:
	   DESKTOP
	   DOWNLOAD
	   TEMPLATES
	   PUBLICSHARE
	   DOCUMENTS
	   MUSIC
	   PICTURES
	   VIDEOS

       The values are relative pathnames from the home directory and will be translated on a per-path-element basis into the users locale.

       Lines beginning with a # character are ignored.

ENVIRONMENT
       XDG_CONFIG_DIRS
	   The user-dirs.defaults file is located in this directory. The default is /etc/xdg.

SEE ALSO
       xdg-user-dirs-update(1)

XDG																	  USER-DIRS.DEFAULT(5)
