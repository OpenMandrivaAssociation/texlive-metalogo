Name:		texlive-metalogo
Version:	18611
Release:	2
Summary:	Extended TeX logo macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/metalogo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metalogo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metalogo.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metalogo.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package exposes spacing parameters for various TeX logos
to the end user, to optimise the logos for different fonts.
Written especially for XeLaTeX users.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
