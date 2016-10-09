Summary:	Another System Definition Facility - package format for Common Lisp libraries
Summary(pl.UTF-8):	Another System Definition Facility - format pakietów bibliotek Common Lispa
Name:		common-lisp-asdf
Version:	20101028
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/cl-asdf/cl-asdf-%{version}.tar.bz2/f258de374780dcf5ad3ffeff422047ff/cl-asdf-%{version}.tar.bz2
# Source0-md5:	f258de374780dcf5ad3ffeff422047ff
Patch0:		%{name}-texinfo5.patch
URL:		http://www.cliki.net/asdf
BuildRequires:	texinfo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Another System Definition Facility (asdf) is a package format for
Common Lisp libraries.

%description -l pl.UTF-8
Another System Definition Facility (asdf) to format pakietów dla
bibliotek Common Lispa.

%prep
%setup -q -n asdf
%patch0 -p1

%build
%{__make} -C doc -j1 asdf.html manual-html

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/common-lisp/source/cl-asdf

cp -p asdf.lisp $RPM_BUILD_ROOT%{_datadir}/common-lisp/source/cl-asdf
cp -p wild-modules.lisp $RPM_BUILD_ROOT%{_datadir}/common-lisp/source/cl-asdf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/asdf
%dir %{_datadir}/common-lisp
%dir %{_datadir}/common-lisp/source
%{_datadir}/common-lisp/source/cl-asdf
