%define module  Sys-Virt
%define name	perl-%{module}
%define	modprefix Sys
%define version 0.1.1
%define release %mkrel 3

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Interface to libvirt virtual machine management API
License:    GPL or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
BuildRequires:  perl-devel
BuildRequires:  libvirt-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}


%description
Sys::Virt is an interface to libvirt virtual machine management API.
The Sys::Virt::Domain module represents a guest domain managed by
the virtual machine monitor.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make CFLAGS="%{optflags}"

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS CHANGES README LICENSE
%{perl_vendorarch}/Sys
%{perl_vendorarch}/auto/Sys
%{_mandir}/man3/Sys::Virt*3pm*


