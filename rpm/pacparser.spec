# Spec file for pacparser
 
%define name        pacparser
%define release     1
%define version     1.3.7
 
Summary:        pacparser
License:        LGPL
Name:           %{name}
Version:        %{version}
Release:        %{release}
Source:         %{name}-%{version}.tar.gz
Prefix:         /usr
Group:          Development/Tools
 
%description
pacparser is a library to parse proxy auto-config (PAC) files.
 
%prep
%setup -q
 
%build
cd src
make
 
%install
cd src
make install DESTDIR=$RPM_BUILD_ROOT

%post
/usr/sbin/ldconfig

%postun
/usr/sbin/ldconfig

%files
%defattr(-,root,root)
/usr/bin/pactester
/usr/include/pacparser.h
/usr/lib/libpacparser.so
/usr/lib/libpacparser.so.1

%docdir /usr/share/man
/usr/share/man

%docdir /usr/share/doc/pacparser
/usr/share/doc/pacparser
