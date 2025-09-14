#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Module
%define		pnam	Build-Tiny
Summary:	Module::Build::Tiny - A tiny replacement for Module::Build
Summary(pl.UTF-8):	Module::Build::Tiny - mały zamiennik systemu Module::Build
Name:		perl-Module-Build-Tiny
Version:	0.052
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	91e56a426d82dbf33761984e26ed8acb
URL:		https://metacpan.org/dist/Module-Build-Tiny
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl-ExtUtils-Config >= 0.003
BuildRequires:	perl-ExtUtils-Helpers >= 0.020
BuildRequires:	perl-ExtUtils-InstallPaths >= 0.002
BuildRequires:	perl-Getopt-Long >= 2.36
BuildRequires:	perl-JSON-PP >= 2
BuildRequires:	perl-Test-Simple >= 0.88
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

%description -l pl.UTF-8
Wiele pakietów perlowych wykorzystuje plik Build.PL zamiast pliku
Makefile.PL do sterowania konfiguracją, budowaniem, testowaniem i
instajacją. Tradycyjnie Build.PL w roli systemu budującego
wykorzystuje Module::Build; ten moduł dostarcza prosty, lekki
zamiennik.

O ile Module::Build ma ponad 6700 linii kodu, ten moduł ma mniej niż
120, a obsługuje funkcje wymaganych przez większość pakietów.

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
%doc Changes README Todo
%dir %{perl_vendorlib}/Module/Build
%{perl_vendorlib}/Module/Build/Tiny.pm
%{_mandir}/man3/Module::Build::Tiny.3pm*
