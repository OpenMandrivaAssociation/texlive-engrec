Name:		texlive-engrec
Version:	15878
Release:	2
Summary:	Enumerate with lower- or uppercase Greek letters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/engrec
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engrec.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engrec.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engrec.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
