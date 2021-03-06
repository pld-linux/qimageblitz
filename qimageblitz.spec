Summary:	Blitz KDE/Qt image filter library
Summary(pl.UTF-8):	Biblioteka filtrów obrazu Blitz dla KDE/Qt
Name:		qimageblitz
Version:	0.0.6
Release:	5
License:	BSD
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/qimageblitz/%{name}-%{version}.tar.bz2
# Source0-md5:	0ae2f7d4e0876764a97ca73799f61df4
Patch0:		%{name}-noexecstack.patch
URL:		http://sourceforge.net/projects/qimageblitz/
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	cmake
BuildRequires:	qt4-build >= 4
BuildRequires:	qt4-qmake >= 4
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blitz is a graphical effect and filter library for KDE 4 that contains
many improvements over KDE 3.x's kdefx library including bugfixes,
memory and speed improvements, and MMX/SSE support.

%description -l pl.UTF-8
Blitz to biblioteka efektów i filtrów graficznych dla KDE 4
zawierająca wiele ulepszeń w stosunku do biblioteki kdefx z KDE 3.x, w
tym poprawki błędów, poprawę wydajności (pod względem wykorzystania
pamięci i szybkości działania) oraz obsługę MMX/SSE.

%package devel
Summary:	Header files for Blitz library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Blitz
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtGui-devel >= 4

%description devel
Header files needed for build programs that use qimageblitz.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do tworzenia programów z użyciem
qimageblitz.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING Changelog README.BLITZ
%attr(755,root,root) %{_bindir}/blitztest
%attr(755,root,root) %{_libdir}/libqimageblitz.so.4.0.0
%attr(755,root,root) %ghost %{_libdir}/libqimageblitz.so.4

%files devel
%defattr(644,root,root,755)
%doc README.PORTING
%attr(755,root,root) %{_libdir}/libqimageblitz.so
%dir %{_includedir}/qimageblitz
%{_includedir}/qimageblitz/blitzcpu.h
%{_includedir}/qimageblitz/qimageblitz.h
%{_includedir}/qimageblitz/qimageblitz_export.h
%{_pkgconfigdir}/qimageblitz.pc
