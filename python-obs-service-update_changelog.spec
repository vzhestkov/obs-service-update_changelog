# spec file for package obs-service-update_changelog

%{?!python_module:%define python_module() python-%{**} python3-%{**}}

%define service update_changelog
%define branch make-it-singlespec
%define modname obs-service-%{service}

Name:           python-obs-service-%{service}
Version:        0.6.0
Release:        0
Summary:        An OBS source service: Update spec file version
License:        GPL-2.0+
Group:          Development/Tools/Building
Url:            https://github.com/openSUSE/obs-service-%{service}/archive/%{branch}.tar.gz
Source:         https://github.com/openSUSE/obs-service-%{service}/archive/%{branch}.tar.gz
BuildArch:      noarch
BuildRequires:  %{python_module devel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-GitPython
Requires:       python-Jinja2 >= 2.9
Requires:       python-py
Requires:       python-pytz
BuildRoot:      %{_tmppath}/%{modname}-%{branch}
Requires(post):   update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
This is a source service for openSUSE Build Service.

Service to update the changelog from git commits.

%prep
%setup -q -n %{modname}-%{branch}

%build
%python_build

%install
install -d %{buildroot}%{_prefix}/lib/obs/service/
%python_install
%{python_expand \
cp %{buildroot}%{_bindir}/update_changelog %{buildroot}%{_prefix}/lib/obs/service/update_changelog-%{$python_bin_suffix}
sed -ri "1s@#!.*python.*@#!%{_bindir}/python%{python_version} -s@" %{buildroot}%{_prefix}/lib/obs/service/update_changelog-%{$python_bin_suffix}
%fdupes %{buildroot}%{$python_sitelib}
}
rm %{buildroot}%{_bindir}/update_changelog

%post
%{_sbindir}/update-alternatives --install %{_prefix}/lib/obs/service/update_changelog update_changelog \
    %{_prefix}/lib/obs/service/update_changelog-%{python_bin_suffix} %{python_version_nodots}

%postun
if [ ! -f %{_prefix}/lib/obs/service/update_changelog-%{python_bin_suffix} ]; then
   %{_sbindir}/update-alternatives --remove update_changelog \
       %{_prefix}/lib/obs/service/update_changelog-%{python_bin_suffix}
fi

%files %python_files
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%ghost %{_sysconfdir}/alternatives/update_changelog
%ghost %{_prefix}/lib/obs/service/update_changelog
%{_prefix}/lib/obs/service/update_changelog-%{python_bin_suffix}
%{python_sitelib}/*

%changelog
