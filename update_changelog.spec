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
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module py}
BuildRequires:  %{python_module GitPython}
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
%python3_install
%makeinstall

# install -d /usr/lib/obs/service
# ln -s %{buildroot}/update_changelog /usr/lib/obs/service
# ln -s %{buildroot}/update_changelog.service /usr/lib/obs/service


# %install
# 
# install -d /usr/lib/obs/service
# install -m 0755 update_changelog /usr/lib/obs/service
# install -m 0644 update_changelog.service /usr/lib/obs/service

# %files %{python-files}
# %defattr(-,root,root)
# %{python_sitelib}/update_changelog
# %{python_sitelib}/update_changelog/templates/header.txt
%files
/usr/bin/update_changelog
%{python_sitelib}/updatechangelog
%{python3_sitelib}/updatechangelog
%{python_sitelib}/updatechangelog-*.egg-info
%{python3_sitelib}/updatechangelog-*.egg-info
/usr/lib/obs/service/update_changelog
/usr/lib/obs/service/update_changelog.service
 
%changelog
