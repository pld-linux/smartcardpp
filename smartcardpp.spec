Summary:	Library for accessing smart cards
Name:		smartcardpp
Version:	0.2.0
Release:	1
License:	BSD
Group:		Libraries
URL:		http://code.google.com/p/esteid/
Source0:	http://esteid.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	4256e9d401864ce60f5d18de606c228f
BuildRequires:	cmake
BuildRequires:	pcsc-lite-devel
BuildRequires:	rpmbuild(macros) >= 1.577
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
smartcardpp is a set of C++ classes to manage smart card
communications and implement basic command primitives.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pcsc-lite-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

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
%doc NEWS
%attr(755,root,root) %{_bindir}/card-test
%attr(755,root,root) %{_libdir}/libsmartcardpp.so.*.*.*
%ghost %attr(755,root,root) %{_libdir}/libsmartcardpp.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmartcardpp.so
%{_libdir}/libsmartcardpp.so
%{_includedir}/smartcardpp
