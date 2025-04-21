KERNEL-INSTALL(8)							kernel-install							     KERNEL-INSTALL(8)

NAME
       kernel-install - Add and remove kernel and initrd images to and from /boot

SYNOPSIS

       kernel-install [OPTIONS...] add KERNEL-VERSION KERNEL-IMAGE [INITRD-FILE...]

       kernel-install [OPTIONS...] remove KERNEL-VERSION

       kernel-install [OPTIONS...] inspect [KERNEL-VERSION] [KERNEL-IMAGE] [INITRD-FILE...]

       kernel-install [OPTIONS...] list

DESCRIPTION
       kernel-install is used to install and remove kernel and initrd images [1] to and from the boot loader partition, referred to as $BOOT here. It will
       usually be one of /boot/, /efi/, or /boot/efi/, see below.

       kernel-install will run the executable files ("plugins") located in the directory /usr/lib/kernel/install.d/ and the local administration directory
       /etc/kernel/install.d/. All files are collectively sorted and executed in lexical order, regardless of the directory in which they live. However, files
       with identical filenames replace each other. Files in /etc/kernel/install.d/ take precedence over files with the same name in
       /usr/lib/kernel/install.d/. This can be used to override a system-supplied executables with a local file if needed; a symbolic link in
       /etc/kernel/install.d/ with the same name as an executable in /usr/lib/kernel/install.d/, pointing to /dev/null, disables the executable entirely.
       Executables must have the extension ".install"; other extensions are ignored.

       An executable placed in these directories should return 0 on success. It may also return 77 to cause the whole operation to terminate (executables
       later in lexical order will be skipped).

COMMANDS
       The following commands are understood:

       add [[[KERNEL-VERSION] KERNEL-IMAGE] [INITRD-FILE ...]]
	   This command takes a kernel version string and a path to a kernel image file as arguments. If the former is omitted, specified as an empty string
	   or as "-" it defaults to the current kernel version, i.e. the same string uname -r returns. If the latter is omitted, specified as an empty string
	   or as "-" defaults to /usr/lib/modules/KERNEL_VERSION/vmlinuz. Optionally, one or more initrd images may be specified as well (note that plugins
	   might generate additional ones).

	   The executable files from /usr/lib/kernel/install.d/*.install and /etc/kernel/install.d/*.install (i.e. the plugins) are called with the following
	   arguments:

	       add KERNEL-VERSION $BOOT/ENTRY-TOKEN/KERNEL-VERSION/ KERNEL-IMAGE \
			 [INITRD-FILE ...]

	   The third argument directly refers to the path where to place kernel images, initrd images and other resources for Boot Loader Specification[2]
	   Type #1 entries (the "entry directory"). If other boot loader schemes are used the parameter may be ignored.

	   The ENTRY-TOKEN string is typically the machine ID and is supposed to identify the local installation on the system. For details see below.

	   Two default plugins execute the following operations in this case:

	   •   kernel-install creates $BOOT/ENTRY-TOKEN/KERNEL-VERSION, if enabled (see $KERNEL_INSTALL_LAYOUT).

	   •   50-depmod.install runs depmod(8) for the KERNEL-VERSION.

	   •   90-loaderentry.install copies KERNEL-IMAGE to $BOOT/ENTRY-TOKEN/KERNEL-VERSION/linux. If INITRD-FILEs are provided, it also copies them to
	       $BOOT/ENTRY-TOKEN/KERNEL_VERSION/INITRD-FILE. This can also be used to prepend microcode before the actual initrd. It also creates a boot
	       loader entry according to the Boot Loader Specification[2] (Type #1) in $BOOT/loader/entries/ENTRY-TOKEN-KERNEL-VERSION.conf. The title of the
	       entry is the PRETTY_NAME parameter specified in /etc/os-release or /usr/lib/os-release (if the former is missing), or "Linux KERNEL-VERSION",
	       if unset.

	       If $KERNEL_INSTALL_LAYOUT is not "bls", this plugin does nothing.

	   •   90-uki-copy.install copies a file uki.efi from $KERNEL_INSTALL_STAGING_AREA or if it does not exist the KERNEL-IMAGE argument, only if it has a
	       ".efi" extension, to $BOOT/EFI/Linux/ENTRY-TOKEN-KERNEL-VERSION.efi.

	       If $KERNEL_INSTALL_LAYOUT is not "uki", this plugin does nothing.

	   Added in version 198.

       add-all
	   This is the same as add (see above), but invokes the operation iteratively for every installed kernel in /usr/lib/modules/. This operation is only
	   supported on systems where the kernel image is installed in /usr/lib/modules/KERNEL-VERSION/vmlinuz.

	   Added in version 255.

       remove KERNEL-VERSION
	   This command expects a kernel version string as single argument.

	   The executable files from /usr/lib/kernel/install.d/*.install and /etc/kernel/install.d/*.install (i.e. the plugins) are called with the following
	   arguments:

	       remove KERNEL-VERSION $BOOT/ENTRY-TOKEN/KERNEL-VERSION/

	   Afterwards, kernel-install removes the entry directory $BOOT/ENTRY-TOKEN/KERNEL-VERSION/ and its contents, if it exists.

	   Two default plugins execute the following operations in this case:

	   •   50-depmod.install removes the files generated by depmod for this kernel again.

	   •   90-loaderentry.install removes the file $BOOT/loader/entries/ENTRY-TOKEN-KERNEL-VERSION.conf.

	   •   90-uki-copy.install removes the file $BOOT/EFI/Linux/ENTRY-TOKEN-KERNEL-VERSION.efi.

	   Added in version 198.

       inspect [[[KERNEL-VERSION] KERNEL-IMAGE] [INITRD-FILE ...]]
	   Takes the same parameters as add.

	   Shows the various paths and parameters configured or auto-detected. In particular shows the values of the various $KERNEL_INSTALL_* environment
	   variables listed below, as they would be passed to plugins. The --json option can be used to get the output of this verb as a JSON object.

	   Added in version 251.

       list
	   Shows the various installed kernels. This enumerates the subdirectories of /usr/lib/modules/, and shows whether a kernel image is installed there.

	   Added in version 255.

COMPATIBILITY WITH THE KERNEL BUILD SYSTEM

       installkernel [OPTIONS...] VERSION VMLINUZ [MAP] [INSTALLATION-DIR]

       When invoked as installkernel, this program accepts arguments as specified by the kernel build system's make install command. The VERSION and VMLINUZ
       parameters specify the kernel version and the kernel binary. The other two parameters (MAP and INSTALLATION-DIR) are currently ignored.

THE $BOOT PARTITION
       The partition where the kernels and Boot Loader Specification[2] snippets are located is called $BOOT.  kernel-install determines the location of this
       partition by checking /efi/, /boot/, and /boot/efi/ in turn. The first location where $BOOT/loader/entries/ or $BOOT/ENTRY-TOKEN/ exists is used.

OPTIONS
       The following options are understood:

       --esp-path=
	   Path to the EFI System Partition (ESP). If not specified, /efi/, /boot/, and /boot/efi/ are checked in turn. It is recommended to mount the ESP to
	   /efi/, if possible.

       --boot-path=
	   Path to the Extended Boot Loader partition, as defined in the Boot Loader Specification[2]. If not specified, /boot/ is checked. It is recommended
	   to mount the Extended Boot Loader partition to /boot/, if possible.

       --make-entry-directory=yes|no|auto
	   Controls creation and deletion of the Boot Loader Specification[2] Type #1 entry directory on the file system containing resources such as kernel
	   and initrd images during add and remove, respectively. The directory is named after the entry token, and is placed immediately below the boot root
	   directory. When "auto", the directory is created or removed only when the install layout is "bls". Defaults to "auto".

	   Added in version 254.

       --entry-token=
	   Controls how to name and identify boot loader entries for this kernel installation or deletion. Takes one of "auto", "machine-id", "os-id",
	   "os-image-id", or an arbitrary string prefixed by "literal:" as argument.

	   If set to machine-id the entries are named after the machine ID of the running system (e.g.	"b0e793a9baf14b5fa13ecbe84ff637ac"). See machine-id(5)
	   for details about the machine ID concept and file.

	   If set to os-id the entries are named after the OS ID of the running system, i.e. the ID= field of os-release(5) (e.g.  "fedora"). Similarly, if
	   set to os-image-id the entries are named after the OS image ID of the running system, i.e. the IMAGE_ID= field of os-release (e.g.
	   "vendorx-cashier-system").

	   If set to auto (the default), the /etc/kernel/entry-token (or $KERNEL_INSTALL_CONF_ROOT/entry-token) file will be read if it exists, and the stored
	   value used. Otherwise if the local machine ID is initialized it is used. Otherwise IMAGE_ID= from os-release will be used, if set. Otherwise, ID=
	   from os-release will be used, if set. Otherwise a randomly generated machine ID is used.

	   Using the machine ID for naming the entries is generally preferable, however there are cases where using the other identifiers is a good option.
	   Specifically: if the identification data that the machine ID entails shall not be stored on the (unencrypted) $BOOT_ROOT partition, or if the ID
	   shall be generated on first boot and is not known when the entries are prepared. Note that using the machine ID has the benefit that multiple
	   parallel installations of the same OS can coexist on the same medium, and they can update their boot loader entries independently. When using
	   another identifier (such as the OS ID or the OS image ID), parallel installations of the same OS would try to use the same entry name. To support
	   parallel installations, the installer must use a different entry token when adding a second installation.

	   Added in version 254.

       -v, --verbose
	   Output additional information about operations being performed.

	   Added in version 242.

       --root=root
	   Takes a directory path as an argument. All paths will be prefixed with the given alternate root path, including config search paths. This is useful
	   to operate on a system image mounted to the specified directory instead of the host system itself.

	   Added in version 255.

       --image=image
	   Takes a path to a disk image file or block device node. If specified, all operations are applied to the file system in the indicated disk image.
	   This option is similar to --root=, but operates on file systems stored in disk images or block devices. The disk image should either contain just a
	   file system or a set of file systems within a GPT partition table, following the Discoverable Partitions Specification[3]. For further information
	   on supported disk images, see systemd-nspawn(1)'s switch of the same name.

	   Added in version 255.

       -h, --help
	   Print a short help text and exit.

       --version
	   Print a short version string and exit.

       --no-pager
	   Do not pipe output into a pager.

       --json=MODE
	   Shows output formatted as JSON. Expects one of "short" (for the shortest possible output without any redundant whitespace or line breaks), "pretty"
	   (for a pretty version of the same, with indentation and line breaks) or "off" (to turn off JSON output, the default).

       --image-policy=policy
	   Takes an image policy string as argument, as per systemd.image-policy(7). The policy is enforced when operating on the disk image specified via
	   --image=, see above. If not specified defaults to the "*" policy, i.e. all recognized file systems in the image are used.

       --no-legend
	   Do not print the legend, i.e. column headers and the footer with hints.

ENVIRONMENT VARIABLES
   Environment variables exported for plugins
       If --verbose is used, $KERNEL_INSTALL_VERBOSE=1 will be exported for plugins. They may output additional logs in this case.

       $KERNEL_INSTALL_IMAGE_TYPE=uki|pe|unknown is set for the plugins to specify the type of the kernel image.

       uki
	   Unified kernel image.

	   Added in version 254.

       pe
	   PE binary.

	   Added in version 254.

       unknown
	   Unknown type.

	   Added in version 254.

       $KERNEL_INSTALL_MACHINE_ID is set for the plugins to the desired machine-id to use. It's always a 128-bit ID. Normally it's read from /etc/machine-id,
       but it can also be overridden via $MACHINE_ID (see below). If not specified via these methods, a fallback value will generated by kernel-install and
       used only for a single invocation.

       $KERNEL_INSTALL_ENTRY_TOKEN is set for the plugins to the desired entry "token" to use. It's an identifier that shall be used to identify the local
       installation, and is often the machine ID, i.e. same as $KERNEL_INSTALL_MACHINE_ID, but might also be a different type of identifier, for example a
       fixed string or the ID=, IMAGE_ID= values from /etc/os-release. The string passed here will be used to name Boot Loader Specification entries, or the
       directories the kernel image and initial RAM disk images are placed into.

       Note that while $KERNEL_INSTALL_ENTRY_TOKEN and $KERNEL_INSTALL_MACHINE_ID are often set to the same value, the latter is guaranteed to be a valid 32
       character ID in lowercase hexadecimals while the former can be any short string. The entry token to use is read from /etc/kernel/entry-token, if it
       exists. Otherwise a few possible candidates below $BOOT are checked for Boot Loader Specification Type 1 entry directories, and if found the entry
       token is derived from that. If that is not successful, $KERNEL_INSTALL_MACHINE_ID is used as fallback.

       $KERNEL_INSTALL_BOOT_ROOT is set for the plugins to the absolute path of the root directory (mount point, usually) of the hierarchy where boot loader
       entries, kernel images, and associated resources should be placed. This usually is the path where the XBOOTLDR partition or the ESP (EFI System
       Partition) are mounted, and also conceptually referred to as $BOOT. Can be overridden by setting $BOOT_ROOT (see below).

       $KERNEL_INSTALL_LAYOUT=auto|bls|uki|other|...  is set for the plugins to specify the installation layout. Additional layout names may be defined by
       convention. If a plugin uses a special layout, it's encouraged to declare its own layout name and configure layout= in install.conf upon initial
       installation. The following values are currently understood:

       bls
	   Standard Boot Loader Specification[2] Type #1 layout, compatible with systemd-boot(7): entries in
	   $BOOT/loader/entries/ENTRY-TOKEN-KERNEL-VERSION[+TRIES].conf, kernel and initrds under $BOOT/ENTRY-TOKEN/KERNEL-VERSION/

	   Implemented by 90-loaderentry.install.

	   Added in version 250.

       uki
	   Standard Boot Loader Specification[2] Type #2 layout, compatible with systemd-boot(7): unified kernel images under $BOOT/EFI/Linux as
	   $BOOT/EFI/Linux/ENTRY-TOKEN-KERNEL-VERSION[+TRIES].efi.

	   Implemented by 90-uki-copy.install.

	   Added in version 253.

       other
	   Some other layout not understood natively by kernel-install.

	   Added in version 250.

       auto
	   Pick the layout automatically. If the kernel is a UKI set layout to uki. If not default to bls if $BOOT/loader/entries.srel with content "type1" or
	   $BOOT/ENTRY-TOKEN exists, or other otherwise.

	   Leaving layout blank has the same effect. This is the default.

	   Added in version 254.

       $KERNEL_INSTALL_INITRD_GENERATOR and $KERNEL_INSTALL_UKI_GENERATOR are set for plugins to select the initrd and/or UKI generator. This may be
       configured as initrd_generator= and uki_generator= in install.conf, see below.

       $KERNEL_INSTALL_STAGING_AREA is set for plugins to a path to a directory. Plugins may drop files in that directory, and they will be installed as part
       of the loader entry, based on the file name and extension: Files named initrd* will be installed as INITRD-FILEs, and files named microcode* will be
       prepended before INITRD-FILEs.

   Environment variables understood by kernel-install
       $KERNEL_INSTALL_CONF_ROOT can be set to override the location of the configuration files read by kernel-install. When set, install.conf, entry-token,
       and other files will be read from this directory.

       $KERNEL_INSTALL_PLUGINS can be set to override the list of plugins executed by kernel-install. The argument is a whitespace-separated list of paths.
       "KERNEL_INSTALL_PLUGINS=:" may be used to prevent any plugins from running.

       $MACHINE_ID can be set for kernel-install to override $KERNEL_INSTALL_MACHINE_ID, the machine ID.

       $BOOT_ROOT can be set for kernel-install to override $KERNEL_INSTALL_BOOT_ROOT, the installation location for boot entries.

       The last two variables may also be set in install.conf. Variables set in the environment take precedence over the values specified in the config file.

EXIT STATUS
       If every executable returns 0 or 77, 0 is returned, and a non-zero failure code otherwise.

FILES
       /etc/kernel/install.d/*.install, /usr/lib/kernel/install.d/*.install
	   Drop-in files which are executed by kernel-install.

	   Added in version 198.

       /etc/kernel/cmdline, /usr/lib/kernel/cmdline, /proc/cmdline
	   Specifies the kernel command line to use. The first of the files that is found will be used.	 $KERNEL_INSTALL_CONF_ROOT may be used to override the
	   search path; see below for details.

	   Added in version 198.

       /etc/kernel/devicetree, /usr/lib/kernel/devicetree
	   Specifies the partial path to the file containing the device tree blob to install with the kernel and use at boot. The first of the files that is
	   found will be used.	$KERNEL_INSTALL_CONF_ROOT may be used to override the search path; see below for details.

	   The devicetree file contains a path, and this path specifies a location relative to the kernel install tree. A set of locations is checked,
	   including in particular /usr/lib/modules/KERNEL_VERSION/dtb/, which is the recommended location to place the dtb files under. For example, with
	   "broadcom/bcm2711-rpi-4-b.dtb" in the devicetree file, the device tree blob for the Raspberry Pi 4 Model B would be installed, and the actual file
	   would be /usr/lib/modules/KERNEL_VERSION/dtb/broadcom/bcm2711-rpi-4-b.dtb.

	   Added in version 255.

       /etc/kernel/tries
	   Read by 90-loaderentry.install and 90-uki-copy.install. If this file exists, a numeric value is read from it and the naming of the generated entry
	   file or UKI is altered to include it as $BOOT/loader/entries/ENTRY-TOKEN-KERNEL-VERSION+TRIES.conf or
	   $BOOT/EFI/Linux/ENTRY-TOKEN-KERNEL-VERSION+TRIES.efi, respectively. This is useful for boot loaders such as systemd-boot(7) which implement boot
	   attempt counting with a counter embedded in the entry file name.  $KERNEL_INSTALL_CONF_ROOT may be used to override the search path; see below for
	   details.

	   Added in version 240.

       /etc/kernel/entry-token
	   If this file exists it is read and used as "entry token" for this system, i.e. is used for naming Boot Loader Specification entries. See
	   $KERNEL_INSTALL_ENTRY_TOKEN above for details.  $KERNEL_INSTALL_CONF_ROOT may be used to override the search path; see below for details.

	   Added in version 251.

       /etc/machine-id
	   The content of this file specifies the machine identification MACHINE-ID.

	   Added in version 198.

       /etc/os-release, /usr/lib/os-release
	   Read by 90-loaderentry.install. If available, PRETTY_NAME= is read from these files and used as the title of the boot menu entry. Otherwise, "Linux
	   KERNEL-VERSION" will be used.

	   Added in version 198.

       /etc/kernel/install.conf, /usr/lib/kernel/install.conf
	   Configuration file with options for kernel-install, as a series of KEY=VALUE assignments, compatible with shell syntax, following the same rules as
	   described in os-release(5). The first of the files that is found will be used.  $KERNEL_INSTALL_CONF_ROOT may be used to override the search path;
	   see below for details.

	   Currently, the following keys are supported: MACHINE_ID=, BOOT_ROOT=, layout=, initrd_generator=, uki_generator=. See the Environment variables
	   section above for details.

	   Added in version 250.

       /etc/kernel/uki.conf
	   Ini-style configuration file for ukify(1) which is only effective when $KERNEL_INSTALL_LAYOUT or layout= in install.conf is set to uki and
	   $KERNEL_INSTALL_UKI_GENERATOR or uki_generator= in install.conf is set to ukify, or is unset.  $KERNEL_INSTALL_CONF_ROOT may be used to override
	   the search path; see below for details.

	   Added in version 255.

       /usr/lib/modules/KERNEL-VERSION/
	   Location for installed kernel modules and other kernel related resources. For each locally installed kernel a directory named after the kernel
	   version (uname -r) is kept.

	   Added in version 255.

       /usr/lib/modules/KERNEL-VERSION/vmlinuz
	   Location for installed kernel images. This is the recommended location for OS package managers to install kernel images into (as applicable), from
	   which kernel-install add then copies it into the final boot partition.

	   Added in version 255.

       For various cases listed above, if the $KERNEL_INSTALL_CONF_ROOT environment variable is set, it will override the search path. The files will be
       loaded only from the directory specified by the environment variable. When the variable is not set, the listed paths are tried in turn, and the first
       file that exists is used.

SEE ALSO
       machine-id(5), os-release(5), depmod(8), systemd-boot(7), ukify(1), Boot Loader Specification[2]

NOTES
	1. Nowadays actually CPIO archives used as an "initramfs", rather than "initrd". See bootup(7) for an explanation.

	2. Boot Loader Specification
	   https://uapi-group.org/specifications/specs/boot_loader_specification

	3. Discoverable Partitions Specification
	   https://uapi-group.org/specifications/specs/discoverable_partitions_specification

systemd 255																     KERNEL-INSTALL(8)
