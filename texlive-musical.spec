Name:		texlive-musical
Version:	54758
Release:	1
Summary:	Typeset (musical) theatre scripts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/musical
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musical.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musical.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is designed to simplify the development and
distribution of scripts for theatrical musicals, especially
ones under development. The output is formatted to follow
generally accepted script style[1] while also maintaining a
high level of typographic integrity, and includes commands for
dialog, lyrics, stage directions, music and dance cues,
rehearsal marks, and more. It gracefully handles dialog that
crosses page breaks, and can generate lists of songs and lists
of dances in the show. [1] There are lots of references for the
One True Way to format a script. Naturally, none of them agree.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/musical
%doc %{_texmfdistdir}/doc/latex/musical

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
