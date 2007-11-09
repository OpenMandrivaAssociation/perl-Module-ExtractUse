%define module  Module-ExtractUse
%define name    perl-%{module}
%define version 0.20
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Find out what modules are used 
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Module/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Pod::Strip)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description 
Module::ExtractUse is basically a Parse::RecDescent grammar to parse Perl code.
It tries very hard to find all modules (whether pragmas, Core, or from CPAN)
used by the parsed code.

"Usage" is defined by either calling use or require

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Module
%{_mandir}/*/*


