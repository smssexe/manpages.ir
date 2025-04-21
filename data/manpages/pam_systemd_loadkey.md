PAM_SYSTEMD_LOADKEY(8)						      pam_systemd_loadkey						PAM_SYSTEMD_LOADKEY(8)

NAME
       pam_systemd_loadkey - Read password from kernel keyring and set it as PAM authtok

SYNOPSIS
       pam_systemd_loadkey.so

DESCRIPTION
       pam_systemd_loadkey reads a NUL-separated password list from the kernel keyring, and sets the last password in the list as the PAM authtok.

       The password list is supposed to be stored in the "user" keyring of the root user, by an earlier call to systemd-ask-password(1) with --keyname=. You
       can pass the keyname to pam_systemd_loadkey via the keyname= option.

OPTIONS
       The following options are understood:

       keyname=
	   Takes a string argument which sets the keyname to read. The default is "cryptsetup", which is used by systemd-cryptsetup@.service(8) to store LUKS
	   passphrase during boot.

	   Added in version 255.

       debug
	   The module will log debugging information as it operates.

	   Added in version 255.

EXAMPLE
       This module is intended to be used when you use LUKS with a passphrase, enable autologin in the display manager, and want to unlock Gnome Keyring / KDE
       KWallet automatically. So in total, you only enter one password during boot.

       You need to set the password of your Gnome Keyring/KWallet to the same as your LUKS passphrase. Then add the following lines to your display manager's
       PAM config under /etc/pam.d/ (e.g.  sddm-autologin):

	   -auth       optional	   pam_systemd_loadkey.so
	   -session    optional	   pam_gnome_keyring.so auto_start
	   -session    optional	   pam_kwallet5.so auto_start

       And add the following lines to your display manager's systemd service file, so it can access root's keyring:

	   [Service]
	   KeyringMode=inherit

       In this setup, early during the boot process, systemd-cryptsetup@.service(8) will ask for the passphrase and store it in the kernel keyring with the
       keyname "cryptsetup". Then when the display manager does the autologin, pam_systemd_loadkey will read the passphrase from the kernel keyring, set it as
       the PAM authtok, and then pam_gnome_keyring and pam_kwallet5 will unlock with the same passphrase.

systemd 255																PAM_SYSTEMD_LOADKEY(8)
