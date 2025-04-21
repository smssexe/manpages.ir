GNUPG(7)							     GNU Privacy Guard 2.4							      GNUPG(7)

NAME
       GnuPG - The GNU Privacy Guard suite of programs

DESCRIPTION
       GnuPG is a set of programs for public key encryption and digital signatures.  The program most users will want to use is the OpenPGP command line tool,
       named gpg.  gpgvis a stripped down version of gpg with no encryption functionality, used only to verify signatures against a trusted keyring.  gpgsm is
       the X.509/CMS (for S/MIME) counterpart of gpg. gpg-agent is a passphrase and private key daemon which may also emulate the ssh-agent.

SEE ALSO
       gpg(1), gpgv(1), gpgsm(1), gpg-agent(1), dirmngr(8), scdaemon(1)

       The full documentation for this tool is maintained as a Texinfo manual.	If GnuPG and the info program are properly installed at your site, the command

	 info gnupg

       should give you access to the complete manual including a menu structure and an index.

GnuPG 2.4.4								  2024-01-25								      GNUPG(7)
