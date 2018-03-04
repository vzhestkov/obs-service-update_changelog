# spec file for package obs-service-update_changelog

%define service update_changelog

Name:           obs-service-%{service}
Version:        0.5.8
Release:        0
Summary:        An OBS source service: Update spec file version
License:        GPL-2.0+
Group:          Development/Tools/Building
Url:            https://github.com/dincamihai/obs-service-%{service}
Source:         master.tar.gz
BuildArch:      noarch
Requires:       python3

%description
This is a source service for openSUSE Build Service.

Service to update the changelog from git commits.

Buildrequires: python-jinja2
Buildrequires: python-py
Buildrequires: python-gitpython

%prep
%setup -q

# %build
# %python_build
# 
# %install
# %python_install
# 

%install

install -d /usr/lib/obs/service
install -m 0755 update_changelog /usr/lib/obs/service
install -m 0644 update_changelog.service /usr/lib/obs/service

# %files
# %defattr(-,root,root)
# %{python_sitelib}/update_changelog
# 
%changelog
