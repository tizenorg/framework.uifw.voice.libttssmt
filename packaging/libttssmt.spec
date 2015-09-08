%define _optdir	/opt
%define _appdir	%{_optdir}/apps



Name:       libttssmt
Summary:    Text To Speech smt plugin shared library
Version:    0.1.2
Release:    1
Group:      Graphics & UI Framework/Voice Framework
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

cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}

%build
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{name}-%{version}/LICENSE %{buildroot}/usr/share/license/%{name}

%files
%manifest libttssmt.manifest
/etc/smack/accesses.d/libttssmt.rule
%defattr(-,root,root,-)
%{_libdir}/voice/tts/1.0/engine/*
/usr/share/voice/tts/smt_vdata/*
%{_libdir}/libsmt.so*
%{_libdir}/voice/tts/1.0/engine-info/ttssmt-info.xml
/usr/share/license/%{name}
