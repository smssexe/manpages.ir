MAILCAP.ORDER(5)						     Order Mailcap Entries						      MAILCAP.ORDER(5)

NAME
       /etc/mailcap.order - the mailcap ordering specifications

DESCRIPTION
       The order of entries in the /etc/mailcap file can be altered by editing the /etc/mailcap.order file.  Each line of that file specifies a package and an
       optional mime type.  Mailcap entries that match will be placed in the order of this file.  Entries that don't match will be placed later.

   Example
	   mime-support:*/*
	   gv:application/postscript
	   netscape:text/html
	   less:text/*
	   emacs:text/*

       The  above would make any entries provided by the mime-support package (as found in the /usr/lib/mime/packages directory) take priority over everything
       else.  The gv package will be used over anything else when it comes to postscript documents.  Netscape will be used for any  html  documents  and  less
       will be used for any remaining text documents.  However, since neither netscape or less provide for editing documents, any edit or compose actions will
       fall through to the emacs rules.

       After modifying this file, be sure to run /usr/sbin/update-mime (as root) to propagate the changes into the /etc/mailcap file.

       Remember	 that  this files takes package names and not executable names.	 If you want to define rules that reference specific programs, the best way is
       to include them in ~/.mailcap or the user section of the /etc/mailcap file.

LIMITATIONS
       There is currently no way to break out a certain type from a wildcard rule.  If, for example, both xv and gimp were  to	specify	 "image/*"  rules,  it
       isn't possible to use xv for gif images but use gimp for jpeg images.

       Also,  I would like to add the ability to specify certain actions in the rules.	For example, if netscape were to have an edit rule but I wanted to use
       emacs for editing/creating html documents, I could place a line like

	 emacs:text/* action=edit|compose

       before the netscape entry.  The update-mime program would then spit out entries such that netscape view rule comes before the emacs view rule but  have
       the netscape edit rule comes after the emacs edit rule.

SEE ALSO
       mailcap(5) run-mailcap(1) update-mime(8)

AUTHOR
       The mailcap.order specification was written by Brian White <bcwhite@pobox.com>

Debian Project								 16th Aug 1998							      MAILCAP.ORDER(5)
