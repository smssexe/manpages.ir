MACHINE-ID(5)								  machine-id								 MACHINE-ID(5)

NAME
       machine-id - Local machine ID configuration file

SYNOPSIS
       /etc/machine-id

DESCRIPTION
       The /etc/machine-id file contains the unique machine ID of the local system that is set during installation or boot. The machine ID is a single
       newline-terminated, hexadecimal, 32-character, lowercase ID. When decoded from hexadecimal, this corresponds to a 16-byte/128-bit value. This ID may
       not be all zeros.

       The machine ID is usually generated from a random source during system installation or first boot and stays constant for all subsequent boots.
       Optionally, for stateless systems, it is generated during runtime during early boot if necessary.

       The machine ID may be set, for example when network booting, with the systemd.machine_id= kernel command line parameter or by passing the option
       --machine-id= to systemd. An ID specified in this manner has higher priority and will be used instead of the ID stored in /etc/machine-id.

       The machine ID does not change based on local or network configuration or when hardware is replaced. Due to this and its greater length, it is a more
       useful replacement for the gethostid(3) call that POSIX specifies.

       This machine ID adheres to the same format and logic as the D-Bus machine ID.

       This ID uniquely identifies the host. It should be considered "confidential", and must not be exposed in untrusted environments, in particular on the
       network. If a stable unique identifier that is tied to the machine is needed for some application, the machine ID or any part of it must not be used
       directly. Instead the machine ID should be hashed with a cryptographic, keyed hash function, using a fixed, application-specific key. That way the ID
       will be properly unique, and derived in a constant way from the machine ID but there will be no way to retrieve the original machine ID from the
       application-specific one. The sd_id128_get_machine_app_specific(3) API provides an implementation of such an algorithm.

INITIALIZATION
       Each machine should have a non-empty ID in normal operation. The ID of each machine should be unique. To achieve those objectives, /etc/machine-id can
       be initialized in a few different ways.

       For normal operating system installations, where a custom image is created for a specific machine, /etc/machine-id should be populated during
       installation.

       systemd-machine-id-setup(1) may be used by installer tools to initialize the machine ID at install time, but /etc/machine-id may also be written using
       any other means.

       For operating system images which are created once and used on multiple machines, for example for containers or in the cloud, /etc/machine-id should be
       either missing or an empty file in the generic file system image (the difference between the two options is described under "First Boot Semantics"
       below). An ID will be generated during boot and saved to this file if possible. Having an empty file in place is useful because it allows a temporary
       file to be bind-mounted over the real file, in case the image is used read-only. Also see Safely Building Images[1].

       systemd-firstboot(1) may be used to initialize /etc/machine-id on mounted (but not booted) system images.

       When a machine is booted with systemd(1) the ID of the machine will be established. If systemd.machine_id= or --machine-id= options (see first section)
       are specified, this value will be used. Otherwise, the value in /etc/machine-id will be used. If this file is empty or missing, systemd will attempt to
       use the D-Bus machine ID from /var/lib/dbus/machine-id, the value of the kernel command line option container_uuid, the KVM DMI product_uuid or the
       devicetree vm,uuid (on KVM systems), the Xen hypervisor uuid, and finally a randomly generated UUID.

       After the machine ID is established, systemd(1) will attempt to save it to /etc/machine-id. If this fails, it will attempt to bind-mount a temporary
       file over /etc/machine-id. It is an error if the file system is read-only and does not contain a (possibly empty) /etc/machine-id file.

       systemd-machine-id-commit.service(8) will attempt to write the machine ID to the file system if /etc/machine-id or /etc/ are read-only during early
       boot but become writable later on.

FIRST BOOT SEMANTICS
       /etc/machine-id is used to decide whether a boot is the first one. The rules are as follows:

	1. The kernel command argument systemd.condition-first-boot= may be used to override the autodetection logic, see kernel-command-line(7).

	2. Otherwise, if /etc/machine-id does not exist, this is a first boot. During early boot, systemd will write "uninitialized\n" to this file and
	   overmount a temporary file which contains the actual machine ID. Later (after first-boot-complete.target has been reached), the real machine ID
	   will be written to disk.

	3. If /etc/machine-id contains the string "uninitialized", a boot is also considered the first boot. The same mechanism as above applies.

	4. If /etc/machine-id exists and is empty, a boot is not considered the first boot.  systemd will still bind-mount a file containing the actual
	   machine-id over it and later try to commit it to disk (if /etc/ is writable).

	5. If /etc/machine-id already contains a valid machine-id, this is not a first boot.

       If according to the above rules a first boot is detected, units with ConditionFirstBoot=yes will be run and systemd will perform additional
       initialization steps, in particular presetting units.

RELATION TO OSF UUIDS
       Note that the machine ID historically is not an OSF UUID as defined by RFC 4122[2], nor a Microsoft GUID; however, starting with systemd v30, newly
       generated machine IDs do qualify as Variant 1 Version 4 UUIDs, as per RFC 4122.

       In order to maintain compatibility with existing installations, an application requiring a strictly RFC 4122 compliant UUID should decode the machine
       ID, and then (non-reversibly) apply the following operations to turn it into a valid RFC 4122 Variant 1 Version 4 UUID. With "id" being an unsigned
       character array:

	   /* Set UUID version to 4 --- truly random generation */
	   id[6] = (id[6] & 0x0F) | 0x40;
	   /* Set the UUID variant to DCE */
	   id[8] = (id[8] & 0x3F) | 0x80;

       (This code is inspired by "generate_random_uuid()" of drivers/char/random.c from the Linux kernel sources.)

HISTORY
       The simple configuration file format of /etc/machine-id originates in the /var/lib/dbus/machine-id file introduced by D-Bus. In fact, this latter file
       might be a symlink to /etc/machine-id.

SEE ALSO
       systemd(1), systemd-machine-id-setup(1), gethostid(3), hostname(5), machine-info(5), os-release(5), sd-id128(3), sd_id128_get_machine(3), systemd-
       firstboot(1)

NOTES
	1. Safely Building Images
	   https://systemd.io/BUILDING_IMAGES

	2. RFC 4122
	   https://tools.ietf.org/html/rfc4122

systemd 255																	 MACHINE-ID(5)
