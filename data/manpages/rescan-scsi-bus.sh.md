RESCAN-SCSI-BUS.SH(1)							 User Commands							 RESCAN-SCSI-BUS.SH(1)

NAME
       rescan-scsi-bus.sh - script to add and remove SCSI devices without rebooting

SYNOPSIS
       rescan-scsi-bus.sh  [--alltargets]  [--attachpq3]  [-c]	[---channels=CLIST]  [--color]	[-d]  [--flush]	 [-f] [--forceremove] [--forcerescan] [--help]
       [--hosts=HLIST] [--ids=TLIST] [--ignore-rev] [--issue-lip] [-i] [--issue-lip-wait=SECS] [-I  SECS]  [-l]	 [-L  NUM]  [--largelun]  [--luns=LLIST]  [-m]
       [--multipath] [--nooptscan] [--nosync] [--remove] [--removelun2] [--resize] [--sparselun] [--sync] [--update] [--version] [--wide] [HOST1 [HOST2 ...]]

OPTIONS
       Option are ordered by their long name. Those without a long name are ordered as if their single letter was a long name.

       -a, --alltargets
	      scan all targets, not just currently existing [default: disabled]

       --attachpq3
	      tell kernel to attach sg to LUN 0 that reports PQ=3

       -c     enables scanning of channels 0 1	 [default: 0 / all detected ones]

       --channels=CLIST
	      scan only channel(s) in CLIST

       --color
	      use coloured prefixes OLD/NEW/DEL

       -d     enable debug			 [default: 0]

       -f, --flush
	      flush failed multipath devices	 [default: disabled]

       --forceremove
	      remove stale devices (DANGEROUS)

       --forcerescan
	      remove and readd existing devices (DANGEROUS)

       -h, --help
	      print usage message then exit

       --hosts=HLIST
	      scan only host(s) in HLIST

       --ids=TLIST
	      scan only target ID(s) in TLIST

       --ignore-rev
	      ignore (firmware) revision change. This is the third text field (4 bytes long) in a standard INQUIRY response.

       -i, --issue-lip
	      issue a FibreChannel LIP reset	 [default: disabled]

       -I SECS, --issue-lip-wait=SECS
	      issue a FibreChannel LIP reset and then wait SECS seconds.

       -L NUM activates scanning for LUNs 0--NUM [default: 0]

       -l     activates scanning for LUNs 0--7	 [default: 0]

       --largelun
	      tell kernel to support LUNs > 7 even on SCSI2 devs

       --luns=NLIST
	      scan only lun(s) in NLIST

       -m, --multipath
	      update multipath devices		 [default: disabled]

       --nooptscan
	      don't stop looking for LUNs is 0 is not found

       --nosync
	      do not issue a sync [default: sync if remove]

       -r, --remove
	      enables removing of devices	 [default: disabled]

       --reportlun2
	      tell kernel to try REPORT_LUN even on SCSI2 devices

       -s, --resize
	      look for resized disks and reload associated multipath devices, if applicable

       --sparselun
	      tell kernel to support sparse LUN numbering

       --sync issue a sync [default: sync if remove]

       -u, --update
	      look for existing disks that have been remapped

       -V, --version
	      shows version string then exits. The version string is a numeric datestamp of the form YYYYMMDD.

       -w, --wide
	      scan for target device IDs 0--15	 [default: 0--7]

	      Host numbers may thus be specified either directly on cmd line (deprecated) or with the --hosts=LIST parameter (recommended).

       Arguments to options that end in LIST (e.g. TLIST) can have this form:
	   A[-B][,C[-D]]...
       which is a comma separated list of single values and/or ranges (no spaces allowed).

SEE ALSO
       There is a brief descripion here: http://fibrevillage.com/storage/585-rescan-scsi-bus-sh-script-for-adding-and-removing-scsi-devices-without-rebooting

       sg3_utils Homepage: http://sg.danny.cz/sg

rescan-scsi-bus.sh							   July 2018							 RESCAN-SCSI-BUS.SH(1)
