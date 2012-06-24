Summary:	Bit-ShiftReg perl module
Summary(pl):	Modu� perla Bit-ShiftReg
Name:		perl-Bit-ShiftReg
Version:	2.0
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Bit/Bit-ShiftReg-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Bit-ShiftReg - Bit Shift Registers with Rotate / Shift Operations.

%description -l pl
Modu� perla Bit-ShiftReg

%prep
%setup -q -n Bit-ShiftReg-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Bit/ShiftReg/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Bit/ShiftReg
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitearch}/Bit/ShiftReg.pm

%dir %{perl_sitearch}/auto/Bit/ShiftReg
%{perl_sitearch}/auto/Bit/ShiftReg/.packlist
%{perl_sitearch}/auto/Bit/ShiftReg/ShiftReg.bs
%attr(755,root,root) %{perl_sitearch}/auto/Bit/ShiftReg/ShiftReg.so

%{_mandir}/man3/*
