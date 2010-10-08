Summary:	JSON plugin for jQuery, provides simple ways to convert to JSON and back again
Name:		jquery-json
Version:	2.2
Release:	0.1
License:	MIT
Group:		Applications/WWW
Source0:	http://jquery-json.googlecode.com/files/jquery.json-%{version}.min.js
# Source0-md5:	2d59ccdc20e736725bdbcb433e080ec0
URL:		http://code.google.com/p/jquery-json/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/jquery

%description
JSON plugin for jQuery, provides simple ways to convert to JSON and
back again.

%prep
%setup -qcT
cp -a %{SOURCE0} jquery.json.js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a jquery.json.js $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}/jquery.json.js
