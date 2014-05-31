#sbs-git:slp/pkgs/l/libttssmt libttssmt 0.0.15 9c82c715d55cf32bb3d69112526145654ec2fbcc
%define _optdir	/opt
%define _appdir	%{_optdir}/apps



Name:       libttssmt
Summary:    Text To Speech smt plugin shared library
Version:    0.1.2
Release:    1
Group:      TO_BE/FILLED_IN
License:    Flora-1.1
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(tts)
BuildRequires:	pkgconfig(tts-engine)

provides : libsmt.so

%description
Description: Text To Speech smt plugin shared library


%prep
%setup -q

%if "%{_repository}" == "wearable"
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_PROFILE="wearable"
%else
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_PROFILE="mobile"
%endif

%build
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{name}-%{version}/LICENSE.Flora %{buildroot}/usr/share/license/%{name}

%files
%manifest libttssmt.manifest
%if "%{_repository}" == "wearable"
/etc/smack/accesses2.d/libttssmt.rule
%else
/etc/smack/accesses.d/libttssmt.rule
%endif
%defattr(-,root,root,-)
%{_libdir}/voice/tts/1.0/engine/*
/usr/share/voice/tts/smt_vdata/*
%{_libdir}/libsmt.so*
%{_libdir}/voice/tts/1.0/engine-info/ttssmt-info.xml
/usr/share/license/%{name}
