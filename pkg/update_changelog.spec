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
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

Service to update the changelog from git commits.

%prep
%setup -q -n obs-service-%{service}-%{version}

%build
%python_build

%install
%python_install

%files
%defattr(-,root,root)
%{python_sitelib}/update_changelog

%changelog
