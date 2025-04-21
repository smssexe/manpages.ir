Find(3pm)						      User Contributed Perl Documentation						     Find(3pm)

NAME
       Module::Find - Find and use installed modules in a (sub)category

SYNOPSIS
	 use Module::Find;

	 # use all modules in the Plugins/ directory
	 @found = usesub Mysoft::Plugins;

	 # use modules in all subdirectories
	 @found = useall Mysoft::Plugins;

	 # find all DBI::... modules
	 @found = findsubmod DBI;

	 # find anything in the CGI/ directory
	 @found = findallmod CGI;

	 # set your own search dirs (uses @INC otherwise)
	 setmoduledirs(@INC, @plugindirs, $appdir);

	 # not exported by default
	 use Module::Find qw(ignoresymlinks followsymlinks);

	 # ignore symlinks
	 ignoresymlinks();

	 # follow symlinks (default)
	 followsymlinks();

DESCRIPTION
       Module::Find lets you find and use modules in categories. This can be very useful for auto-detecting driver or plugin modules. You can differentiate
       between looking in the category itself or in all subcategories.

       If you want Module::Find to search in a certain directory on your harddisk (such as the plugins directory of your software installation), make sure you
       modify @INC before you call the Module::Find functions.

FUNCTIONS
       "setmoduledirs(@directories)"
	   Sets	 the  directories  to  be  searched  for  modules. If not set, Module::Find will use @INC. If you use this function, @INC will not be included
	   automatically, so add it if you want it. Set to undef to revert to default behaviour.

       "@found = findsubmod Module::Category"
	   Returns modules found in the Module/Category subdirectories of your perl installation. E.g. "findsubmod CGI" will return  "CGI::Session",  but  not
	   "CGI::Session::File" .

       "@found = findallmod Module::Category"
	   Returns  modules  found  in the Module/Category subdirectories of your perl installation. E.g. "findallmod CGI" will return "CGI::Session" and also
	   "CGI::Session::File" .

       "@found = usesub Module::Category"
	   Uses and returns modules found in the Module/Category subdirectories of your perl installation. E.g. "usesub CGI" will return  "CGI::Session",  but
	   not "CGI::Session::File" .

	   If any module dies during loading, usesub will also die at this point.

       "@found = useall Module::Category"
	   Uses	 and  returns  modules found in the Module/Category subdirectories of your perl installation. E.g. "useall CGI" will return "CGI::Session" and
	   also "CGI::Session::File" .

	   If any module dies during loading, useall will also die at this point.

       "ignoresymlinks()"
	   Do not follow symlinks. This function is not exported by default.

       "followsymlinks()"
	   Follow symlinks (default behaviour). This function is not exported by default.

HISTORY
       0.01, 2004-04-22
	       Original version; created by h2xs 1.22

       0.02, 2004-05-25
	       Added test modules that were left out in the first version. Thanks to Stuart Johnston for alerting me to this.

       0.03, 2004-06-18
	       Fixed a bug (non-localized $_) by declaring a loop variable in use functions.  Thanks to Stuart Johnston for alerting me to this and  providing
	       a fix.

	       Fixed non-platform compatibility by using File::Spec.  Thanks to brian d foy.

	       Added setmoduledirs and updated tests. Idea shamelessly stolen from ...errm... inspired by brian d foy.

       0.04, 2005-05-20
	       Added POD tests.

       0.05, 2005-11-30
	       Fixed issue with bugfix in PathTools-3.14.

       0.06, 2008-01-26
	       Module::Find now won't report duplicate modules several times anymore (thanks to Uwe Völker for the report and the patch)

       0.07, 2009-09-08
	       Fixed RT#38302: Module::Find now follows symlinks by default (can be disabled).

       0.08, 2009-09-08
	       Fixed RT#49511: Removed Mac OS X extended attributes from distribution

       0.09, 2010-02-26
	       Fixed RT#38302: Fixed META.yml generation (thanks very much to cpanservice for the help).

       0.10, 2010-02-26
	       Fixed RT#55010: Removed Unicode BOM from Find.pm.

       0.11, 2012-05-22
	       Fixed RT#74251: defined(@array) is deprecated under Perl 5.15.7.	 Thanks to Roman F, who contributed the implementation.

       0.12, 2014-02-08
	       Fixed RT#81077: useall fails in taint mode Thanks to Aran Deltac, who contributed the implementation and test.

	       Fixed RT#83596: Documentation doesn't describe behaviour if a module fails to load Clarified documentation for useall and usesub.

	       Fixed RT#62923: setmoduledirs(undef) doesn't reset to searching @INC Added more explicit tests.	Thanks to Colin Robertson for his input.

       0.13, 2015-03-09
	       This release contains two contributions from Moritz Lenz:

	       Link to Module::Pluggable and Class::Factory::Util in "SEE ALSO"

	       Align package name parsing with how perl does it (allowing single quotes as module separator)

	       Also, added a test for meta.yml

       0.14, 2019-12-25
	       A long overdue update. Thank you for the many contributions!

	       Fixed RT#99055: Removed file readability check (pull request contributed by Moritz Lenz)

	       Now supports @INC hooks (pull request contributed by Graham Knop)

	       Now filters out filenames starting with a dot (pull request contributed by Desmond Daignault)

	       Now uses strict (pull request contributed by Shlomi Fish)

	       Fixed RT#122016: test/ files show up in metacpan (bug report contributed by Karen Etheridge)

       0.15, 2019-12-26
	       Fixed  RT#127657 (bug report contributed by Karen Etheridge): Module::Find now uses @ModuleDirs (if specified) for loading modules. Previously,
	       when using setmoduledirs() to set an array of directories that did not contain @INC, Module::Find would find the modules	 correctly,  but  load
	       them from @INC.

       0.16, 2022-08-01
	       Fixes  an  issue	 where	symlink tests failed on systems that do not support creation of symlinks.  The issue appears on Windows systems due to
	       changed behaviour in "File::Find" described in perl5/issue #19995 <https://github.com/Perl/perl5/issues/19995> Symlink  tests  were  previously
	       skipped if "symlink()" is not available, and now also if creation of a symlink is not possible.

	       Fixes  issue  #9	 <https://github.com/crenz/Module-Find/issues/9>.  Note that on Windows system, the patch to "File::Find" from perl5/PR #20008
	       <https://github.com/Perl/perl5/pull/20008> will be required for proper operation.

DEVELOPMENT NOTES
       The development repository for this module is hosted on GitHub: <http://github.com/crenz/Module-Find/>. Please report any  bugs	by  opening  an	 issue
       there.

SEE ALSO
       perl, Module::Pluggable, Class::Factory::Util

AUTHOR
       Christian Renz, <crenz@web42.com>

COPYRIGHT AND LICENSE
       Copyright 2004-2022 by Christian Renz <crenz@web42.com>. All rights reserved.

       This library is free software; you can redistribute it and/or modify it under the same terms as Perl itself.

perl v5.36.0								  2022-10-22								     Find(3pm)
