Summary: Utilities for manipulating Macintosh file formats.
Name: macutils
Version: 2.0b3
Release: 12
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
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

%{__make} BINDIR=$RPM_BUILD_ROOT/usr/bin install
cp man/* $RPM_BUILD_ROOT/usr/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/bin/macunpack
/usr/bin/hexbin
/usr/bin/macsave
/usr/bin/macstream
/usr/bin/binhex
/usr/bin/tomac
/usr/bin/frommac
/usr/man/man1/binhex.1
/usr/man/man1/frommac.1
/usr/man/man1/hexbin.1
/usr/man/man1/macsave.1
/usr/man/man1/macstream.1
/usr/man/man1/macunpack.1
/usr/man/man1/macutil.1
/usr/man/man1/tomac.1
