%define module  Sys-Virt
%define name	perl-%{module}
%define	modprefix Sys

%define version 0.1.0
%define release %mkrel 2

Summary: Interface to libvirt virtual machine management API
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
License: GPL or Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/%{module}/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel libvirt-devel


%description
Sys::Virt is an interface to libvirt virtual machine management API.
The Sys::Virt::Domain module represents a guest domain managed by
the virtual machine monitor.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorarch}/Sys/Virt.pm
%dir %{perl_vendorarch}/Sys/Virt
%{perl_vendorarch}/Sys/Virt/*.pm
%dir %{perl_vendorarch}/auto/Sys/Virt
%{perl_vendorarch}/auto/Sys/Virt/Virt.so
%{_mandir}/man3/Sys::Virt*3pm*


