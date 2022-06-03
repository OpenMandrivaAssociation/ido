%define _empty_manifest_terminate_build 0

%define api 3-0.1
%define major 0

%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname %{name} -d

Summary:	Provides extra GTK+ menu items
Name:		ido
Version:	13.10.0
Release:	1
License:	LGPLv3+
Group:		System/Libraries
Url:		http://launchpad.net/ido
#Source0:	https://launchpad.net/ido/12.10/%{version}/+download/%{name}-%{version}.tar.gz
Source0:	https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/ido/13.10.0+17.04.20161028-0ubuntu3/ido_13.10.0+17.04.20161028.orig.tar.gz
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(gtk+-3.0)

%description
This library provdes extra gtk menu items for display in system indicators.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	IDO provides extra GTK+ menu items
Group:		System/Libraries
Obsoletes:	%{_lib}ido0 < 12.10.2

%description -n %{libname}
This library provdes extra gtk menu items for display in system indicators.

This package provides the shared libraries to be used by applications.

%files -n %{libname}
%doc COPYING
%{_libdir}/lib%{name}%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	IDO provides extra GTK+ menu items
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
This package provides the development files to build applications.

%files -n %{devname}
%dir %{_includedir}/libido%{api}
%{_includedir}/libido%{api}/libido/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

#----------------------------------------------------------------------------

%prep
%autosetup -c -p1

%build
export CFLAGS+=" -Wno-error"
%configure \
	--disable-static \
	--enable-gtk-doc

%make_build

%install
%make_install
