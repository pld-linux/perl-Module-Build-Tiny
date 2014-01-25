#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Module
%define		pnam	Build-Tiny
%include	/usr/lib/rpm/macros.perl
Summary:	Module::Build::Tiny - A tiny replacement for Module::Build
#Summary(pl.UTF-8):	
Name:		perl-Module-Build-Tiny
Version:	0.034
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	31efb75e0e535566c70551b46d981f7e
URL:		http://search.cpan.org/dist/Module-Build-Tiny/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-ExtUtils-Config >= 0.003
BuildRequires:	perl-ExtUtils-Helpers >= 0.020
BuildRequires:	perl-ExtUtils-InstallPaths >= 0.002
BuildRequires:	perl-Test-Harness >= 3.30
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Many Perl distributions use a Build.PL file instead of a Makefile.PL
file to drive distribution configuration, build, test and
installation. Traditionally, Build.PL uses Module::Build as
the underlying build system. This module provides a simple,
lightweight, drop-in replacement.

Whereas Module::Build has over 6,700 lines of code; this module has
less than 120, yet supports the features needed by most distributions.

Your .pm and .pod files must be in lib/.  Any executables must be in
script/.  Test files must be in t/. Dist sharedirs must be in share/.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__sed} -i -e 's/.*in blib is readonly.*/#&/g' t/simple.t

%build
%{__perl} Build.PL \
	--installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	--destdir=$RPM_BUILD_ROOT \
	--create_packlist=0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%dir %{perl_vendorlib}/Module/Build
%{perl_vendorlib}/Module/Build/Tiny.pm
%{_mandir}/man3/*
