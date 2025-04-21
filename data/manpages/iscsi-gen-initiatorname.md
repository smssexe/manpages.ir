ISCSI_GEN_INITIATORNAME(8)					 Linux Administrator's Manual					    ISCSI_GEN_INITIATORNAME(8)

NAME
       iscsi-gen-initiatorname - smart iSCSI initiator name generation tool

SYNOPSIS
       iscsi-gen-initiatorname [OPTIONS]

DESCRIPTION
       iscsi-gen-initiatorname	generates  an  iSCSI  Initiator Name in the initiatorname.iscsi file. It is an error to try to overwrite an existing Initiator
       Name, unless the -f (force) option is supplied.

       The Initiator Name will be taken from the kernel command line, if present (from the rd.initiatorname parameter),	 else  from  the  iBFT	subsystem  (if
       present in sysfs), else it will be generated using the iscsi-iname command.

       It is an error if both the kernel command-line Initiator Name and the iBFT Initiator Name are both set, and they are different.	it is also an error to
       try to write over an Initiator Name file if it read-only, or to create one if its directory is not writable.

       You must be root to run this command.

OPTIONS
       [-h]   Display a help message and exit.

       [-f]   Force overwrite of existing initiator name, if present.

       [-p]IQN-PREFIX
	      Use IQN-PREFIX as the prefix to the IQN generated, instead of the default of iqn.1996-04.de.suse:01.

FILES
       /etc/iscsi/initiatorname.iscsi
	      The file containing the initiator name. Do not edit manually.

SEE ALSO
       iscsi-iname(8)

AUTHORS
       Open-iSCSI project <http://www.open-iscsi.com/>
       Hannes Reinecke <hare@suse.de>
       Lee Duncan <lduncan@suse.com>

									   APR 2022						    ISCSI_GEN_INITIATORNAME(8)
