DEVLINK-LC(8)								     Linux								 DEVLINK-LC(8)

NAME
       devlink-lc - devlink line card configuration

SYNOPSIS
       devlink [ OPTIONS ] lc  { COMMAND | help }

       OPTIONS := { -V[ersion] }

       devlink lc set DEV lc LC_INDEX [ type { LC_TYPE | notype } ]

       devlink lc show [ DEV [ lc LC_INDEX ] ]

       devlink lc help

DESCRIPTION
   devlink lc set - change line card attributes
       DEV    Specifies the devlink device to operate on.

		  Format is:
		    BUS_NAME/BUS_ADDRESS

       lc LC_INDEX
	      Specifies index of a line card slot to set.

       type { LC_TYPE  | notype } Type of line card to provision. Each driver provides a list of supported line card types which is shown in the output of de‐
	      vlink lc show command.

   devlink lc show - display line card attributes
       DEV    Specifies the devlink device to operate on. If this and lc arguments are omitted all line cards of all devices are listed.

       lc LC_INDEX
	      Specifies index of a line card slot to show.

EXAMPLES
       devlink lc show
	   Shows the state of all line cards on the system.

       devlink lc show pci/0000:01:00.0 lc 1
	   Shows the state of line card with index 1.

       devlink lc set pci/0000:01:00.0 lc 1 type 16x100G
	   Sets type of specified line card to type 16x100G.

       devlink lc set pci/0000:01:00.0 lc 1 notype
	   Clears provisioning on a line card.

SEE ALSO
       devlink(8), devlink-dev(8), devlink-port(8), devlink-monitor(8),

AUTHOR
       Jiri Pirko <jiri@nvidia.com>

iproute2								  20 Apr 2022								 DEVLINK-LC(8)
