# revision 18611
# category Package
# catalog-ctan /macros/latex/contrib/metalogo
# catalog-date 2010-05-29 17:49:59 +0200
# catalog-license lppl
# catalog-version 0.12
Name:		texlive-metalogo
Version:	0.12
Release:	1
Summary:	Extended TeX logo macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/metalogo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metalogo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metalogo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metalogo.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package exposes spacing parameters for various TeX logos
to the end user, to optimise the logos for different fonts.
Written especially for XeLaTeX users.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/metalogo/metalogo.sty
%doc %{_texmfdistdir}/doc/latex/metalogo/README
%doc %{_texmfdistdir}/doc/latex/metalogo/TeXoutline.pdf
%doc %{_texmfdistdir}/doc/latex/metalogo/eLaToutline.pdf
%doc %{_texmfdistdir}/doc/latex/metalogo/metalogo.pdf
#- source
%doc %{_texmfdistdir}/source/latex/metalogo/metalogo.dtx
%doc %{_texmfdistdir}/source/latex/metalogo/metalogo.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
