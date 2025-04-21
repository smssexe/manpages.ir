SYSTEMD-TPM2-SETUP.SERVICE(8)					  systemd-tpm2-setup.service					 SYSTEMD-TPM2-SETUP.SERVICE(8)

NAME
       systemd-tpm2-setup.service, systemd-tpm2-setup-early.service, systemd-tpm2-setup - Set up the TPM2 Storage Root Key (SRK) at boot

SYNOPSIS
       systemd-tpm2-setup.service

       /usr/lib/systemd/systemd-tpm2-setup

DESCRIPTION
       systemd-tpm2-setup.service and systemd-tpm2-setup-early.service are services that generate the Storage Root Key (SRK) if it hasn't been generated yet,
       and stores it in the TPM.

       The services will store the public key of the SRK key pair in a PEM file in /run/systemd/tpm2-srk-public-key.pem and
       /var/lib/systemd/tpm2-srk-public-key.pem. It will also store it in TPM2B_PUBLIC format in /run/systemd/tpm2-srk-public-key.tpm2_public and
       /var/lib/systemd/tpm2-srk-public-key.tpm2b_public.

       systemd-tpm2-setup-early.service runs very early at boot (possibly in the initrd), and writes the SRK public key to /run/systemd/tpm2-srk-public-key.*
       (as /var/ is generally not accessible this early yet), while systemd-tpm2-setup.service runs during a later boot phase and saves the public key to
       /var/lib/systemd/tpm2-srk-public-key.*.

FILES
       /run/systemd/tpm2-srk-public-key.pem, /run/systemd/tpm2-srk-public-key.tpm2b_public
	   The SRK public key in PEM and TPM2B_PUBLIC format, written during early boot.

	   Added in version 255.

       /var/lib/systemd/tpm2-srk-public-key.pem, /var/lib/systemd/tpm2-srk-public-key.tpm2_public
	   The SRK public key in PEM and TPM2B_PUBLIC format, written during later boot (once /var/ is available).

	   Added in version 255.

SEE ALSO
       systemd(1)

systemd 255															 SYSTEMD-TPM2-SETUP.SERVICE(8)
