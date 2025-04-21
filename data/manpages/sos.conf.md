sos.conf(5)							      File Formats Manual							   sos.conf(5)

NAME
       sos.conf - sos report configuration

DESCRIPTION
       sos report uses a configuration file at /etc/sos/sos.conf, and there are subdirectories under /etc/sos that are used for specific purposes.

       Note that non-root users may override options set in /etc/sos/sos.conf by creating their own sos.conf under $HOME/.config/sos.

       The order in which options are loaded is as follows:

	 1. System configuration file at /etc/sos/sos.conf
	 2. User-specific configuration file at $HOME/.config/sos/sos.conf (for sos
	    components that support non-root)
	 3. In the case of running sos report, presets either automatically loaded
	    due to system configuration, or specified via --preset
	 4. Command line values

       In other words, config files will override defaults, presets override config files, and command line values override presets and config files.

SUBDIRECTORIES
       The following subdirectories exist under /etc/sos and are used as noted below

       extras.d
	      This directory is used to store configuration files used by the sos_extras plugin.

	      The plugin traverses this directory and for each file there it executes commands or collects files optionally with sizelimit.

	      Expected content of an extras file is as follows:
		  - empty lines or those starting with '#' are ignored
		  - add_copy_spec called to lines starting by ':', optionally followed by
		    sizelimit
		  - otherwise, whole line will be executed as a command.
		  Example:
		  command1 --arg1 val1
		  command2
		  :/path/to/file
		  :/path/to/files* sizelimit

		  WARNING: be careful what files to collect or what commands to execute:
		  - avoid calling potentially dangerous or system altering commands, like:
		    - using multiple commands on a line (via pipes, semicolon etc.)
		    - executing commands on background
		    - setting env.variables (as those will be ignored)
		    - altering a system (not only by "rm -rf")
		  - be aware, no secret obfuscation is made

       groups.d
	      This directory is used to store host group configuration files for sos collect.

	      These files can specify any/all of the primary, nodes, and cluster-type options.

	      Users  may  create  their	 own  private host groups in $HOME/.config/sos/groups.d/. If a host group of the same name is saved in both the user's
	      homedir and this directory, the homedir configuration file will have precedence. When run as non-root, sos collect will save host groups to  the
	      user's home dir, and create the necessary directory structure if required.

	      Note  that  non-root  users  may	load host groups defined under /etc/sos/groups.d/, but they may not write new groups or update existing groups
	      saved there.

       presets.d
	      This directory is used to store preset configuration files for sos report.

	      Presets may be used to save standard sets of options. See man sos-report for more information.

PARAMETERS
       There are sections for each sos component, as well as global values and those for plugin options. Options are set using 'ini'-style name = value pairs.
       Disabling/enabling a boolean option is done the same way like on command line (e.g. process.lsof=off).

       Some options accept a comma separated list of values.

       Using options that don't expect a value (like all-logs or no-report) will result in enabling those options, regardless of value set.

       Sections are parsed in the ordering:
       - [global]
       - [component]
       - [plugin_options]

       [global]
	      <option>	    Sets (long) option value. Short options (i.e. z=auto)
			    are not supported.

       [component]
	      Each component will have a separate section, and it will support the options that particular component provides. These are readily  identifiable
	      in the --help output for each component, E.G. sos report --help.

       [plugin_options]
	      Alter available options for defined (and loaded) plugins.

	      Takes the form plugin.option = value, for example rpm.rpmva = true.

EXAMPLES
       To use quiet and batch mode with 10 threads:

       [global]
       batch=yes
       build=true
       threads=10

       To disable the 'host' and 'filesys' plugins:

       [report]
       skip-plugins = host,filesys

       To disable rpm package verification in the RPM plugin:

       [plugin_options]
       rpm.rpmva = off

FILES
       /etc/sos/sos.conf
       $HOME/.config/sos/sos.conf (optional)

SEE ALSO
       sos-report(1) sos-collect(1) sos-clean(1)

sos configuration file							      SOS								   sos.conf(5)
