Summary: Gearman Server and C Library
Name: gearmand
Version: 0.9
Release: 1
License: BSD
Group: System Environment/Libraries
BuildRequires: gcc-c++
URL: http://www.gearman.org/

Packager: Brian Aker <brian@tangent.org>

Source: http://launchpad.net/gearmand/trunk/%{version}/+download/gearmand-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Gearman provides a generic framework to farm out work to other machines, dispatching function calls to machines that are better suited to do work, to do work in parallel, to load balance processing, or to call functions between languages.

%prep
%setup -q

%configure

%build
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install  DESTDIR="%{buildroot}" AM_INSTALL_PROGRAM_FLAGS=""

%clean
%{__rm} -rf %{buildroot}

%files
%{_bindir}/gearman
%{_sbindir}/gearmand
%{_includedir}/libgearman/*.h
%{_libdir}/libgearman.a
%{_libdir}/libgearman.la
%{_libdir}/libgearman.so
%{_libdir}/libgearman.so.*
%{_libdir}/pkgconfig/gearmand.pc
%{_mandir}/man1/gear*
%{_mandir}/man3/gear*
%{_mandir}/man8/gear*


%changelog
* Wed Jan 7 2009 Brian Aker <brian@tangent.org> - 0.1-1
- Initial package
