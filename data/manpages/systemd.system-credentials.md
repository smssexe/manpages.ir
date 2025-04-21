SYSTEMD.SYSTEM-CREDENTIALS(7)					  systemd.system-credentials					 SYSTEMD.SYSTEM-CREDENTIALS(7)

NAME
       systemd.system-credentials - System Credentials

DESCRIPTION
       System and Service Credentials[1] are data objects that may be passed into booted systems or system services as they are invoked. They can be acquired
       from various external sources, and propagated into the system and from there into system services. Credentials may optionally be encrypted with a
       machine-specific key and/or locked to the local TPM2 device, and are only decrypted when the consuming service is invoked.

       System credentials may be used to provision and configure various aspects of the system. Depending on the consuming component credentials are only used
       on initial invocations or are needed for all invocations.

       Credentials may be used for any kind of data, binary or text, and may carry passwords, secrets, certificates, cryptographic key material, identity
       information, configuration, and more.

WELL KNOWN SYSTEM CREDENTIALS
       firstboot.keymap
	   The console key mapping to set (e.g.	 "de"). Read by systemd-firstboot(1), and only honoured if no console keymap has been configured before.

	   Added in version 252.

       firstboot.locale, firstboot.locale-messages
	   The system locale to set (e.g.  "de_DE.UTF-8"). Read by systemd-firstboot(1), and only honoured if no locale has been configured before.
	   firstboot.locale sets "LANG", while firstboot.locale-message sets "LC_MESSAGES".

	   Added in version 252.

       firstboot.timezone
	   The system timezone to set (e.g.  "Europe/Berlin"). Read by systemd-firstboot(1), and only honoured if no system timezone has been configured
	   before.

	   Added in version 252.

       login.issue
	   The data of this credential is written to /etc/issue.d/50-provision.conf, if the file doesn't exist yet.  agetty(8) reads this file and shows its
	   contents at the login prompt of terminal logins. See issue(5) for details.

	   Consumed by /usr/lib/tmpfiles.d/provision.conf, see tmpfiles.d(5).

	   Added in version 252.

       login.motd
	   The data of this credential is written to /etc/motd.d/50-provision.conf, if the file doesn't exist yet.  pam_motd(8) reads this file and shows its
	   contents as "message of the day" during terminal logins. See motd(5) for details.

	   Consumed by /usr/lib/tmpfiles.d/provision.conf, see tmpfiles.d(5).

	   Added in version 252.

       network.hosts
	   The data of this credential is written to /etc/hosts, if the file doesn't exist yet. See hosts(5) for details.

	   Consumed by /usr/lib/tmpfiles.d/provision.conf, see tmpfiles.d(5).

	   Added in version 252.

       network.dns, network.search_domains
	   DNS server information and search domains. Read by systemd-resolved.service(8).

	   Added in version 253.

       passwd.hashed-password.root, passwd.plaintext-password.root
	   May contain the password (either in UNIX hashed format, or in plaintext) for the root users. Read by both systemd-firstboot(1) and systemd-
	   sysusers(1), and only honoured if no root password has been configured before.

	   Added in version 252.

       passwd.shell.root
	   The path to the shell program (e.g.	"/bin/bash") for the root user. Read by both systemd-firstboot(1) and systemd-sysusers(1), and only honoured
	   if no root shell has been configured before.

	   Added in version 252.

       ssh.authorized_keys.root
	   The data of this credential is written to /root/.ssh/authorized_keys, if the file doesn't exist yet. This allows provisioning SSH access for the
	   system's root user.

	   Consumed by /usr/lib/tmpfiles.d/provision.conf, see tmpfiles.d(5).

	   Added in version 252.

       sysusers.extra
	   Additional sysusers.d(5) lines to process during boot.

	   Added in version 252.

       sysctl.extra
	   Additional sysctl.d(5) lines to process during boot.

	   Added in version 252.

       tmpfiles.extra
	   Additional tmpfiles.d(5) lines to process during boot.

	   Added in version 252.

       fstab.extra
	   Additional mounts to establish at boot. For details, see systemd-fstab-generator(8).

	   Added in version 254.

       vconsole.keymap, vconsole.keymap_toggle, vconsole.font, vconsole.font_map, vconsole.font_unimap
	   Console settings to apply, see systemd-vconsole-setup.service(8) for details.

	   Added in version 253.

       getty.ttys.serial, getty.ttys.container
	   Used for spawning additional login prompts, see systemd-getty-generator(8) for details.

	   Added in version 254.

       vmm.notify_socket
	   Configures an sd_notify(3) compatible AF_VSOCK socket the service manager will report status information, ready notification and exit status on.
	   For details see systemd(1).

	   Added in version 253.

       system.machine_id
	   Takes a 128bit ID to initialize the machine ID from (if it is not set yet). Interpreted by the service manager (PID 1). For details see systemd(1).

	   Added in version 254.

SEE ALSO
       systemd(1), kernel-command-line(7), smbios-type-11(7)

NOTES
	1. System and Service Credentials
	   https://systemd.io/CREDENTIALS

systemd 255															 SYSTEMD.SYSTEM-CREDENTIALS(7)
