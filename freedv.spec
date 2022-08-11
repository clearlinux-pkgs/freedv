#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : freedv
Version  : 1.7.0
Release  : 22
URL      : https://github.com/drowe67/freedv-gui/archive/v1.7.0/freedv-gui-1.7.0.tar.gz
Source0  : https://github.com/drowe67/freedv-gui/archive/v1.7.0/freedv-gui-1.7.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC-BY-4.0 LGPL-2.1
Requires: freedv-bin = %{version}-%{release}
Requires: freedv-data = %{version}-%{release}
Requires: freedv-license = %{version}-%{release}
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
BuildRequires : speexdsp-dev
BuildRequires : wxWidgets
BuildRequires : wxWidgets-dev
Patch1: 0001-Fix-check-for-LPCNet.patch

%description
# Building FreeDV GUI
This document describes how to build the FreeDV GUI program for various operating systems.  FreeDV GUI is developed on Ubuntu Linux, and then cross compiled for Windows using Fedora Linux (Fedora has great cross compiling support) and Docker.

%package bin
Summary: bin components for the freedv package.
Group: Binaries
Requires: freedv-data = %{version}-%{release}
Requires: freedv-license = %{version}-%{release}

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
%setup -q -n freedv-gui-1.7.0
cd %{_builddir}/freedv-gui-1.7.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644447335
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DUSE_INTERNAL_CODEC2=FALSE \
-DUSE_STATIC_DEPS=FALSE
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1644447335
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/freedv
cp %{_builddir}/freedv-gui-1.7.0/COPYING %{buildroot}/usr/share/package-licenses/freedv/0468d1cb0e40500dc98fa86141431a9f9e088c2b
cp %{_builddir}/freedv-gui-1.7.0/contrib/LICENSE %{buildroot}/usr/share/package-licenses/freedv/e9101bd4e253c0f7da54e8f581cf72322df10162
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/freedv

%files data
%defattr(-,root,root,-)
/usr/share/applications/freedv.desktop
/usr/share/freedv-gui/USER_MANUAL.html
/usr/share/freedv-gui/USER_MANUAL.md
/usr/share/freedv-gui/USER_MANUAL.pdf
/usr/share/freedv-gui/wav/all_2020.wav
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
