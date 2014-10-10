%define upstream_name	 Kwiki-ListPages
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	List all Kwiki Pages
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Kwiki/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Kwiki)
BuildArch:	noarch

%description
This module provides an indexed list of all the pages in a Kwiki wiki via a
button on the toolbar. At the top of the list is a navigation bar with letters
or numbers which have page entries associated with them.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Kwiki
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 403379
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.11-6mdv2009.0
+ Revision: 257452
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.11-5mdv2009.0
+ Revision: 245421
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.11-3mdv2008.1
+ Revision: 122820
- kill re-definition of %%buildroot on Pixel's request


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-3mdv2007.0
- Rebuild

* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.11-2mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL

* Thu Jan 19 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdk
- first mandriva release

