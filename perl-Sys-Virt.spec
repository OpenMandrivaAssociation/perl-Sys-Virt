%define upstream_name    Sys-Virt
%define upstream_version 0.2.3

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Interface to libvirt virtual machine management API
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Sys/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  libvirt-devel
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl-devel
BuildRequires:  xen-devel

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}


%description
Sys::Virt is an interface to libvirt virtual machine management API.
The Sys::Virt::Domain module represents a guest domain managed by
the virtual machine monitor.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
