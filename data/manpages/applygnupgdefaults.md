APPLYGNUPGDEFAULTS(8)						     GNU Privacy Guard 2.4						 APPLYGNUPGDEFAULTS(8)

NAME
       applygnupgdefaults - Run gpgconf --apply-defaults for all users.

SYNOPSIS
       applygnupgdefaults

DESCRIPTION
       This is a legacy script.	 Modern application should use the per component global configuration files under ‘/etc/gnupg/’.

       This  script  is a wrapper around gpgconf to run it with the command --apply-defaults for all real users with an existing GnuPG home directory.	Admins
       might want to use this script to update he GnuPG configuration files for all users after ‘/etc/gnupg/gpgconf.conf’ has been changed.  This  allows  en‐
       forcing	certain	 policies for all users.  Note, that this is not a bulletproof way to force a user to use certain options.  A user may always directly
       edit the configuration files and bypass gpgconf.

       applygnupgdefaults is invoked by root as:

	 applygnupgdefaults

GnuPG 2.4.4								  2024-01-25							 APPLYGNUPGDEFAULTS(8)
