SYSTEMD-GPT-AUTO-GENERATOR(8)					  systemd-gpt-auto-generator					 SYSTEMD-GPT-AUTO-GENERATOR(8)

NAME
       systemd-gpt-auto-generator - Generator for automatically discovering and mounting root, /home/, /srv/, /var/ and /var/tmp/ partitions, as well as
       discovering and enabling swap partitions, based on GPT partition type GUIDs

SYNOPSIS
       /usr/lib/systemd/system-generators/systemd-gpt-auto-generator

DESCRIPTION
       systemd-gpt-auto-generator is a unit generator that automatically discovers the root partition, /home/, /srv/, /var/, /var/tmp/, the EFI System
       Partition, the Extended Boot Loader Partition, and swap partitions and creates mount and swap units for them, based on the partition type GUIDs of GUID
       partition tables (GPT). See UEFI Specification[1], chapter 5 for more details. It implements the Discoverable Partitions Specification[2].

       Note that this generator has no effect on non-GPT systems. It will also not create mount point configuration for directories which already contain
       files or if the mount point is explicitly configured in fstab(5). If the units this generator creates are overridden, for example by units in
       directories with higher precedence, drop-ins and additional dependencies created by this generator might still be used.

       This generator will only look for the root partition on the same physical disk where the EFI System Partition (ESP) is located. Note that support from
       the boot loader is required: the EFI variable LoaderDevicePartUUID of the 4a67b082-0a4c-41cf-b6c7-440b29bb8c4f vendor UUID is used to determine from
       which partition, and hence the disk, from which the system was booted. If the boot loader does not set this variable, this generator will not be able
       to detect the root partition. See the Boot Loader Interface[3] for details.

       Similarly, this generator will only look for the other partitions on the same physical disk as the root partition. In this case, boot loader support is
       not required. These partitions will not be searched for on systems where the root file system is distributed on multiple disks, for example via btrfs
       RAID.

       systemd-gpt-auto-generator is useful for centralizing file system configuration in the partition table and making configuration in /etc/fstab or on the
       kernel command line unnecessary.

       This generator looks for the partitions based on their partition type GUID. The following partition type GUIDs are identified:

       Table 1. Partition Type GUIDs
       ┌──────────────────────────────────────┬────────────────────────────────┬─────────────────┬──────────────────────────────────┐
       │ Partition Type GUID		      │ Name			       │ Mount Point	 │ Explanation			    │
       ├──────────────────────────────────────┼────────────────────────────────┼─────────────────┼──────────────────────────────────┤
       │ SD_GPT_ROOT_X86_64		      │ Root Partition (x86-64)	       │ /		 │ The first partition with this    │
       │ 4f68bce3-e8cd-4db1-96e7-fbcaf984b709 │				       │		 │ type UUID, located on the same   │
       │				      │				       │		 │ disk as the ESP, is used as the  │
       │				      │				       │		 │ root file system / on AMD64 /    │
       │				      │				       │		 │ 64-bit x86 systems.		    │
       ├──────────────────────────────────────┼────────────────────────────────┼─────────────────┼──────────────────────────────────┤
       │ SD_GPT_ROOT_ARM64		      │ Root Partition (64-bit ARM)    │ /		 │ The first partition with this    │
       │ b921b045-1df0-41c3-af44-4c6f280d3fae │				       │		 │ type UUID, located on the same   │
       │				      │				       │		 │ disk as the ESP, is used as the  │
       │				      │				       │		 │ root file system / on AArch64 /  │
       │				      │				       │		 │ 64-bit ARM systems.		    │
       ├──────────────────────────────────────┼────────────────────────────────┼─────────────────┼──────────────────────────────────┤
       │ SD_GPT_ROOT_ALPHA SD_GPT_ROOT_ARC    │ root partitions for other      │ /		 │ The first partition with the	    │
       │ SD_GPT_ROOT_ARM SD_GPT_ROOT_ARM64    │ architectures		       │		 │ type UUID matching the	    │
       │ SD_GPT_ROOT_IA64		      │				       │		 │ architecture, located on the	    │
       │ SD_GPT_ROOT_LOONGARCH64	      │				       │		 │ same disk as the ESP, is used as │
       │ SD_GPT_ROOT_MIPS SD_GPT_ROOT_MIPS64  │				       │		 │ the root file system /. For the  │
       │ SD_GPT_ROOT_MIPS_LE		      │				       │		 │ full list and constant values,   │
       │ SD_GPT_ROOT_MIPS64_LE		      │				       │		 │ see Discoverable Partitions	    │
       │ SD_GPT_ROOT_PARISC SD_GPT_ROOT_PPC   │				       │		 │ Specification[2].		    │
       │ SD_GPT_ROOT_PPC64		      │				       │		 │				    │
       │ SD_GPT_ROOT_PPC64_LE		      │				       │		 │				    │
       │ SD_GPT_ROOT_RISCV32		      │				       │		 │				    │
       │ SD_GPT_ROOT_RISCV64 SD_GPT_ROOT_S390 │				       │		 │				    │
       │ SD_GPT_ROOT_S390X SD_GPT_ROOT_TILEGX │				       │		 │				    │
       │ SD_GPT_ROOT_X86 SD_GPT_ROOT_X86_64   │				       │		 │				    │
       │ SD_GPT_USR_ALPHA SD_GPT_USR_ARC      │				       │		 │				    │
       │ SD_GPT_USR_ARM SD_GPT_USR_IA64	      │				       │		 │				    │
       │ SD_GPT_USR_LOONGARCH64		      │				       │		 │				    │
       │ SD_GPT_USR_MIPS_LE		      │				       │		 │				    │
       │ SD_GPT_USR_MIPS64_LE		      │				       │		 │				    │
       │ SD_GPT_USR_PARISC SD_GPT_USR_PPC     │				       │		 │				    │
       │ SD_GPT_USR_PPC64 SD_GPT_USR_PPC64_LE │				       │		 │				    │
       │ SD_GPT_USR_RISCV32		      │				       │		 │				    │
       │ SD_GPT_USR_RISCV64 SD_GPT_USR_S390   │				       │		 │				    │
       │ SD_GPT_USR_S390X SD_GPT_USR_TILEGX   │				       │		 │				    │
       │ SD_GPT_USR_X86			      │				       │		 │				    │
       ├──────────────────────────────────────┼────────────────────────────────┼─────────────────┼──────────────────────────────────┤
       │ SD_GPT_HOME			      │ Home Partition		       │ /home/		 │ The first partition with this    │
       │ 933ac7e1-2eb4-4f13-b844-0e14e2aef915 │				       │		 │ type UUID on the same disk as    │
       │				      │				       │		 │ the ESP is mounted to /home/.    │
       ├──────────────────────────────────────┼────────────────────────────────┼─────────────────┼──────────────────────────────────┤
       │ SD_GPT_SRV			      │ Server Data Partition	       │ /srv/		 │ The first partition with this    │
       │ 3b8f8425-20e0-4f3b-907f-1a25a76f98e8 │				       │		 │ type UUID on the same disk as    │
       │				      │				       │		 │ the ESP is mounted to /srv/.	    │
       ├──────────────────────────────────────┼────────────────────────────────┼─────────────────┼──────────────────────────────────┤
       │ SD_GPT_VAR			      │ Variable Data Partition	       │ /var/		 │ The first partition with this    │
       │ 4d21b016-b534-45c2-a9fb-5c16e091fd2d │				       │		 │ type UUID on the same disk as    │
       │				      │				       │		 │ the ESP is mounted to /var/ —    │
       │				      │				       │		 │ under the condition its	    │
       │				      │				       │		 │ partition UUID matches the first │
       │				      │				       │		 │ 128 bit of the HMAC-SHA256 of    │
       │				      │				       │		 │ the GPT type uuid of this	    │
       │				      │				       │		 │ partition keyed by the machine   │
       │				      │				       │		 │ ID of the installation stored in │
       │				      │				       │		 │ machine-id(5).		    │
       ├──────────────────────────────────────┼────────────────────────────────┼─────────────────┼──────────────────────────────────┤
       │ SD_GPT_TMP			      │ Temporary Data Partition       │ /var/tmp/	 │ The first partition with this    │
       │ 7ec6f557-3bc5-4aca-b293-16ef5df639d1 │				       │		 │ type UUID on the same disk as    │
       │				      │				       │		 │ the ESP is mounted to /var/tmp/. │
       ├──────────────────────────────────────┼────────────────────────────────┼─────────────────┼──────────────────────────────────┤
       │ SD_GPT_SWAP			      │ Swap			       │ n/a		 │ All partitions with this type    │
       │ 0657fd6d-a4ab-43c4-84e5-0933c84b4f4f │				       │		 │ UUID on the same disk as the ESP │
       │				      │				       │		 │ are used as swap.		    │
       ├──────────────────────────────────────┼────────────────────────────────┼─────────────────┼──────────────────────────────────┤
       │ SD_GPT_ESP			      │ EFI System Partition (ESP)     │ /efi/ or /boot/ │ The first partition with this    │
       │ c12a7328-f81f-11d2-ba4b-00a0c93ec93b │				       │		 │ type UUID located on the same    │
       │				      │				       │		 │ disk as the root partition is    │
       │				      │				       │		 │ mounted to /boot/ or /efi/, see  │
       │				      │				       │		 │ below.			    │
       ├──────────────────────────────────────┼────────────────────────────────┼─────────────────┼──────────────────────────────────┤
       │ SD_GPT_XBOOTLDR		      │ Extended Boot Loader Partition │ /boot/		 │ The first partition with this    │
       │ bc13c2ff-59e6-4262-a352-b275fd6f7172 │				       │		 │ type UUID located on the same    │
       │				      │				       │		 │ disk as the root partition is    │
       │				      │				       │		 │ mounted to /boot/, see below.    │
       └──────────────────────────────────────┴────────────────────────────────┴─────────────────┴──────────────────────────────────┘

       This generator understands the following attribute flags for partitions:

       Table 2. Partition Attribute Flags
       ┌────────────────────────────────────────┬─────────────────────────────────────┬────────────────────────────────────────┐
       │ Flag					│ Applicable to			      │ Explanation			       │
       ├────────────────────────────────────────┼─────────────────────────────────────┼────────────────────────────────────────┤
       │ SD_GPT_FLAG_READ_ONLY			│ /, /home/, /srv/, /var/, /var/tmp/, │ Partition is mounted read-only	       │
       │ 0x1000000000000000			│ Extended Boot Loader Partition      │					       │
       ├────────────────────────────────────────┼─────────────────────────────────────┼────────────────────────────────────────┤
       │ SD_GPT_FLAG_NO_AUTO 0x8000000000000000 │ /, /home/, /srv/, /var/, /var/tmp/, │ Partition is not mounted automatically │
       │					│ Extended Boot Loader Partition      │					       │
       ├────────────────────────────────────────┼─────────────────────────────────────┼────────────────────────────────────────┤
       │ SD_GPT_FLAG_NO_BLOCK_IO_PROTOCOL	│ EFI System Partition (ESP)	      │ Partition is not mounted automatically │
       │ 0x0000000000000002			│				      │					       │
       └────────────────────────────────────────┴─────────────────────────────────────┴────────────────────────────────────────┘

       The /home/, /srv/, /var/, /var/tmp/ and swap partitions may be encrypted in LUKS format. In this case, a device mapper device is set up under the names
       /dev/mapper/home, /dev/mapper/srv, /dev/mapper/var, /dev/mapper/tmp or /dev/mapper/swap. Note that this might create conflicts if the same partition is
       listed in /etc/crypttab with a different device mapper device name.

       When systemd is running in the initrd the / partition may be encrypted with LUKS as well. In this case, a device mapper device is set up under the name
       /dev/mapper/root, and a sysroot.mount is set up that mounts the device under /sysroot. For more information, see bootup(7).

       The root partition can be specified by symlinking /run/systemd/volatile-root to /dev/block/$major:$minor. This is especially useful if the root mount
       has been replaced by some form of volatile file system (overlayfs).

       Mount and automount units for the EFI System Partition (ESP) and Extended Boot Loader Partition (XBOOTLDR) are generated on EFI systems. If the disk
       contains an XBOOTLDR partition, as defined in the Boot Loader Specification[4], it is made available at /boot/. This generator creates an automount
       unit; the mount will only be activated on-demand when accessed. The mount point will be created if necessary.

       The ESP is mounted to /boot/ if that directory exists and is not used for XBOOTLDR, and otherwise to /efi/. Same as for /boot/, an automount unit is
       used. The mount point will be created if necessary.

       No configuration is created for mount points that are configured in fstab(5) or when the target directory contains files.

       When using this generator in conjunction with btrfs file systems, make sure to set the correct default subvolumes on them, using btrfs subvolume
       set-default.

       If the system was booted via systemd-stub(7) and the stub reported to userspace that the kernel image was measured to a TPM2 PCR, then any discovered
       root and /var/ volume identifiers (and volume encryption key in case it is encrypted) will be automatically measured into PCR 15 on activation, via
       systemd-pcrfs@.service(8).

       systemd-gpt-auto-generator implements systemd.generator(7).

KERNEL COMMAND LINE
       systemd-gpt-auto-generator understands the following kernel command line parameters:

       systemd.gpt_auto, rd.systemd.gpt_auto
	   Those options take an optional boolean argument, and default to yes. The generator is enabled by default, and a false value may be used to disable
	   it (e.g.  "systemd.gpt_auto=0").

	   Added in version 242.

       systemd.image_policy=, rd.systemd.image_policy=
	   Takes an image dissection policy string as argument (as per systemd.image-policy(7)), and allows enforcing a policy on dissection and use of the
	   automatically discovered GPT partition table entries.

	   Added in version 254.

       root=, rootfstype=, rootflags=
	   When root= is used with the special value "gpt-auto" (or if the parameter is not used at all), automatic discovery of the root partition based on
	   the GPT partition type is enabled. Any other value disables this logic.

	   The rootfstype= and rootflags= are used to select the file system type and options when the root file system is automatically discovered.

	   Added in version 242.

       rw, ro
	   Mount the root partition read-write or read-only initially.

	   Note that unlike most kernel command line options these settings do not override configuration in the file system, and the file system may be
	   remounted later. See systemd-remount-fs.service(8).

	   Added in version 242.

       systemd.swap=
	   Takes a boolean argument or enables the option if specified without an argument. If disabled, automatic discovery of swap partition(s) based on GPT
	   partition type is disabled. Defaults to enabled.

	   Added in version 254.

SEE ALSO
       systemd(1), systemd.mount(5), systemd.swap(5), systemd-fstab-generator(8), systemd-cryptsetup@.service(8), systemd-pcrfs@.service(8), machine-id(5),
       cryptsetup(8), fstab(5), btrfs(8)

NOTES
	1. UEFI Specification
	   https://uefi.org/specifications

	2. Discoverable Partitions Specification
	   https://uapi-group.org/specifications/specs/discoverable_partitions_specification

	3. Boot Loader Interface
	   https://systemd.io/BOOT_LOADER_INTERFACE

	4. Boot Loader Specification
	   https://uapi-group.org/specifications/specs/boot_loader_specification

systemd 255															 SYSTEMD-GPT-AUTO-GENERATOR(8)
