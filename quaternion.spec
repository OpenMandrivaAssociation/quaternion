%define oname Quaternion
%define beta %{nil}

Summary:	An IM client for the Matrix protocol
Name:		quaternion
Version:	0.0.96
Release:	1
License:	GPLv3+
Group:		Networking/Instant messaging
Url:		https://github.com/quotient-im/Quaternion
Source0:	https://github.com/quotient-im/Quaternion/archive/v%{version}/%{oname}-%{version}.tar.gz
Source1:	https://github.com/quotient-im/libQuotient/archive/0.8.1.2/libQuotient-0.8.1.2.tar.gz
BuildRequires:	qmake-qt6
BuildRequires:	cmake
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Network)
BuildRequires:  cmake(Olm)
BuildRequires:  cmake(QtOlm)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Keychain)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:  pkgconfig(OpenSSL)
BuildRequires:	cmake(VulkanHeaders)
BuildRequires:	pkgconfig(xkbcommon-x11)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	qt6-qtmultimedia-gstreamer
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:	qt6-qtbase-sql-postgresql
BuildRequires:	qt6-qtbase-sql-odbc
BuildRequires:	qt6-qtbase-sql-mariadb
BuildRequires:	qt6-qtbase-sql-firebird

%description
An IM client for the Matrix protocol.

%files
%doc README.md
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
export CC=gcc
export CXX=g++
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
