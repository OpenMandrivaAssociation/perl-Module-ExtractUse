%define upstream_name    Module-ExtractUse
Name:		perl-%{upstream_name}
Version:	0.345
Release:	2

Summary:	Find out what modules are used 

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/domm/Module-ExtractUse
Source0:	https://cpan.metacpan.org/authors/id/D/DO/DOMM/Module-ExtractUse-%{version}.tar.gz

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
%setup -q -n %{upstream_name}-%{version}

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



