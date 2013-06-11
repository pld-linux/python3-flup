%define		_realname	flup
Summary:	Random collection of WSGI modules
Summary(pl.UTF-8):	Zestaw różnych modułów WSGI
Name:		python3-%{_realname}
Version:	1.0.3
%define	_snap	20120326
%define	_hash	cc23b715b120
Release:	0.%{_snap}
Group:		Development/Languages/Python
License:	X11/MIT
Source0:	http://hg.saddi.com/flup-py3.0/archive/cc23b715b120.tar.bz2/flup-%{version}_%{_snap}.tar.bz2
# Source0-md5:	9bf9ba90d9b8d112eff998286597c534
URL:		http://www.saddi.com/software/flup/
BuildRequires:	python3-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	python3-distribute
%pyrequires_eq  python3-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Python package is a random collection of WSGI modules.

%description -l pl.UTF-8
Ten pakiet Pythona jest zestawem różnych modułów WSGI

%prep
%setup -q -n flup-py3-0-%{_hash}

%build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{py3_sitescriptdir}/flup*
