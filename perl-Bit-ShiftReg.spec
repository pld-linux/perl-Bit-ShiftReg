%define	pdir	Bit
%define	pnam	ShiftReg
%include	/usr/lib/rpm/macros.perl
Summary:	Bit-ShiftReg perl module
Summary(pl):	Modu� perla Bit-ShiftReg
Name:		perl-Bit-ShiftReg
Version:	2.0
Release:	6

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bit-ShiftReg - Bit Shift Registers with Rotate / Shift Operations.

%description -l pl
Modu� perla Bit-ShiftReg.

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
