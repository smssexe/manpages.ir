LVM.CONF(5)							      File Formats Manual							   LVM.CONF(5)

NAME
       lvm.conf — Configuration file for LVM2

SYNOPSIS
       /etc/lvm/lvm.conf

DESCRIPTION
       lvm.conf is loaded during the initialisation phase of lvm(8).  This file can in turn lead to other files being loaded - settings read in later override
       earlier settings.  File timestamps are checked between commands and if any have changed, all the files are reloaded.

       For a description of each lvm.conf(5) setting, run:

       lvmconfig --typeconfig default --withcomments --withspaces

       The settings defined in lvm.conf can be overridden by any of these extended configuration methods:

       direct config override on command line
	      The --config ConfigurationString command line option takes the ConfigurationString as direct string representation of the configuration to over‐
	      ride the existing configuration. The ConfigurationString is of exactly the same format as used in any LVM configuration file.

       profile config
	      A	 profile  is a set of selected customizable configuration settings that are aimed to achieve a certain characteristics in various environments
	      or uses. It's used to override existing configuration.  Normally, the name of the profile should reflect that environment or use.

       There are two groups of profiles recognised: command profiles and metadata profiles.

       The command profile is used to override selected configuration settings at global LVM command level - it is applied at the very beginning of  LVM  com‐
       mand execution and it is used throughout the whole time of LVM command execution. The command profile is applied by using the --commandprofile Profile‐
       Name command line option that is recognised by all LVM2 commands.

       The  metadata  profile  is used to override selected configuration settings at Volume Group/Logical Volume level - it is applied independently for each
       Volume Group/Logical Volume that is being processed. As such, each Volume Group/Logical Volume can store the profile name used in its metadata so  next
       time  the Volume Group/Logical Volume is processed, the profile is applied automatically. If Volume Group and any of its Logical Volumes have different
       profiles defined, the profile defined for the Logical Volume is preferred. The metadata profile can be attached/detached	 by  using  the	 lvchange  and
       vgchange commands and their --metadataprofile ProfileName and --detachprofile options or the --metadataprofile option during creation when using vgcre‐
       ate  or	lvcreate command.  The vgs and lvs reporting commands provide -o vg_profile and -o lv_profile output options to show the metadata profile cur‐
       rently attached to a Volume Group or a Logical Volume.

       The set of options allowed for command profiles is mutually exclusive when compared to the set of options allowed for metadata profiles.	 The  settings
       that belong to either of these two sets can't be mixed together and LVM tools will reject such profiles.

       LVM  itself  provides  a few predefined configuration profiles.	Users are allowed to add more profiles with different values if needed.	 For this pur‐
       pose, there's the command_profile_template.profile (for command profiles) and metadata_profile_template.profile (for metadata profiles)	which  contain
       all  settings that are customizable by profiles of certain type. Users are encouraged to copy these template profiles and edit them as needed. Alterna‐
       tively, the lvmconfig --file <ProfileName.profile> --type profilable-command <section> or lvmconfig  --file  <ProfileName.profile>  --type  profilable-
       metadata <section> can be used to generate a configuration with profilable settings in either of the type for given section and save it to new Profile‐
       Name.profile (if the section is not specified, all profilable settings are reported).

       The  profiles are stored in /etc/lvm/profile directory by default.  This location can be changed by using the config/profile_dir setting.  Each profile
       configuration is stored in ProfileName.profile file in the profile directory. When referencing the profile, the .profile suffix is left out.

       tag config
	      See tags configuration setting description below.

       When several configuration methods are used at the same time and when LVM looks for the value of a particular setting, it traverses this config cascade
       from left to right:

       direct config override on command line → command profile config → metadata profile config → tag config → lvmlocal.conf → lvm.conf

       No part of this cascade is compulsory. If there's no setting value found at the end of the cascade, a default value is used for that setting.  Use lvm‐
       config to check what settings are in use and what the default values are.

SYNTAX
       This section describes the configuration file syntax.

       Whitespace is not significant unless it is within quotes.  This provides a wide choice of acceptable indentation styles.	 Comments  begin  with	#  and
       continue to the end of the line.	 They are treated as whitespace.

       Here is an informal grammar:

       file = value*
	      A configuration file consists of a set of values.

       value = section | assignment
	      A value can either be a new section, or an assignment.

       section = identifier '{' value* '}'
	      A	 section  groups associated values together. If the same section is encountered multiple times, the contents of all instances are concatenated
	      together in the order of appearance.
	      It is denoted by a name and delimited by curly brackets.
	      e.g. backup {
			...
		   }

       assignment = identifier '=' ( array | type )
	      An assignment associates a type with an identifier. If the identifier contains forward slashes, those are interpreted as	path  delimiters.  The
	      statement	 section/key  =	 value	is equivalent to section { key = value }. If multiple instances of the same key are encountered, only the last
	      value is used (and a warning is issued).
	      e.g. level = 7

       array =	'[' ( type ',')* type ']' | '[' ']'
	      Inhomogeneous arrays are supported.
	      Elements must be separated by commas.
	      An empty array is acceptable.

       type = integer|float|string
	      integer = [0-9]*
	      float = [0-9]*'.'[0-9]*
	      string = '"' .* '"'

	      Strings with spaces must be enclosed in double quotes, single words that start with a letter can be left unquoted.

SETTINGS
       The lvmconfig command prints the LVM configuration settings in various ways.  See the man page lvmconfig(8).

       Command to print a list of all possible config settings, with their default values:
       lvmconfig --type default

       Command to print a list of all possible config settings, with their default values, and a full description of each as a comment:
       lvmconfig --type default --withcomments

       Command to print a list of all possible config settings, with their current values (configured, non-default values are shown):
       lvmconfig --type current

       Command to print all config settings that have been configured with a different value than the default (configured, non-default values are shown):
       lvmconfig --type diff

       Command to print a single config setting, with its default value, and a full description, where "Section" refers to the config  section,	 e.g.  global,
       and "Setting" refers to the name of the specific setting, e.g. umask:
       lvmconfig --type default --withcomments Section/Setting

FILES
       /etc/lvm/lvm.conf
       /etc/lvm/lvmlocal.conf
       /etc/lvm/archive
       /etc/lvm/backup
       /etc/lvm/cache/.cache
       /etc/lvm/profile
       /run/lock/lvm

SEE ALSO
       lvm(8), lvmconfig(8)

Red Hat, Inc.						       LVM TOOLS 2.03.16(2) (2022-05-18)						   LVM.CONF(5)
