Summary:	Library for accessing smart cards
Summary(pl.UTF-8):	Biblioteka do dostępu do kart procesorowych
Name:		smartcardpp
Version:	0.3.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: http://code.google.com/p/esteid/downloads/list
Source0:	http://esteid.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	c6172387475982393d02314f389f3513
URL:		http://code.google.com/p/esteid/
BuildRequires:	cmake >= 2.6
BuildRequires:	libstdc++-devel
BuildRequires:	pcsc-lite-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
smartcardpp is a set of C++ classes to manage smart card
communications and implement basic command primitives.

%description -l pl.UTF-8
smartcardpp to zbiór klas C++ pozwalających na zarządzanie
komunikacją z kartami procesorowymi oraz implementujących podstawowe
polecenia.

%package devel
Summary:	Header files for smartcardpp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki smartcardpp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	pcsc-lite-devel

%description devel
This package contains header files for developing applications that
use smartcardpp library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę smartcardpp.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS
%attr(755,root,root) %{_bindir}/card-test
%attr(755,root,root) %{_libdir}/libsmartcardpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmartcardpp.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmartcardpp.so
%{_includedir}/smartcardpp
%{_pkgconfigdir}/smartcardpp.pc
