USER-DIRS.DIRS(5)							 File Formats							     USER-DIRS.DIRS(5)

NAME
       user-dirs.dirs - settings for XDG user dirs

DESCRIPTION
       The $HOME/.config/user-dirs.dirs file is a text file that contains the user-specific values for the XDG user dirs. It is created and updated by the
       xdg-user-dirs-update command.

       This file contains lines of the form

	   XDG_NAME_DIR=VALUE

       The following names are recognised:
	   DESKTOP
	   DOWNLOAD
	   TEMPLATES
	   PUBLICSHARE
	   DOCUMENTS
	   MUSIC
	   PICTURES
	   VIDEOS

       VALUE must be of the form "$HOME/Path" or "/Path".

       Lines beginning with a # character are ignored.

       The format of user-dirs.dirs is designed to allow direct sourcing of this file in shell scripts.

ENVIRONMENT
       XDG_CONFIG_DIRS
	   The user-dirs.defaults file is located in this directory. The default is /etc/xdg.

SEE ALSO
       xdg-user-dirs-update(1)

XDG																	     USER-DIRS.DIRS(5)
