%define oname Quaternion

Summary:	An IM client for the Matrix protocol
Name:		quaternion
Version:	0.0.9.3
Release:	1
License:	GPLv3+
Group:		Networking/Instant messaging
Url:		https://github.com/QMatrixClient/Quaternion
Source0:	https://github.com/QMatrixClient/Quaternion/archive/v%{version}/%{oname}-%{version}.tar.gz
Source1:	https://github.com/QMatrixClient/libqmatrixclient/archive/v0.4.2.1.%(echo %{version}|cut -d. -f4).tar.gz
BuildRequires:	qmake5
BuildRequires:	cmake
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5QuickWidgets)

%description
An IM client for the Matrix protocol.

%files
%doc COPYING README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/com.github.quaternion.appdata.xml
%{_iconsdir}/hicolor/*/apps/%{name}.*

%prep
%setup -qn %{oname}-%{version} -a 1
rmdir lib
mv libqmatrixclient-* lib

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DBUILD_STATIC_LIBS:BOOL=ON
%make

%install
%makeinstall_std -C build

# We don't need the -devel files -- they're only used internally
rm -rf %{buildroot}%{_includedir} \
	%{buildroot}%{_bindir}/qmc-example \
	%{buildroot}%{_libdir}/*.a \
	%{buildroot}%{_libdir}/cmake
