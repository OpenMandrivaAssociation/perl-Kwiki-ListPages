%define module	Kwiki-ListPages
%define name	perl-%{module}
%define version 0.11
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	List all Kwiki Pages
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Kwiki/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
License:	GPL
Group:		Development/Perl
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Kwiki)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module provides an indexed list of all the pages in a Kwiki wiki via a
button on the toolbar. At the top of the list is a navigation bar with letters
or numbers which have page entries associated with them.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Kwiki
%{_mandir}/*/*

