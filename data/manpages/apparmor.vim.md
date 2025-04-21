APPARMOR.VIM(5)								   AppArmor							       APPARMOR.VIM(5)

NAME
       apparmor.vim - vim syntax highlighting file for AppArmor profiles

SYNOPSIS
       Your system may be configured to automatically use syntax highlighting for installed AppArmor policies. If not, you can enable syntax highlighting in a
       specific vim session by performing:

	:set syntax=apparmor

DESCRIPTION
       apparmor.vim provides syntax highlighting rules for the vim(1) text editor; the rules provide an easy visual method to inspect AppArmor profiles for
       syntax correctness and semantics.

       The colors indicate the relative severity of granting a specific set of privileges. Ranking access with colors is necessarily generic and vague, but it
       may help you understand your profiles better.

BUGS
       apparmor.vim does not properly detect dark versus light backgrounds.  Patches accepted. If you find any bugs, please report them at
       <https://gitlab.com/apparmor/apparmor/-/issues>.

SEE ALSO
       vim(1), apparmor(7), apparmor.d(5), aa_change_hat(2), and <https://wiki.apparmor.net>.

AppArmor 4.0.1								  2024-07-18							       APPARMOR.VIM(5)
