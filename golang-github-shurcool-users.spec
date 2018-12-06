# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/users
%global commit          49c67e49c5377c48c01f82d3e1b6844a901a0b33

%global common_description %{expand:
Users service definition for Go.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Users service definition for Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/google/go-github/github)
BuildRequires: golang(github.com/tambet/go-asana/asana)
BuildRequires: golang(golang.org/x/net/webdav)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git49c67e4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180420git49c67e4
- First package for Fedora

