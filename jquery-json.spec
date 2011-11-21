%define		plugin	json
Summary:	JSON plugin for jQuery, provides simple ways to convert to JSON and back again
Name:		jquery-%{plugin}
Version:	2.3
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	http://jquery-json.googlecode.com/files/jquery.json-%{version}.js
# Source0-md5:	761234abe4fbf042f3f8396ec4502e48
Source1:	http://jquery-json.googlecode.com/files/jquery.json-%{version}.min.js
# Source1-md5:	baa3ab64491201645de9021108f36824
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
cp -p %{SOURCE0} $RPM_BUILD_ROOT%{_appdir}/json-%{version}.js
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_appdir}/json-%{version}.min.js
ln -s json-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/json.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
