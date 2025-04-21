SYSTEMD-INTEGRITYSETUP-GENERATOR(8)			       systemd-integritysetup-generator				   SYSTEMD-INTEGRITYSETUP-GENERATOR(8)

NAME
       systemd-integritysetup-generator - Unit generator for integrity protected block devices

SYNOPSIS
       /usr/lib/systemd/system-generators/systemd-integritysetup-generator

DESCRIPTION
       systemd-integritysetup-generator is a generator that translates /etc/integritytab entries into native systemd units early at boot. This will create
       systemd-integritysetup@.service(8) units as necessary.

       systemd-integritysetup-generator implements systemd.generator(7).

SEE ALSO
       systemd(1), systemd-integritysetup@.service(8), integritysetup(8)

systemd 255														   SYSTEMD-INTEGRITYSETUP-GENERATOR(8)
