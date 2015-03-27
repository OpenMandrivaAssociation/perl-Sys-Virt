%define	module	Sys-Virt
%define upstream_version 1.2.1
Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Interface to libvirt virtual machine management API
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	http://www.cpan.org/modules/by-module/Sys/Sys-Virt-%{version}.tar.gz

BuildRequires:	pkgconfig(libvirt) >= 0.9.9
BuildRequires:	perl(XML::XPath)
BuildRequires:	perl-devel
BuildRequires:	xen-devel


%description
Sys::Virt is an interface to libvirt virtual machine management API.
The Sys::Virt::Domain module represents a guest domain managed by
the virtual machine monitor.

%prep
%setup -q -n %{module}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc AUTHORS README LICENSE
%{perl_vendorarch}/Sys
%{perl_vendorarch}/auto/Sys
%{_mandir}/man3/Sys::Virt*3pm*
