#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : freedv
Version  : 1.9.0
Release  : 51
URL      : https://github.com/drowe67/freedv-gui/archive/v1.9.0/freedv-gui-1.9.0.tar.gz
Source0  : https://github.com/drowe67/freedv-gui/archive/v1.9.0/freedv-gui-1.9.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC-BY-4.0 LGPL-2.1
Requires: freedv-bin = %{version}-%{release}
Requires: freedv-data = %{version}-%{release}
Requires: freedv-license = %{version}-%{release}
Requires: wxWidgets
BuildRequires : LPCNet-dev
BuildRequires : buildreq-cmake
BuildRequires : codec2-dev
BuildRequires : extra-cmake-modules pkgconfig(libpulse)
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : hamlib-dev
BuildRequires : libsamplerate-dev
BuildRequires : libsndfile-dev
BuildRequires : pkgconfig(portaudio-2.0)
BuildRequires : socket.io-client-cpp-dev
BuildRequires : speexdsp-dev
BuildRequires : wxWidgets
BuildRequires : wxWidgets-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Fix-check-for-LPCNet.patch

%description
# Building FreeDV GUI
This document describes how to build the FreeDV GUI program for various operating systems.  FreeDV GUI is developed on Ubuntu Linux, and then cross compiled for Windows using Fedora Linux (Fedora has great cross compiling support) and Docker.

%package bin
Summary: bin components for the freedv package.
Group: Binaries
Requires: freedv-data = %{version}-%{release}
Requires: freedv-license = %{version}-%{release}
Requires: wxWidgets-lib

%description bin
bin components for the freedv package.


%package data
Summary: data components for the freedv package.
Group: Data

%description data
data components for the freedv package.


%package license
Summary: license components for the freedv package.
Group: Default

%description license
license components for the freedv package.


%prep
%setup -q -n freedv-gui-1.9.0
cd %{_builddir}/freedv-gui-1.9.0
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692113326
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake .. -DUSE_INTERNAL_CODEC2=FALSE \
-DUSE_STATIC_DEPS=FALSE
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DUSE_INTERNAL_CODEC2=FALSE \
-DUSE_STATIC_DEPS=FALSE
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :
cd ../clr-build-avx2;
make test || : || :

%install
export SOURCE_DATE_EPOCH=1692113326
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/freedv
cp %{_builddir}/freedv-gui-%{version}/COPYING %{buildroot}/usr/share/package-licenses/freedv/0468d1cb0e40500dc98fa86141431a9f9e088c2b || :
cp %{_builddir}/freedv-gui-%{version}/contrib/LICENSE %{buildroot}/usr/share/package-licenses/freedv/e9101bd4e253c0f7da54e8f581cf72322df10162 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/freedv
/usr/bin/freedv

%files data
%defattr(-,root,root,-)
/usr/share/applications/freedv.desktop
/usr/share/freedv-gui/USER_MANUAL.html
/usr/share/freedv-gui/USER_MANUAL.md
/usr/share/freedv-gui/USER_MANUAL.pdf
/usr/share/freedv-gui/wav/all_2020.wav
/usr/share/freedv-gui/wav/all_2020B.wav
/usr/share/freedv-gui/wav/all_2020B_mpp.wav
/usr/share/freedv-gui/wav/ve9qrp_1600.wav
/usr/share/freedv-gui/wav/ve9qrp_2400b.wav
/usr/share/freedv-gui/wav/ve9qrp_700c.wav
/usr/share/freedv-gui/wav/ve9qrp_700d.wav
/usr/share/freedv-gui/wav/ve9qrp_700e.wav
/usr/share/freedv-gui/wav/ve9qrp_800xa.wav
/usr/share/icons/hicolor/128x128/apps/freedv.png
/usr/share/icons/hicolor/256x256/apps/freedv.png
/usr/share/icons/hicolor/48x48/apps/freedv.png
/usr/share/icons/hicolor/64x64/apps/freedv.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/freedv/0468d1cb0e40500dc98fa86141431a9f9e088c2b
/usr/share/package-licenses/freedv/e9101bd4e253c0f7da54e8f581cf72322df10162
