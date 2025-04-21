securetty(5)							      File Formats Manual							  securetty(5)

NAME
       securetty - list of terminals on which root is allowed to login

DESCRIPTION
       The  file /etc/securetty contains the names of terminals (one per line, without leading /dev/) which are considered secure for the transmission of cer‐
       tain authentication tokens.

       It is used by (some versions of) login(1) to restrict the terminals on which root is allowed to login.  See login.defs(5) if you use the shadow suite.

       On PAM enabled systems, it is used for the same purpose by pam_securetty(8) to restrict the terminals on which empty passwords are accepted.

FILES
       /etc/securetty

SEE ALSO
       login(1), login.defs(5), pam_securetty(8)

Linux man-pages 6.7							  2023-10-31								  securetty(5)
