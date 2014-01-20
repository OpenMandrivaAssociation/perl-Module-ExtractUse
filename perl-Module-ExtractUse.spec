%define upstream_name    Module-ExtractUse
%define upstream_version 0.32

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Find out what modules are used 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/Module-ExtractUse-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-version
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(Parse::RecDescent)
BuildRequires:	perl(Pod::Strip)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch:	noarch

%description 
Module::ExtractUse is basically a Parse::RecDescent grammar to parse Perl code.
It tries very hard to find all modules (whether pragmas, Core, or from CPAN)
used by the parsed code.

"Usage" is defined by either calling use or require

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes README
%{perl_vendorlib}/Module
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2010.0
+ Revision: 403863
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.23-2mdv2009.0
+ Revision: 268617
- rebuild early 2009.0 package (before pixel changes)

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdv2009.0
+ Revision: 201861
- update to new version 0.23

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2008.1
+ Revision: 109508
- update to new version 0.22

* Fri Nov 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2008.1
+ Revision: 107233
- update to new version 0.20
- update to new version 0.20

* Thu May 03 2007 Michael Scherer <misc@mandriva.org> 0.19-1mdv2008.0
+ Revision: 21530
- update to 0.19


* Wed Nov 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-3mdv2007.0
+ Revision: 88340
- fix buildrequires
- fix buildrequires
- Import perl-Module-ExtractUse

* Tue Nov 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2007.1
- first mdv release


