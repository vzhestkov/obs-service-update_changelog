# spec file for package obs-service-update_changelog

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define service update_changelog
%define branch master

Name:           obs-service-%{service}
Version:        0.5.8
Release:        0
Summary:        An OBS source service: Update spec file version
License:        GPL-2.0+
Group:          Development/Tools/Building
Url:            https://github.com/dincamihai/obs-service-%{service}/archive/%{branch}.tar.gz
Source:         https://github.com/dincamihai/obs-service-%{service}/archive/%{branch}.tar.gz
BuildArch:      noarch
BuildRequires:  %{python_module devel}
Requires:  %{python_module GitPython}
Requires:  %{python_module Jinja2}
Requires:  %{python_module py}
BuildRoot:      %{_tmppath}/%{name}-%{branch}

%description
This is a source service for openSUSE Build Service.

Service to update the changelog from git commits.

%prep
%setup -q -n %{name}-%{branch}

%build
%python_build

%install
%python_install
%makeinstall

%files
/usr/lib/obs
/usr/lib/obs/service
/usr/bin/update_changelog
%{python_sitelib}/updatechangelog
%{python3_sitelib}/updatechangelog
%{python_sitelib}/updatechangelog-*.egg-info
%{python3_sitelib}/updatechangelog-*.egg-info
/usr/lib/obs/service/update_changelog
/usr/lib/obs/service/update_changelog.service
 
%changelog
