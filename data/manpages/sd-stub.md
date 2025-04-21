SYSTEMD-STUB(7)								 systemd-stub							       SYSTEMD-STUB(7)

NAME
       systemd-stub, sd-stub, linuxx64.efi.stub, linuxia32.efi.stub, linuxaa64.efi.stub - A simple UEFI kernel boot stub

SYNOPSIS
       /usr/lib/systemd/boot/efi/linuxx64.efi.stub

       /usr/lib/systemd/boot/efi/linuxia32.efi.stub

       /usr/lib/systemd/boot/efi/linuxaa64.efi.stub

       ESP/.../foo.efi.extra.d/*.addon.efi

       ESP/.../foo.efi.extra.d/*.cred

       ESP/.../foo.efi.extra.d/*.raw

       ESP/loader/addons/*.addon.efi

       ESP/loader/credentials/*.cred

DESCRIPTION
       systemd-stub (stored in per-architecture files linuxx64.efi.stub, linuxia32.efi.stub, linuxaa64.efi.stub on disk) is a simple UEFI boot stub. An UEFI
       boot stub is attached to a Linux kernel binary image, and is a piece of code that runs in the UEFI firmware environment before transitioning into the
       Linux kernel environment. The UEFI boot stub ensures a Linux kernel is executable as regular UEFI binary, and is able to do various preparations before
       switching the system into the Linux world.

       The UEFI boot stub looks for various resources for the kernel invocation inside the UEFI PE binary itself. This allows combining various resources
       inside a single PE binary image (usually called "Unified Kernel Image", or "UKI" for short), which may then be signed via UEFI SecureBoot as a whole,
       covering all individual resources at once. Specifically it may include:

       •   A ".linux" section with the ELF Linux kernel image.

       •   An ".osrel" section with OS release information, i.e. the contents of the os-release(5) file of the OS the kernel belongs to.

       •   A ".cmdline" section with the kernel command line to pass to the invoked kernel.

       •   An ".initrd" section with the initrd.

       •   A ".splash" section with an image (in the Windows .BMP format) to show on screen before invoking the kernel.

       •   A ".dtb" section with a compiled binary DeviceTree.

       •   A ".uname" section with the kernel version information, i.e. the output of uname -r for the kernel included in the ".linux" section.

       •   An ".sbat" section with SBAT[1] revocation metadata.

       •   A ".pcrsig" section with a set of cryptographic signatures for the expected TPM2 PCR values after the kernel has been booted, in JSON format. This
	   is useful for implementing TPM2 policies that bind disk encryption and similar to kernels that are signed by a specific key.

       •   A ".pcrpkey" section with a public key in the PEM format matching the signature data in the the ".pcrsig" section.

       If UEFI SecureBoot is enabled and the ".cmdline" section is present in the executed image, any attempts to override the kernel command line by passing
       one as invocation parameters to the EFI binary are ignored. Thus, in order to allow overriding the kernel command line, either disable UEFI SecureBoot,
       or don't include a kernel command line PE section in the kernel image file. If a command line is accepted via EFI invocation parameters to the EFI
       binary it is measured into TPM PCR 12 (if a TPM is present).

       If a DeviceTree is embedded in the ".dtb" section, it replaces an existing DeviceTree in the corresponding EFI configuration table. systemd-stub will
       ask the firmware via the "EFI_DT_FIXUP_PROTOCOL" for hardware specific fixups to the DeviceTree.

       The contents of eight of these nine sections are measured into TPM PCR 11. It is otherwise not used and thus the result can be pre-calculated without
       too much effort. The ".pcrsig" section is not included in this PCR measurement, since it is supposed to contain signatures for the output of the
       measurement operation, and thus cannot also be input to it.

       When ".pcrsig" and/or ".pcrpkey" sections are present in a unified kernel image their contents are passed to the booted kernel in an synthetic initrd
       cpio archive that places them in the /.extra/tpm2-pcr-signature.json and /.extra/tpm2-pcr-public-key.pem files. Typically, a tmpfiles.d(5) line then
       ensures they are copied into /run/systemd/tpm2-pcr-signature.json and /run/systemd/tpm2-pcr-public-key.pem where they remain accessible even after the
       system transitions out of the initrd environment into the host file system. Tools such systemd-cryptsetup@.service(8), systemd-cryptenroll(1) and
       systemd-creds(1) will automatically use files present under these paths to unlock protected resources (encrypted storage or credentials) or bind
       encryption to booted kernels.

       For further details about the UKI concept, see the UKI specification[2].

COMPANION FILES
       The systemd-stub UEFI boot stub automatically collects three types of auxiliary companion files optionally placed in drop-in directories on the same
       partition as the EFI binary, dynamically generates cpio initrd archives from them, and passes them to the kernel. Specifically:

       •   For a kernel binary called foo.efi, it will look for files with the .cred suffix in a directory named foo.efi.extra.d/ next to it. If the kernel
	   binary uses a counter for the purpose of Automatic Boot Assessment[3], this counter will be ignored. For example, foo+3-0.efi will look in
	   directory foo.efi.extra.d/. A cpio archive is generated from all files found that way, placing them in the /.extra/credentials/ directory of the
	   initrd file hierarchy. The main initrd may then access them in this directory. This is supposed to be used to store auxiliary, encrypted,
	   authenticated credentials for use with LoadCredentialEncrypted= in the UEFI System Partition. See systemd.exec(5) and systemd-creds(1) for details
	   on encrypted credentials. The generated cpio archive is measured into TPM PCR 12 (if a TPM is present).

       •   Similarly, files foo.efi.extra.d/*.raw are packed up in a cpio archive and placed in the /.extra/sysext/ directory in the initrd file hierarchy.
	   This is supposed to be used to pass additional system extension images to the initrd. See systemd-sysext(8) for details on system extension images.
	   The generated cpio archive containing these system extension images is measured into TPM PCR 13 (if a TPM is present).

       •   Similarly, files foo.efi.extra.d/*.addon.efi are loaded and verified as PE binaries, and a ".cmdline" section is parsed from them. Addons are
	   supposed to be used to pass additional kernel command line parameters or Devicetree blobs, regardless of the kernel image being booted, for example
	   to allow platform vendors to ship platform-specific configuration.

	   In case Secure Boot is enabled, these files will be validated using keys in UEFI DB, Shim's DB or Shim's MOK, and will be rejected otherwise.
	   Additionally, if the both the addon and the UKI contain a a ".uname" section, the addon will be rejected if they do not match exactly. It is
	   recommended to always add a ".sbat" section to all signed addons, so that they may be revoked with a SBAT policy update, without requiring
	   blocklisting via DBX/MOKX. The ukify(1) tool will add a SBAT policy by default if none is passed when building addons. For more information on SBAT
	   see Shim documentation[1].

	   Addon files are sorted, loaded, and measured into TPM PCR 12 (if a TPM is present) and appended to the kernel command line. UKI command line
	   options are listed first, then options from addons in /loader/addons/*.addon.efi, and finally UKI-specific addons. Device tree blobs are loaded and
	   measured following the same algorithm. Addons are always loaded in the same order based on the filename, so that, given the same set of addons, the
	   same set of measurements can be expected in PCR12. However, note that the filename is not protected by the PE signature, and as such an attacker
	   with write access to the ESP could potentially rename these files to change the order in which they are loaded, in a way that could alter the
	   functionality of the kernel, as some options might be order-dependent. If you sign such addons, you should pay attention to the PCR12 values and
	   make use of an attestation service so that improper use of your signed addons can be detected and dealt with using one of the aforementioned
	   revocation mechanisms.

       •   Files /loader/credentials/*.cred are packed up in a cpio archive and placed in the /.extra/global_credentials/ directory of the initrd file
	   hierarchy. This is supposed to be used to pass additional credentials to the initrd, regardless of the kernel being booted. The generated cpio
	   archive is measured into TPM PCR 12 (if a TPM is present).

       •   Additionally, files /loader/addons/*.addon.efi are loaded and verified as PE binaries, and ".cmdline" and/or ".dtb" sections are parsed from them.
	   This is supposed to be used to pass additional command line parameters or Devicetree blobs to the kernel, regardless of the kernel being booted.

       These mechanisms may be used to parameterize and extend trusted (i.e. signed), immutable initrd images in a reasonably safe way: all data they contain
       is measured into TPM PCRs. On access they should be further validated: in case of the credentials case by encrypting/authenticating them via TPM, as
       exposed by systemd-creds encrypt -T (see systemd-creds(1) for details); in case of the system extension images by using signed Verity images.

TPM PCR NOTES
       Note that when a unified kernel using systemd-stub is invoked the firmware will measure it as a whole to TPM PCR 4, covering all embedded resources,
       such as the stub code itself, the core kernel, the embedded initrd and kernel command line (see above for a full list).

       Also note that the Linux kernel will measure all initrds it receives into TPM PCR 9. This means every type of initrd will be measured two or three
       times: the initrd embedded in the kernel image will be measured to PCR 4, PCR 9 and PCR 11; the initrd synthesized from credentials will be measured to
       both PCR 9 and PCR 12; the initrd synthesized from system extensions will be measured to both PCR 4 and PCR 9. Let's summarize the OS resources and the
       PCRs they are measured to:

       Table 1. OS Resource PCR Summary
       ┌───────────────────────────────────────────────────────┬─────────────────┐
       │ OS Resource					       │ Measurement PCR │
       ├───────────────────────────────────────────────────────┼─────────────────┤
       │ systemd-stub code (the entry point of the unified PE  │ 4		 │
       │ binary)					       │		 │
       ├───────────────────────────────────────────────────────┼─────────────────┤
       │ Core kernel code (embedded in unified PE binary)      │ 4 + 11		 │
       ├───────────────────────────────────────────────────────┼─────────────────┤
       │ OS release information (embedded in the unified PE    │ 4 + 11		 │
       │ binary)					       │		 │
       ├───────────────────────────────────────────────────────┼─────────────────┤
       │ Main initrd (embedded in unified PE binary)	       │ 4 + 9 + 11	 │
       ├───────────────────────────────────────────────────────┼─────────────────┤
       │ Default kernel command line (embedded in unified PE   │ 4 + 11		 │
       │ binary)					       │		 │
       ├───────────────────────────────────────────────────────┼─────────────────┤
       │ Overridden kernel command line			       │ 12		 │
       ├───────────────────────────────────────────────────────┼─────────────────┤
       │ Boot splash (embedded in the unified PE binary)       │ 4 + 11		 │
       ├───────────────────────────────────────────────────────┼─────────────────┤
       │ TPM2 PCR signature JSON (embedded in unified PE       │ 4 + 9		 │
       │ binary, synthesized into initrd)		       │		 │
       ├───────────────────────────────────────────────────────┼─────────────────┤
       │ TPM2 PCR PEM public key (embedded in unified PE       │ 4 + 9 + 11	 │
       │ binary, synthesized into initrd)		       │		 │
       ├───────────────────────────────────────────────────────┼─────────────────┤
       │ Credentials (synthesized initrd from companion files) │ 9 + 12		 │
       ├───────────────────────────────────────────────────────┼─────────────────┤
       │ System Extensions (synthesized initrd from companion  │ 9 + 13		 │
       │ files)						       │		 │
       └───────────────────────────────────────────────────────┴─────────────────┘

EFI VARIABLES
       The following EFI variables are defined, set and read by systemd-stub, under the vendor UUID "4a67b082-0a4c-41cf-b6c7-440b29bb8c4f", for communication
       between the boot stub and the OS:

       LoaderDevicePartUUID
	   Contains the partition UUID of the EFI System Partition the EFI image was run from.	systemd-gpt-auto-generator(8) uses this information to
	   automatically find the disk booted from, in order to discover various other partitions on the same disk automatically.

	   Added in version 250.

       LoaderFirmwareInfo, LoaderFirmwareType
	   Brief firmware information. Use bootctl(1) to view this data.

	   Added in version 250.

       LoaderImageIdentifier
	   The path of EFI executable, relative to the EFI System Partition's root directory. Use bootctl(1) to view this data.

	   Added in version 250.

       StubInfo
	   Brief stub information. Use bootctl(1) to view this data.

	   Added in version 250.

       StubPcrKernelImage
	   The PCR register index the kernel image, initrd image, boot splash, devicetree database, and the embedded command line are measured into, formatted
	   as decimal ASCII string (e.g.  "11"). This variable is set if a measurement was successfully completed, and remains unset otherwise.

	   Added in version 252.

       StubPcrKernelParameters
	   The PCR register index the kernel command line and credentials are measured into, formatted as decimal ASCII string (e.g.  "12"). This variable is
	   set if a measurement was successfully completed, and remains unset otherwise.

	   Added in version 252.

       StubPcrInitRDSysExts
	   The PCR register index the systemd extensions for the initrd, which are picked up from the file system the kernel image is located on. Formatted as
	   decimal ASCII string (e.g.  "13"). This variable is set if a measurement was successfully completed, and remains unset otherwise.

	   Added in version 252.

       Note that some of the variables above may also be set by the boot loader. The stub will only set them if they aren't set already. Some of these
       variables are defined by the Boot Loader Interface[4].

INITRD RESOURCES
       The following resources are passed as initrd cpio archives to the booted kernel, and thus make up the initial file system hierarchy in the initrd
       execution environment:

       /
	   The main initrd from the ".initrd" PE section of the unified kernel image.

	   Added in version 252.

       /.extra/credentials/*.cred
	   Credential files (suffix ".cred") that are placed next to the unified kernel image (as described above) are copied into the /.extra/credentials/
	   directory in the initrd execution environment.

	   Added in version 252.

       /.extra/global_credentials/*.cred
	   Similarly, credential files in the /loader/credentials/ directory in the file system the unified kernel image is placed in are copied into the
	   /.extra/global_credentials/ directory in the initrd execution environment.

	   Added in version 252.

       /.extra/sysext/*.raw
	   System extension image files (suffix ".raw") that are placed next to the unified kernel image (as described above) are copied into the
	   /.extra/sysext/ directory in the initrd execution environment.

	   Added in version 252.

       /.extra/tpm2-pcr-signature.json
	   The TPM2 PCR signature JSON object included in the ".pcrsig" PE section of the unified kernel image is copied into the
	   /.extra/tpm2-pcr-signature.json file in the initrd execution environment.

	   Added in version 252.

       /.extra/tpm2-pcr-pkey.pem
	   The PEM public key included in the ".pcrpkey" PE section of the unified kernel image is copied into the /.extra/tpm2-pcr-public-key.pem file in the
	   initrd execution environment.

	   Added in version 252.

       Note that all these files are located in the "tmpfs" file system the kernel sets up for the initrd file hierarchy and are thus lost when the system
       transitions from the initrd execution environment into the host file system. If these resources shall be kept around over this transition they need to
       be copied to a place that survives the transition first, for example via a suitable tmpfiles.d(5) line. By default, this is done for the TPM2 PCR
       signature and public key files.

SMBIOS TYPE 11 STRINGS
       systemd-stub can be configured using SMBIOS Type 11 strings. Applicable strings consist of a name, followed by "=", followed by the value.
       systemd-stub will search the table for a string with a specific name, and if found, use its value. The following strings are read:

       io.systemd.stub.kernel-cmdline-extra
	   If set, the value of this string is added to the list of kernel command line arguments that are measured in PCR12 and passed to the kernel.

	   Added in version 254.

ASSEMBLING KERNEL IMAGES
       In order to assemble a bootable Unified Kernel Image from various components as described above, use ukify(1).

SEE ALSO
       systemd-boot(7), systemd.exec(5), systemd-creds(1), systemd-sysext(8), Boot Loader Specification[5], Boot Loader Interface[4], ukify(1), systemd-
       measure(1), TPM2 PCR Measurements Made by systemd[6]

NOTES
	1. SBAT
	   https://github.com/rhboot/shim/blob/main/SBAT.md

	2. UKI specification
	   https://uapi-group.org/specifications/specs/unified_kernel_image/

	3. Automatic Boot Assessment
	   https://systemd.io/AUTOMATIC_BOOT_ASSESSMENT

	4. Boot Loader Interface
	   https://systemd.io/BOOT_LOADER_INTERFACE

	5. Boot Loader Specification
	   https://uapi-group.org/specifications/specs/boot_loader_specification

	6. TPM2 PCR Measurements Made by systemd
	   https://systemd.io/TPM2_PCR_MEASUREMENTS

systemd 255																       SYSTEMD-STUB(7)
