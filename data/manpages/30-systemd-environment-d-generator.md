SYSTEMD-ENVIRONMENT-D-GENERATOR(8)				systemd-environment-d-generator				    SYSTEMD-ENVIRONMENT-D-GENERATOR(8)

NAME
       systemd-environment-d-generator, 30-systemd-environment-d-generator - Load variables specified by environment.d

SYNOPSIS
       /usr/lib/systemd/user-environment-generators/30-systemd-environment-d-generator

DESCRIPTION
       systemd-environment-d-generator is a systemd.environment-generator(7) that reads environment configuration specified by environment.d(5) configuration
       files and passes it to the systemd(1) user manager instance.

SEE ALSO
       systemd(1), systemctl(1), systemd.environment-generator(7), systemd.generator(7)

systemd 255														    SYSTEMD-ENVIRONMENT-D-GENERATOR(8)
