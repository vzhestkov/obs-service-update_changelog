# spec file for package obs-service-update_changelog

%define service update_changelog
%define branch master

Name:           obs-service-%{service}
Version:        0.6.0
Release:        0
Summary:        An OBS source service: Update spec file version
License:        GPL-2.0+
Group:          Development/Tools/Building
Url:            https://github.com/openSUSE/obs-service-%{service}/archive/%{branch}.tar.gz
Source:         https://github.com/openSUSE/obs-service-%{service}/archive/%{branch}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python-rpm-macros
Requires:       python3-GitPython
Requires:       python3-Jinja2 >= 2.9
Requires:       python3-py
Requires:       python3-pytz
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
%dir /usr/lib/obs
%dir /usr/lib/obs/service
/usr/bin/update_changelog
%{python3_sitelib}/updatechangelog
%{python3_sitelib}/updatechangelog-*.egg-info
/usr/lib/obs/service/update_changelog
/usr/lib/obs/service/update_changelog.service
 
%changelog
