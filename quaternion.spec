%define oname Quaternion
%define beta %{nil}

Summary:	An IM client for the Matrix protocol
Name:		quaternion
Version:	0.0.96
Release:	0.beta3.1
License:	GPLv3+
Group:		Networking/Instant messaging
Url:		https://github.com/quotient-im/Quaternion
Source0:	https://github.com/quotient-im/Quaternion/archive/v%{version}/%{oname}-%{version}-beta3.tar.gz
Source1:	https://github.com/quotient-im/libQuotient/archive/0.8.0/libQuotient-0.8.0.tar.gz
BuildRequires:	qmake-qt6
BuildRequires:	cmake
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6LinguistTools)
#BuildRequires:	cmake(Qt5Keychain)
BuildRequires:	cmake(Qt6QuickControls2)

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
%autosetup -n %{oname}-%{version}-beta3 -a 1 -p1
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
