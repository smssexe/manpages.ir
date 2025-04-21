Error::Simple(3pm)					      User Contributed Perl Documentation					    Error::Simple(3pm)

NAME
       Error::Simple - the simple error sub-class of Error

VERSION
       version 0.17029

SYNOPSIS
	   use base 'Error::Simple';

DESCRIPTION
       The only purpose of this module is to allow one to say:

	   use base 'Error::Simple';

       and the only thing it does is "use" Error.pm. Refer to the documentation of Error for more information about Error::Simple.

METHODS
   Error::Simple->new($text [, $value])
       Constructs an Error::Simple with the text $text and the optional value $value.

   $err->stringify()
       Error::Simple overloads this method.

KNOWN BUGS
       None.

AUTHORS
       Shlomi Fish ( <http://www.shlomifish.org/> )

SEE ALSO
       Error

SUPPORT
   Websites
       The following websites have more information about this module, and may be of help to you. As always, in addition to those websites please use your
       favorite search engine to discover more resources.

       •   MetaCPAN

	   A modern, open-source CPAN search engine, useful to view POD in HTML format.

	   <https://metacpan.org/release/Error>

       •   Search CPAN

	   The default CPAN search engine, useful to view POD in HTML format.

	   <http://search.cpan.org/dist/Error>

       •   RT: CPAN's Bug Tracker

	   The RT ( Request Tracker ) website is the default bug/issue tracking system for CPAN.

	   <https://rt.cpan.org/Public/Dist/Display.html?Name=Error>

       •   CPAN Ratings

	   The CPAN Ratings is a website that allows community ratings and reviews of Perl modules.

	   <http://cpanratings.perl.org/d/Error>

       •   CPANTS

	   The CPANTS is a website that analyzes the Kwalitee ( code metrics ) of a distribution.

	   <http://cpants.cpanauthors.org/dist/Error>

       •   CPAN Testers

	   The CPAN Testers is a network of smoke testers who run automated tests on uploaded CPAN distributions.

	   <http://www.cpantesters.org/distro/E/Error>

       •   CPAN Testers Matrix

	   The CPAN Testers Matrix is a website that provides a visual overview of the test results for a distribution on various Perls/platforms.

	   <http://matrix.cpantesters.org/?dist=Error>

       •   CPAN Testers Dependencies

	   The CPAN Testers Dependencies is a website that shows a chart of the test results of all dependencies for a distribution.

	   <http://deps.cpantesters.org/?module=Error>

   Bugs / Feature Requests
       Please	 report	  any	bugs   or   feature   requests	 by   email   to   "bug-error	at   rt.cpan.org",   or	  through   the	  web	interface   at
       <https://rt.cpan.org/Public/Bug/Report.html?Queue=Error>. You will be automatically notified of any progress on the request by the system.

   Source Code
       The code is open to the world, and available for you to hack on. Please feel free to browse it and play with it, or whatever. If you want to contribute
       patches, please send me a diff or prod me to pull from your repository :)

       <https://github.com/shlomif/perl-error.pm>

	 git clone git://github.com/shlomif/perl-error.pm.git

AUTHOR
       Shlomi Fish ( http://www.shlomifish.org/ )

BUGS
       Please report any bugs or feature requests on the bugtracker website <https://github.com/shlomif/perl-error.pm/issues>

       When submitting a bug or request, please include a test-file or a patch to an existing test-file that illustrates the bug or desired feature.

COPYRIGHT AND LICENSE
       This software is copyright (c) 2020 by Shlomi Fish ( http://www.shlomifish.org/ ).

       This is free software; you can redistribute it and/or modify it under the same terms as the Perl 5 programming language system itself.

perl v5.36.0								  2022-10-14							    Error::Simple(3pm)
