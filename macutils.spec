Summary: Utilities for manipulating Macintosh file formats.
Name: macutils
Version: 2.0b3
Release: 14
Copyright: disributable
Group: Applications/System
Source: ftp://sunsite.unc.edu/pub/Linux/utils/compress/macutils.tar.gz
Patch: macutils-misc.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The macutils package includes a set of utilities for manipulating
files that are commonly used by Macintosh machines.  Macutils includes
utilities like binhex, hexbin, macunpack, etc.

Install macutils if you need to manipulate files that are commonly used
by Macintosh machines.

%prep
%setup -q -n macutils
%patch -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install macunpack/macunpack		$RPM_BUILD_ROOT%{_bindir}
install hexbin/hexbin			$RPM_BUILD_ROOT%{_bindir}
install mixed/{macsave,macstream}	$RPM_BUILD_ROOT%{_bindir}
install binhex/binhex			$RPM_BUILD_ROOT%{_bindir}
install comm/{tomac,frommac}		$RPM_BUILD_ROOT%{_bindir}
cp man/* $RPM_BUILD_ROOT/%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
