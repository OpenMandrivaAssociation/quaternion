%define oname Quaternion
%define beta %{nil}

Summary:	An IM client for the Matrix protocol
Name:		quaternion
Version:	0.0.95.1
Release:	2
License:	GPLv3+
Group:		Networking/Instant messaging
Url:		https://github.com/quotient-im/Quaternion
Source0:	https://github.com/quotient-im/Quaternion/archive/v%{version}/%{oname}-%{version}.tar.gz
Source1:	https://github.com/quotient-im/libQuotient/archive/0.6.11/libQuotient-0.6.11.tar.gz
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
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5Keychain)
BuildRequires:	cmake(Qt5QuickControls2)

%description
An IM client for the Matrix protocol.

%files
%doc COPYING README.md
%{_bindir}/%{name}
%{_datadir}/applications/com.github.quaternion.desktop
%{_datadir}/metainfo/com.github.quaternion.appdata.xml
%{_iconsdir}/hicolor/*/apps/%{name}.*
%dir %{_datadir}/Quotient
%dir %{_datadir}/Quotient/quaternion
%{_datadir}/Quotient/quaternion/translations

%prep
%autosetup -n %{oname}-%{version} -a 1 -p1
rmdir lib
mv libQuotient-* lib

%build
%cmake \
	-DUSE_INTREE_LIBQMC=ON \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DBUILD_STATIC_LIBS:BOOL=ON

%make_build

%install
%make_install -C build

# We don't need the -devel files -- they're only used internally
rm -rf %{buildroot}%{_includedir} \
	%{buildroot}%{_bindir}/qmc-example \
	%{buildroot}%{_libdir}/*.a \
	%{buildroot}%{_libdir}/cmake \
	%{buildroot}%{_libdir}/pkgconfig \
	%{buildroot}%{_datadir}/ndk-modules \
	%{buildroot}%{_bindir}/quotest
