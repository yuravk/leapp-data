%define dist_list almalinux centos oraclelinux rocky
%define conflict_dists() %(for i in almalinux centos oraclelinux rocky; do if [ "${i}" != "%{dist_name}" ]; then echo -n "leapp-data-${i} "; fi; done)

Name:		leapp-data
Version:	0.1
Release:	2%{?dist}
Summary:	data for migrating tool
Group:		Applications/Databases
License:	ASL 2.0
URL:		https://github.com/AlmaLinux/leapp-data
Source0:	%{name}-%{version}.tar.gz
BuildArch:  noarch

%package %{dist_name}
Summary: %{summary}
Conflicts: %{conflict_dists}

%description %{dist_name}
%{summary}


%description
%{dist_name} %{summary}

%prep
%setup -q


%build


%install
mkdir -p %{buildroot}%{_sysconfdir}/leapp/files
install -t %{buildroot}%{_sysconfdir}/leapp/files files/%{dist_name}/*


%files %{dist_name}
%doc
%{_sysconfdir}/leapp/files/*


%changelog
* Thu Aug 26 2021 Avi Miller <avi.miller@oracle.com> - 0.1-2
- switched to using the full oraclelinux name
- switched the Oracle Linux repos to use https
- added Apache-2.0 NOTICE attribution file

* Wed Aug 25 2021 Sergey Fokin <sfokin@almalinux.org> - 0.1-1
- initial project