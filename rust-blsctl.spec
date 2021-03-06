# Generated by rust2rpm 15
%bcond_without check
%global __cargo_skip_build 0

%global crate blsctl

Name:           rust-%{crate}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Manages BLS entries and kernel cmdline options

# Upstream license specification: LGPL-2.1-or-later
License:        LGPLv2+
URL:            https://crates.io/crates/blsctl
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  rpm-devel

Requires:      rpm-libs

%global _description %{expand:
Manages BLS entries and kernel cmdline options.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%{_bindir}/blsctl

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Mon Oct 05 12:21:12 CEST 2020 Javier Martinez Canillas <javierm@redhat.com> - 0.2.1-1
- Initial package
