Summary:	Utilities for manipulating Macintosh file formats
Summary(pl):	Narzêdzia do obróbki plików plików z Macintosha
Name:		macutils
Version:	2.0b3
Release:	14
License:	disributable
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}.tar.gz
Patch0:		%{name}-misc.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The macutils package includes a set of utilities for manipulating
files that are commonly used by Macintosh machines. Macutils includes
utilities like binhex, hexbin, macunpack, etc.

Install macutils if you need to manipulate files that are commonly
used by Macintosh machines.

%description -l pl
Pakiet macutils zawiera zestaw narzêdzi do obróbki plików powszechnie
u¿ywanych na Macintoshach. Zawiera binhex, hexbin, macunpack itp.

%prep
%setup -q -n %{name}
%patch -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install macunpack/macunpack		$RPM_BUILD_ROOT%{_bindir}
install hexbin/hexbin			$RPM_BUILD_ROOT%{_bindir}
install mixed/{macsave,macstream}	$RPM_BUILD_ROOT%{_bindir}
install binhex/binhex			$RPM_BUILD_ROOT%{_bindir}
install comm/{tomac,frommac}		$RPM_BUILD_ROOT%{_bindir}
install man/* $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz doc/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
