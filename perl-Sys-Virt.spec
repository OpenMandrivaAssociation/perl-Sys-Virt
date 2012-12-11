%define	module	Sys-Virt
%define	upstream_version 0.9.9

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Interface to libvirt virtual machine management API
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	http://www.cpan.org/modules/by-module/Sys/%{module}-%{upstream_version}.tar.gz

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


%changelog
* Thu Feb 02 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.9.9-1
+ Revision: 770581
- new version
- fix license
- cleanups
- use pkgconfig() deps
- mass rebuild of perl extensions against perl 5.14.2

* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.8-1
+ Revision: 688829
- update to new version 0.2.8

* Fri Mar 04 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.2.6-1
+ Revision: 641663
- update to 0.2.6

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.2.4-1mdv2011.0
+ Revision: 562463
- update to 0.2.4

* Sat Jan 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.2.3-1mdv2011.0
+ Revision: 492159
- update to 0.2.3

* Tue Sep 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.2.2-1mdv2010.0
+ Revision: 442641
- update to 0.2.2

* Wed Aug 26 2009 Jérôme Quelin <jquelin@mandriva.org> 0.2.1-1mdv2010.0
+ Revision: 421389
- update to 0.2.1

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-1mdv2010.0
+ Revision: 370183
- update to new version 0.2.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Mon Feb 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.2-1mdv2008.1
+ Revision: 174676
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Sep 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-2mdv2008.0
+ Revision: 78769
- spec cleanup and ship documentation files

* Mon Apr 23 2007 Olivier Blin <blino@mandriva.org> 0.1.1-1mdv2008.0
+ Revision: 17258
- 0.1.1


(none)