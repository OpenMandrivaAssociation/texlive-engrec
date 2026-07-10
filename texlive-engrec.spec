%global tl_name engrec
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Enumerate with lower- or uppercase Greek letters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/engrec
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/engrec.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/engrec.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/engrec.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides two macros \engrec and \EnGrec to convert number
arguments to lower case or upper case greek letters. They have the
syntax of \alph, i.e. \engrec{a_counter}, \EnGrec{a_counter}. Options
are provided to work with the upgreek and fourier packages. Requires
amstext.

