SMBIOS-TYPE-11(7)							smbios-type-11							     SMBIOS-TYPE-11(7)

NAME
       smbios-type-11 - SMBIOS Type 11 strings

SYNOPSIS
       /sys/firmware/dmi/entries/11-*/raw

DESCRIPTION
       Various OS components process SMBIOS Type 11 vendor strings that a virtual machine manager (VMM) may set and a virtual machine (VM) receives. SMBIOS
       Type 11 vendor strings may play a similar role as kernel-command-line(1) parameters but generally are under control of the VMM rather than the boot
       loader or UKI.

       For details on SMBIOS Type 11 see the System Management BIOS[1] specifications.

STRINGS
       The following strings are supported:

       io.systemd.credential:CREDENTIAL=VALUE, io.systemd.credential.binary:CREDENTIAL=VALUE
	   This allows passing additional system credentials into the system, in textual or binary (Base64) form. See systemd.exec(5) and System and Service
	   Credentials[2] for details.

	   Added in version 252.

       io.systemd.stub.kernel-cmdline-extra=CMDLINE
	   This allows configuration of additional kernel command line options, and is read by the kernel UEFI stub. For details see systemd-stub(1).

	   Added in version 254.

SEE ALSO
       systemd(1), kernel-command-line(7), systemd.system-credentials(7)

NOTES
	1. System Management BIOS
	   https://www.dmtf.org/standards/smbios/

	2. System and Service Credentials
	   https://systemd.io/CREDENTIALS

systemd 255																     SMBIOS-TYPE-11(7)
