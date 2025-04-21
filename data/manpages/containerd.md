containerd(8)()																       containerd(8)()

       containerd is a high performance container runtime whose daemon can be started by using this command. If none of the config, publish, oci-hook, or help
       commands are specified, the default action of the containerd command is to start the containerd daemon in the foreground.

       A  default  configuration  is  used if no TOML configuration is specified or located at the default file location. The containerd config command can be
       used to generate the default configuration for containerd. The output of that command can be used and modified as necessary as a custom configuration.

NAME
       containerd

SYNOPSIS
       containerd

	      [--address|-a]=[value]
	      [--config|-c]=[value]
	      [--log-level|-l]=[value]
	      [--root]=[value]
	      [--state]=[value]

       Usage:

	      containerd [GLOBAL OPTIONS] command [COMMAND OPTIONS] [ARGUMENTS...]

GLOBAL OPTIONS
       --address, -a="": Address for containerd's GRPC server

       --config, -c="": Path to the configuration file (default: /etc/containerd/config.toml)

       --log-level, -l="": Set the logging level [trace, debug, info, warn, error, fatal, panic]

       --root="": containerd root directory

       --state="": containerd state directory

COMMANDS
config
       Information on the containerd config

   default
       See the output of the default config

   dump
       See the output of the final main config with imported in subconfig files

publish
       Binary to publish events to containerd

       --namespace="": Namespace to publish to

       --topic="": Topic of the event

oci-hook
       Provides a base for OCI runtime hooks to allow arguments to be injected.

																	       containerd(8)()
