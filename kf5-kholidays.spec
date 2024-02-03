#
# Conditional build:
%bcond_with	tests		# build with tests
# TODO:
# - runtime Requires if any
%define		kdeframever	5.249.0
%define		qtver		5.15.2
%define		kfname		kholidays

Summary:	kholidays
Name:		kf5-%{kfname}
Version:	5.249.0
Release:	0.1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	56eff1e0a5dac9760c26776dda3443d1
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 3.16
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

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
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}6_qt --with-qm --all-name --with-kde


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}6_qt.lang
%defattr(644,root,root,755)
%{_libdir}/libKF6Holidays.so.6
%{_libdir}/libKF6Holidays.so.5.*.*
%dir %{_libdir}/qt6/qml/org/kde/kholidays
%{_libdir}/qt6/qml/org/kde/kholidays/libkholidaysdeclarativeplugin.so
%{_libdir}/qt6/qml/org/kde/kholidays/qmldir
%{_datadir}/qlogging-categories6/kholidays.categories
%{_libdir}/qt6/qml/org/kde/kholidays/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kholidays/kholidaysdeclarativeplugin.qmltypes


%files devel
%defattr(644,root,root,755)
%{_includedir}/KF6/KHolidays
%{_libdir}/cmake/KF6Holidays
%{_libdir}/libKF6Holidays.so
