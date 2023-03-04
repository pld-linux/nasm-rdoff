Summary:	Tools for the RDOFF binary format, sometimes used with NASM
Summary(pl.UTF-8):	Narzędzia do formatu binarnego RDOFF, czasem używane z NASM-em
Summary(ru.UTF-8):	Инструменты для бинарного формата RDOFF
Summary(uk.UTF-8):	Інструменти для бінарного формату RDOFF
Name:		nasm-rdoff
# nasm 2.16 dropped rdoff format support
Version:	2.15.05
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	https://www.nasm.us/pub/nasm/releasebuilds/%{version}/nasm-%{version}.tar.xz
# Source0-md5:	1c9802446d7341c41c21eb98c7859064
URL:		https://www.nasm.us/
BuildRequires:	perl-base
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for the operating-system independent RDOFF binary format, which
is sometimes used with the Netwide Assembler (NASM). These tools
include linker, library manager, loader, and information dump.

%description -l pl.UTF-8
Narzędzia do niezależnego od systemu operacyjnego formatu binarnego
RDOFF, czasem używanego z programem NASM (Netwide Assembler). Te
narzędzia zawierają linker, zarządcę bibliotek, loader oraz narzędzie
do zrzucania informacji.

%description -l ru.UTF-8
Инструменты для независимого от операционной системы бинарного формата
RDOFF, который иногда используют с NASM. Эти инструменты включают
редактор связей, библиотечный менеджер, загрузчик и программу выдачи
информационнного дампа.

%description -l uk.UTF-8
Інструменти для незалежного від операційної системи бінарного формату
RDOFF, котрий іноді використовують з NASM. Ці інструменти включають
редактор зв'язків, бібліотечний менеджер, завантажувач та програму
видачі інформаційного дампу.

%prep
%setup -q -n nasm-%{version}

%build
%configure

%{__make} -j1 rdf

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install_rdf \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoff/README
%attr(755,root,root) %{_bindir}/ldrdf
%attr(755,root,root) %{_bindir}/rdf2bin
%attr(755,root,root) %{_bindir}/rdf2com
%attr(755,root,root) %{_bindir}/rdf2ihx
%attr(755,root,root) %{_bindir}/rdf2ith
%attr(755,root,root) %{_bindir}/rdf2srec
%attr(755,root,root) %{_bindir}/rdfdump
%attr(755,root,root) %{_bindir}/rdflib
%attr(755,root,root) %{_bindir}/rdx
%{_mandir}/man1/ldrdf.1*
%{_mandir}/man1/rdf2bin.1*
%{_mandir}/man1/rdf2com.1*
%{_mandir}/man1/rdf2ihx.1*
%{_mandir}/man1/rdf2ith.1*
%{_mandir}/man1/rdf2srec.1*
%{_mandir}/man1/rdfdump.1*
%{_mandir}/man1/rdflib.1*
%{_mandir}/man1/rdx.1*
