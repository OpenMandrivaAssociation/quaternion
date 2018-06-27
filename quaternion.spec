%define oname Quaternion

Summary:	An IM client for the Matrix protocol
Name:		quaternion
Version:	0.0.9.2
Release:	1.%{git}.1
License:	GPLv3+
Group:		Networking/Instant messaging
Url:		https://github.com/QMatrixClient/Quaternion
Source0:	%{oname}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Widgets)

%description
An IM client for the Matrix protocol.

%files
%doc COPYING README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DBUILD_STATIC_LIBS:BOOL=ON
%make

%install
%makeinstall_std -C build

