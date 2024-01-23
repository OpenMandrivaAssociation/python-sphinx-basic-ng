%define beta b2

Name:		python-sphinx-basic-ng
Version:	1.0.0
Release:	%{?beta:0.%{beta}.}1
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-basic-ng/sphinx_basic_ng-%{version}%{?beta:%{beta}}.tar.gz
Summary:	A modern skeleton for Sphinx themes.
URL:		https://pypi.org/project/sphinx-basic-ng/
License:	GPL
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
A modern skeleton for Sphinx themes.

%prep
%autosetup -p1 -n sphinx_basic_ng-%{version}%{?beta:%{beta}}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/sphinx_basic_ng
%{py_sitedir}/sphinx_basic_ng*.*-info
