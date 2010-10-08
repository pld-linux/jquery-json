%define		plugin	json
Summary:	JSON plugin for jQuery, provides simple ways to convert to JSON and back again
Name:		jquery-%{plugin}
Version:	2.2
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	http://jquery-json.googlecode.com/files/jquery.json-%{version}.min.js
# Source0-md5:	2d59ccdc20e736725bdbcb433e080ec0
URL:		http://code.google.com/p/jquery-json/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
JSON plugin for jQuery, provides simple ways to convert to JSON and
back again.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a %{SOURCE0} $RPM_BUILD_ROOT%{_appdir}/json.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
