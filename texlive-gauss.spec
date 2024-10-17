Name:		texlive-gauss
Version:	32934
Release:	2
Summary:	A package for Gaussian operations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gauss
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gauss.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gauss.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The gauss package provides configurable tools for producing row
and column operations on matrices (a.k.a. Gaussian operations).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gauss/gauss.sty
%doc %{_texmfdistdir}/doc/latex/gauss/README
%doc %{_texmfdistdir}/doc/latex/gauss/gauss-doc.pdf
%doc %{_texmfdistdir}/doc/latex/gauss/gauss-ex.pdf
%doc %{_texmfdistdir}/doc/latex/gauss/gauss-ex.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
