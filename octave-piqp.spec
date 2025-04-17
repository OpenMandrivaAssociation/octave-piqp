%global octpkg piqp

# the *.oct library si sstripped somwhere
%global _debugsource_template %{nil}


Summary:	PIQP is a Proximal Interior Point Quadratic Programming solver, which can solve
Name:		octave-piqp
Version:	0.5.0
Release:	1
License:	BSD-2-Clause
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/piqp/
Url:		https://github.com/PREDICT-EPFL/piqp
Source0:	https://github.com/PREDICT-EPFL/piqp/releases/download/v%{version}/piqp-octave.tar.gz

BuildRequires:  octave-devel >= 4.0.0
BuildRequires:  pkgconfig(eigen3)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%patchlist
octave-piqp-0.5.0-use_system_eigen.patch

%description
PIQP is a Proximal Interior Point Quadratic Programming solver, which 
can solve dense and sparse quadratic programs.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-octave
sed -i -e "s,gnu++14,gnu++20,g" make_piqp.m

%build

%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

install -dm 0755 %{buildroot}%{_libdir}/octave/packages/%{octpkg}-%{version}
mv %{buildroot}%{_datadir}/octave/packages/%{octpkg}-%{version}/piqp_oct.oct \
	%{buildroot}%{_libdir}/octave/packages/%{octpkg}-%{version}

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

