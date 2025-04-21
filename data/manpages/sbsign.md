SBSIGN(1)								 User Commands								     SBSIGN(1)

NAME
       sbsign - UEFI secure boot signing tool

SYNOPSIS
       sbsign [options] --key <keyfile> --cert <certfile> <efi-boot-image>

DESCRIPTION
       Sign an EFI boot image for use with secure boot.

OPTIONS
       --engine <eng>
	      use the specified engine to load the key

       --key <keyfile>
	      signing key (PEM-encoded RSA private key)

       --cert <certfile>
	      certificate (x509 certificate)

       --addcert <addcertfile> additional intermediate certificates in a file

       --detached
	      write a detached signature, instead of a signed binary

       --output <file>
	      write signed data to <file> (default <efi-boot-image>.signed, or <efi-boot-image>.pk7 for detached signatures)

sbsign 0.9.4								  April 2024								     SBSIGN(1)
