# revision 32934
# category Package
# catalog-ctan /macros/latex/contrib/gauss
# catalog-date 2012-04-10 17:44:48 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-gauss
Version:	20180303
Release:	1
Summary:	A package for Gaussian operations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gauss
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gauss.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gauss.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
