%define _disable_ld_no_undefined 1
# im gonna pass on using the api in the libname for now
%define api 3-0.1
%define major 0

%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Provides extra GTK+ menu items
Name:		ido
Version:	0.3.4
Release:	1
License:	LGPLv2.1, LGPLv3
Url:		http://launchpad.net/ido
Group:		System/Libraries
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libutouch-geis)

%description
This library provdes extra gtk menu items for display in system indicators.

%package -n %{libname}
Summary:	IDO provides extra GTK+ menu items
Group:		System/Libraries

%description -n %{libname}
This library provdes extra gtk menu items for display in system indicators.

This package provides the shared libraries to be used by applications.

%package -n %{develname}
Summary:	IDO provides extra GTK+ menu items
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
This package provides the development files to build applications.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
  --disable-static \
  --enable-gtk-doc

%make

%install
%makeinstall_std
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%files -n %{libname}
%doc COPYING
%{_libdir}/*%{api}.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/libido%{api}
%{_includedir}/libido%{api}/libido/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so



%changelog
* Fri Apr 06 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.3.4-1
+ Revision: 789535
- removed unneeded patches
- new version 0.3.4
- added p2 to fix deprication in build
- imported package ido

