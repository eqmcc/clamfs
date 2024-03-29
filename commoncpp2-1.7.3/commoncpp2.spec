%{!?release: %define release 0}
%{!?version: %define version 1.7.3}

%define _libname libcommoncpp2-1_7-0
%define _devname libcommoncpp2-devel

Name: commoncpp2
Summary: "commoncpp2" - A GNU package for creating portable C++ programs
Version: %{version}
Release: %{release}%{?dist}
License: RGPL v2 or later
Group: Development/Libraries
URL: http://www.gnu.org/software/commoncpp/commoncpp.html
Source0: ftp://ftp.gnu.org/gnu/commoncpp/commoncpp2-%{PACKAGE_VERSION}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gnutls
Requires: zlib
Requires: libstdc++
Prereq: /sbin/install-info
BuildRequires: gnutls-devel
BuildRequires: zlib-devel
BuildRequires: libstdc++-devel
BuildRequires: doxygen
BuildRequires: info

%description
GNU Common C++ offers portable abstraction of system services such as
threads and sockets.  GNU Common C++ also provides a threadsafe class
framework for strings, config file and XML parsing, and object
serialization.

%package -n %{_libname}
Group: System/Libraries
Summary: Runtime libraries for GNU Common C++ threading and sockets
Provides: %{name} = %{version}-%{release}

%package -n %{_devname}
Requires: %{_libname} = %{version}-%{release}
Requires: libxml2-devel
Requires: zlib-devel
Requires: libstdc++-devel
Requires(post,postun): info
Group: Development/Libraries
Summary: Headers and static link library for commoncpp2
Provides: %{name}-devel = %{version}-%{release}

%package doc
Requires: commoncpp2 = %{version}
Summary: Class documentation for GNU Common C++
Group: Documentation

%description -n %{_libname}
This package contains the runtime library needed by applications that use 
GNU Common C++.

%description -n %{_devname}
This package provides the header files, link libraries and documentation for
building GNU Common C++ applications.

%description doc
This includes doxygen generated class references for the GNU Common C++
library.

%prep
%setup
%build
%configure
%{__make} %{?_smp_mflags} CXXFLAGS="$RPM_OPT_FLAGS"

%install

%{__mkdir} -p %{buildroot}/%{_mandir}/man3
%makeinstall
%{__strip} %{buildroot}/%{_libdir}/lib*.so.*.*


%clean
%{__rm} -fr %{buildroot}

%files -n %{_libname}
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING.addendum NEWS README TODO ChangeLog
%{_libdir}/*.so.*

%files -n %{_devname}
%defattr(-,root,root,-)
%doc doc/html/*.html doc/html/*.*g*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/*.la
%dir %{_includedir}/cc++
%{_includedir}/cc++/*.h
%{_bindir}/*
%{_infodir}/commoncpp2.info*
%{_datadir}/aclocal/*.m4
%{_libdir}/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc doc/html/*

%post -n %{_libname} -p /sbin/ldconfig

%postun -n %{_libname} -p /sbin/ldconfig


