Summary:	Utilities for manipulating Macintosh file formats
Summary(de.UTF-8):	Dienstprogramme zum Bearbeiten von Macintosh-Dateiformaten
Summary(es.UTF-8):	Utilitarios para manipulación de archivos en formato MacIntosh (Apple)
Summary(fr.UTF-8):	Utilitaires pour manipuler les fichiers au format Macintosh
Summary(ja.UTF-8):	Macintosh のファイル形式を扱うユーティリティ
Summary(pl.UTF-8):	Narzędzia do obróbki plików z Macintosha
Summary(pt_BR.UTF-8):	Utilitários para manipulação de arquivos no formato MacIntosh (Apple)
Summary(tr.UTF-8):	Macintosh tipi dosyaları işlemek için araçlar
Name:		macutils
Version:	2.0b3
Release:	19
License:	distributable
Group:		Applications/File
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}.tar.gz
# Source0-md5:	4ff71b1634ea503398c33994458fbe40
Patch0:		%{name}-misc.patch
Patch1:		%{name}-gcc3.4.patch
Patch2:		%{name}-gcc4.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The macutils package includes a set of utilities for manipulating
files that are commonly used by Macintosh machines. Macutils includes
utilities like binhex, hexbin, macunpack, etc.

Install macutils if you need to manipulate files that are commonly
used by Macintosh machines.

%description -l de.UTF-8
Dies ist eine Reihe von Dienstprogramme zum Bearbeiten von
Macintosh-Dateien. Enthalten sind u.a.: macunpack, hexbin und binhex.

%description -l es.UTF-8
Este es un conjunto de utilitarios para la manipulación de archivos
del Macintosh. Están incluidos utilitarios populares como macunpack,
hexbin y binhex .

%description -l fr.UTF-8
C'est un ensemble d'utilitaires pour manipuler des fichiers provenant
de Macintosh. Des utilitaires populaires comme macunpack, hexbin, et
binhex sont inclus.

%description -l ja.UTF-8
macutils パッケージには, Macintosh で一般的に利用されている
ファイル形式を扱うユーティリティが収められています.
例えば binhex, hexbin, macunpack などが収録されています.
Macintosh のファイル形式を使う必要があれば macutils パッケージを
インストールして下さい.

%description -l pl.UTF-8
Pakiet macutils zawiera zestaw narzędzi do obróbki plików powszechnie
używanych na Macintoshach. Zawiera binhex, hexbin, macunpack itp.

%description -l pt_BR.UTF-8
Este é um conjunto de utilitários para manipulação de arquivos do
Macintosh. Utilitários populares como macunpack, hexbin e binhex estão
incluídos.

%description -l tr.UTF-8
Bu pakette Macintosh dosyalarının işlenmesinde kullanılabilecek
araçlar yer almaktadır. Paket macunpack, hexbin ve binhex gibi yaygın
olarak kullanılan programları içermektedir.

%prep
%setup -q -n %{name}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install macunpack/macunpack hexbin/hexbin mixed/{macsave,macstream} \
	binhex/binhex comm/{tomac,frommac} $RPM_BUILD_ROOT%{_bindir}
install man/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
