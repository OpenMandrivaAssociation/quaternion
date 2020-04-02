%define oname Quaternion

Summary:	An IM client for the Matrix protocol
Name:		quaternion
Version:	0.0.9.4e
Release:	1
License:	GPLv3+
Group:		Networking/Instant messaging
Url:		https://github.com/QMatrixClient/Quaternion
Source0:	https://github.com/QMatrixClient/Quaternion/archive/v%{version}/%{oname}-%{version}.tar.gz
Source1:	https://github.com/quotient-im/libQuotient/archive/0.5.3.2/libQuotient-0.5.3.2.tar.gz
BuildRequires:	qmake5
BuildRequires:	cmake
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	cmake(Qt5LinguistTools)

%description
An IM client for the Matrix protocol.

%files
%doc COPYING README.md
%{_bindir}/%{name}
%{_datadir}/applications/com.github.quaternion.desktop
%{_datadir}/metainfo/com.github.quaternion.appdata.xml
%{_iconsdir}/hicolor/*/apps/%{name}.*

#QMatrixClient files. Keep it until provide QMatrixClient lib as submodule. In future make it as separate package.
%{_datadir}/QMatrixClient/quaternion/translations/quaternion*

%prep
%setup -qn %{oname}-%{version} -a 1
rmdir lib
mv libQuotient-* lib

%build
%cmake \
	-DUSE_INTREE_LIBQMC=1 \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DBUILD_STATIC_LIBS:BOOL=ON
%make_build

%install
%make_install -C build

# We don't need the -devel files -- they're only used internally
rm -rf %{buildroot}%{_includedir} \
	%{buildroot}%{_bindir}/qmc-example \
	%{buildroot}%{_libdir}/*.a \
	%{buildroot}%{_libdir}/cmake
