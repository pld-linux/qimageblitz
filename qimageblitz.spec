Summary:	Blitz KDE/Qt image filter library
Summary(pl.UTF-8):	Biblioteka filtrów obrazu Blitz dla KDE/Qt
Name:		qimageblitz
Version:	0.0.4
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/qimageblitz/%{name}-%{version}.tar.bz2
# Source0-md5:	cb87c7f1c0455e8984ee4830f1e749cf
URL:		http://sourceforge.net/projects/qimageblitz/
BuildRequires:	QtGui-devel
BuildRequires:	cmake
BuildRequires:	kde4-kdelibs-devel >= 4.0.0
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
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
Summary(pl.UTF.8):	Pliki nagłówkowe biblioteki Blitz
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files needed for build programs that use qimageblitz.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do tworzenia programów z użyciem
qimageblitz.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

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
%attr(755,root,root) %{_bindir}/blitztest
%attr(755,root,root) %{_libdir}/libqimageblitz.so.4.0.0
%attr(755,root,root) %ghost %{_libdir}/libqimageblitz.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqimageblitz.so
%dir %{_includedir}/qimageblitz
%{_includedir}/qimageblitz/blitzcpu.h
%{_includedir}/qimageblitz/qimageblitz.h
%{_includedir}/qimageblitz/qimageblitz_export.h
%{_pkgconfigdir}/qimageblitz.pc
