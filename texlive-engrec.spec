# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/engrec
# catalog-date 2008-05-07 22:48:57 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-engrec
Version:	1.1
Release:	9
Summary:	Enumerate with lower- or uppercase Greek letters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/engrec
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engrec.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engrec.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engrec.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides two macros \engrec and \EnGrec to convert
number arguments to lower case or upper case greek letters.
They have the syntax of \alph, i.e. \engrec{a_counter},
\EnGrec{a_counter}. Options are provided to work with the
upgreek and fourier packages. Requires amstext.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/engrec/engrec.sty
%doc %{_texmfdistdir}/doc/latex/engrec/LISEZMOI
%doc %{_texmfdistdir}/doc/latex/engrec/README
%doc %{_texmfdistdir}/doc/latex/engrec/engrec.pdf
#- source
%doc %{_texmfdistdir}/source/latex/engrec/Makefile
%doc %{_texmfdistdir}/source/latex/engrec/engrec.dtx
%doc %{_texmfdistdir}/source/latex/engrec/engrec.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 751469
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 718335
- texlive-engrec
- texlive-engrec
- texlive-engrec
- texlive-engrec

