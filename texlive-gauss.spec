# revision 24411
# category Package
# catalog-ctan /macros/latex/contrib/gauss
# catalog-date 2011-10-26 17:26:33 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-gauss
Version:	20111026
Release:	5
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111026-2
+ Revision: 752187
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111026-1
+ Revision: 718523
- texlive-gauss
- texlive-gauss
- texlive-gauss
- texlive-gauss

