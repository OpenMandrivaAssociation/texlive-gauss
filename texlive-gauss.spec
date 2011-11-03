# revision 24411
# category Package
# catalog-ctan /macros/latex/contrib/gauss
# catalog-date 2011-10-26 17:26:33 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-gauss
Version:	20111026
Release:	1
Summary:	A package for Gaussian operations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gauss
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gauss.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gauss.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The gauss package provides configurable tools for producing row
and column operations on matrices (a.k.a. Gaussian operations).

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
%{_texmfdistdir}/tex/latex/gauss/gauss.sty
%doc %{_texmfdistdir}/doc/latex/gauss/README
%doc %{_texmfdistdir}/doc/latex/gauss/gauss-doc.pdf
%doc %{_texmfdistdir}/doc/latex/gauss/gauss-ex.pdf
%doc %{_texmfdistdir}/doc/latex/gauss/gauss-ex.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
