%include	/usr/lib/rpm/macros.perl
Summary:	Bit-ShiftReg perl module
Summary(pl):	Modu³ perla Bit-ShiftReg
Name:		perl-Bit-ShiftReg
Version:	2.0
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Bit/Bit-ShiftReg-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bit-ShiftReg - Bit Shift Registers with Rotate / Shift Operations.

%description -l pl
Modu³ perla Bit-ShiftReg.

%prep
%setup -q -n Bit-ShiftReg-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Bit/ShiftReg.pm
%dir %{perl_sitearch}/auto/Bit/ShiftReg
%{perl_sitearch}/auto/Bit/ShiftReg/ShiftReg.bs
%attr(755,root,root) %{perl_sitearch}/auto/Bit/ShiftReg/ShiftReg.so
%{_mandir}/man3/*
