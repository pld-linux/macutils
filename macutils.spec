Summary:	Utilities for manipulating Macintosh file formats
Summary(de):	Dienstprogramme zum Bearbeiten von Macintosh-Dateiformaten
Summary(es):	Utilitarios para manipulación de archivos en formato MacIntosh (Apple)
Summary(fr):	Utilitaires pour manipuler les fichiers au format Macintosh
Summary(pl):	Narzêdzia do obróbki plików z Macintosha
Summary(pt_BR):	Utilitários para manipulação de arquivos no formato MacIntosh (Apple)
Summary(tr):	Macintosh tipi dosyalarý iþlemek için araçlar
Name:		macutils
Version:	2.0b3
Release:	18
License:	distributable
Group:		Applications/File
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}.tar.gz
Patch0:		%{name}-misc.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The macutils package includes a set of utilities for manipulating
files that are commonly used by Macintosh machines. Macutils includes
utilities like binhex, hexbin, macunpack, etc.

Install macutils if you need to manipulate files that are commonly
used by Macintosh machines.

%description -l de
Dies ist eine Reihe von Dienstprogramme zum Bearbeiten von
Macintosh-Dateien. Enthalten sind u.a.: macunpack, hexbin und binhex.

%description -l es
Este es un conjunto de utilitarios para la manipulación de archivos
del Macintosh. Están incluidos utilitarios populares como macunpack,
hexbin y binhex .

%description -l fr
C'est un ensemble d'utilitaires pour manipuler des fichiers provenant
de Macintosh. Des utilitaires populaires comme macunpack, hexbin, et
binhex sont inclus.

%description -l pl
Pakiet macutils zawiera zestaw narzêdzi do obróbki plików powszechnie
u¿ywanych na Macintoshach. Zawiera binhex, hexbin, macunpack itp.

%description -l pt_BR
Este é um conjunto de utilitários para manipulação de arquivos do
Macintosh. Utilitários populares como macunpack, hexbin e binhex estão
incluídos.

%description -l tr
Bu pakette Macintosh dosyalarýnýn iþlenmesinde kullanýlabilecek
araçlar yer almaktadýr. Paket macunpack, hexbin ve binhex gibi yaygýn
olarak kullanýlan programlarý içermektedir.

%prep
%setup -q -n %{name}
%patch -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install macunpack/macunpack hexbin/hexbin mixed/{macsave,macstream} \
	binhex/binhex comm/{tomac,frommac} $RPM_BUILD_ROOT%{_bindir}
install man/* $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz doc/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
