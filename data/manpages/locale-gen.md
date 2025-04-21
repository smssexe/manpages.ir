LOCALE-GEN(8)							    System Manager's Manual							 LOCALE-GEN(8)

NAME
       locale-gen — generate localisation files from templates

SYNOPSIS
       locale-gen [--keep-existing]

DESCRIPTION
       As  compiled  locales are large, only templates are distributed in the default locales package, and only the desired locales are compiled on the target
       system.

       After selecting the locales into /etc/locale.gen (via dpkg package configuration, for example), locale-gen is run to compile them via localedef(1).

OPTIONS
       --keep-existing	Do not remove /usr/lib/locale/locale-archive, only compiling new locales.

FILES
       /etc/locale.gen	Whitespace-separated newline-delimited locale charset list of locales to build with # start-of-line comments.
       /var/lib/locales/supported.d  A directory containing locale.gen snippets provided by language-pack packages.  Do not edit these manually, they will  be
				     overwritten on package upgrades.

SEE ALSO
       locale(1), localedef(1), locale.gen(5)

       /usr/share/i18n/SUPPORTED (/usr/local/share/i18n/SUPPORTED) — list of all supported locales on the current system.

       The locales-all package, which contains all supported locales in compiled form.

Debian									  May 5, 2022								 LOCALE-GEN(8)
