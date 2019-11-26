# TODO:
# - runtime Requires if any
%define		kdeframever	5.62
%define		qtver		5.9.0
%define		kfname		kholidays

Summary:	kholidays
Name:		kf5-%{kfname}
Version:	5.62.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	8774e89e20901b7b7766fb7553ae46b8
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
kholidays.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}5_qt --with-qm --all-name --with-kde


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5_qt.lang
%defattr(644,root,root,755)
%{_libdir}/libKF5Holidays.so.5
%{_libdir}/libKF5Holidays.so.5.*.*
%dir %{_libdir}/qt5/qml/org/kde/kholidays
%{_libdir}/qt5/qml/org/kde/kholidays/libkholidaysdeclarativeplugin.so
%{_libdir}/qt5/qml/org/kde/kholidays/qmldir

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/kholidays_version.h
%{_includedir}/KF5/KHolidays
%{_libdir}/cmake/KF5Holidays
%{_libdir}/libKF5Holidays.so
%{_libdir}/qt5/mkspecs/modules/qt_KHolidays.pri
