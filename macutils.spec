Summary:	Utilities for manipulating Macintosh file formats
Summary(de):	Dienstprogramme zum Bearbeiten von Macintosh-Dateiformaten
Summary(es):	Utilitarios para manipulaci�n de archivos en formato MacIntosh (Apple)
Summary(fr):	Utilitaires pour manipuler les fichiers au format Macintosh
Summary(ja):	Macintosh �Υե���������򰷤��桼�ƥ���ƥ�
Summary(pl):	Narz�dzia do obr�bki plik�w z Macintosha
Summary(pt_BR):	Utilit�rios para manipula��o de arquivos no formato MacIntosh (Apple)
Summary(tr):	Macintosh tipi dosyalar� i�lemek i�in ara�lar
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

%description -l de
Dies ist eine Reihe von Dienstprogramme zum Bearbeiten von
Macintosh-Dateien. Enthalten sind u.a.: macunpack, hexbin und binhex.

%description -l es
Este es un conjunto de utilitarios para la manipulaci�n de archivos
del Macintosh. Est�n incluidos utilitarios populares como macunpack,
hexbin y binhex .

%description -l fr
C'est un ensemble d'utilitaires pour manipuler des fichiers provenant
de Macintosh. Des utilitaires populaires comme macunpack, hexbin, et
binhex sont inclus.

%description -l ja
macutils �ѥå������ˤ�, Macintosh �ǰ���Ū�����Ѥ���Ƥ���
�ե���������򰷤��桼�ƥ���ƥ���������Ƥ��ޤ�.
�㤨�� binhex, hexbin, macunpack �ʤɤ���Ͽ����Ƥ��ޤ�.
Macintosh �Υե����������Ȥ�ɬ�פ������ macutils �ѥå�������
���󥹥ȡ��뤷�Ʋ�����.

%description -l pl
Pakiet macutils zawiera zestaw narz�dzi do obr�bki plik�w powszechnie
u�ywanych na Macintoshach. Zawiera binhex, hexbin, macunpack itp.

%description -l pt_BR
Este � um conjunto de utilit�rios para manipula��o de arquivos do
Macintosh. Utilit�rios populares como macunpack, hexbin e binhex est�o
inclu�dos.

%description -l tr
Bu pakette Macintosh dosyalar�n�n i�lenmesinde kullan�labilecek
ara�lar yer almaktad�r. Paket macunpack, hexbin ve binhex gibi yayg�n
olarak kullan�lan programlar� i�ermektedir.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
