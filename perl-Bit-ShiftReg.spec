#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Bit
%define	pnam	ShiftReg
Summary:	Bit::ShiftReg - bit shift registers with rotate / shift operations
Summary(pl):	Bit::ShiftReg - rejestry bitowego przesuwania z rotacj± / przesuniêciem
Name:		perl-Bit-ShiftReg
Version:	2.0
Release:	9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d8afa46eb43b252ae019c3193635d1e2
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bit::ShiftReg Perl module implements rotate left, rotate right, shift
left and shift right operations with carry flag for all C integer
types.

The results depend on the number of bits that the integer types
unsigned char, unsigned short, unsigned int and unsigned long have on
your machine.

%description -l pl
Modu³ Perla Bit::ShiftReg zawiera implementacjê operacji: rotacji w
lewo, rotacji w prawo, przesuniêcia w lewo i przesuniêcia w prawo ze
znacznikiem przeniesienia dla wszystkich typów ca³kowitych w C.

Wynik zale¿y od ilo¶ci bitów, jak± maj± typy: unsigned char, unsigned
short, unsigned int i unsigned long na danej architekturze.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

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
%{perl_vendorarch}/Bit/ShiftReg.pm
%dir %{perl_vendorarch}/auto/Bit/ShiftReg
%{perl_vendorarch}/auto/Bit/ShiftReg/ShiftReg.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Bit/ShiftReg/ShiftReg.so
%{_mandir}/man3/*
