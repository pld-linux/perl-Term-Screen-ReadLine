#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Term
%define		pnam	Screen-ReadLine
Summary:	ReadLine extension for Term::Screen Perl module
Summary(pl.UTF-8):	Roszerzenie ReadLine dla modułu Perla Term::Screen
Name:		perl-Term-Screen-ReadLine
Version:	0.35
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	09756d236169edc8cfaecb58953fa69d
Patch0:		%{name}-test.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module extends Term::Screen with a readline() function. It also
makes it possible to use a 'single' Esc to escape instead of the
Term::Screen double Esc.

%description -l pl.UTF-8
Moduł rozszerzający Term::Screena o funkcję readline() oraz
pozwalający na użycie 'pojedynczego' Esc zamiast podwójnego w
Term::Screenie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Term/Screen/ReadLine.pm
%{_mandir}/man3/*
