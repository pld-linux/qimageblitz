Summary:	qimageblitz
Summary(pl.UTF-8):	qimageblitz
Name:		qimageblitz
Version:	0.0.4
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qimageblitz/%{name}-%{version}.tar.bz2
# Source0-md5:	cb87c7f1c0455e8984ee4830f1e749cf
URL:		http://sourceforge.net/project/showfiles.php?group_id=202856
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kde4-kdelibs-devel >= 4.0.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qimageblitz

%description -l pl.UTF-8
qimageblitz

%package devel
Summary:	%{name} header files
Summary(pl.UTF.8):	Pliki nagłówkowe %{name}
Group:		Development/Libraries
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
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
export KDEDIR=%{_prefix}
export QTDIR=%{_prefix}
export PATH=$QTDIR/bin:$KDEDIR/bin:%{_datadir}/qt4/bin:$PATH
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/blitztest
%attr(755,root,root) %{_libdir}/libqimageblitz.so.4.0.0
%attr(755,root,root) %{_libdir}/libqimageblitz.so.4
%{_pkgconfigdir}/qimageblitz.pc

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/qimageblitz
%{_includedir}/qimageblitz/blitzcpu.h
%{_includedir}/qimageblitz/qimageblitz.h
%{_includedir}/qimageblitz/qimageblitz_export.h
%attr(755,root,root) %{_libdir}/libqimageblitz.so
