%include	/usr/lib/rpm/macros.perl
%define		pdir	Bit
%define		pnam	ShiftReg
Summary:	Bit::ShiftReg perl module
Summary(pl):	Modu³ perla Bit::ShiftReg
Name:		perl-Bit-ShiftReg
Version:	2.0
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bit::ShiftReg - Bit Shift Registers with Rotate / Shift Operations.

%description -l pl
Modu³ perla Bit::ShiftReg.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitearch}/Bit/ShiftReg.pm
%dir %{perl_sitearch}/auto/Bit/ShiftReg
%{perl_sitearch}/auto/Bit/ShiftReg/ShiftReg.bs
%attr(755,root,root) %{perl_sitearch}/auto/Bit/ShiftReg/ShiftReg.so
%{_mandir}/man3/*
