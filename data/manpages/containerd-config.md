containerd-config(8)						    System Manager's Manual						  containerd-config(8)

NAME
       containerd-config - information on the containerd config

SYNOPSIS
       containerd config [command]

DESCRIPTION
       The  containerd	config command has one subcommand, named default, which will display on standard output the default containerd config for this version
       of the containerd daemon.

       This output can be piped to a containerd-config.toml(5) file and placed in /etc/containerd to be used as the configuration  for	containerd  on	daemon
       startup. The configuration can be placed in any filesystem location and used with the --config option to the containerd daemon as well.

       See containerd-config.toml(5) for more information on the containerd configuration options.

OPTIONS
       default
	      This subcommand will output the TOML formatted containerd configuration to standard output

BUGS
       Please file any specific issues that you encounter at https://github.com/containerd/containerd.

AUTHOR
       Phil Estes estesp@gmail.com ⟨mailto:estesp@gmail.com⟩

SEE ALSO
       ctr(8), containerd(8), containerd-config.toml(5)

									  01/30/2018							  containerd-config(8)
