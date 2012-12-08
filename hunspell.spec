%define major 0
%define api 1.3
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Summary:	Spell checker and morphological analyzer library
Name:		hunspell
Version:	1.3.2
Release:	4
License:	GPLv2+
Group:		System/Internationalization
Url:		http://hunspell.sourceforge.net/
Source0:	http://downloads.sourceforge.net/hunspell/%{name}-%{version}.tar.gz
# (tpg) Mdv's specific path to myspell dictionaries
Patch0:		%{name}-1.2.15-dict-path.patch
BuildRequires:	libreadline-devel
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	bison
BuildRequires:	libtool

%description
Hunspell is a spell checker and morphological analyzer library
and program designed for languages with rich morphology and complex
word compounding or character encoding.

%package -n %{libname}
Summary:	Shared libraries for hunspell
Group:		System/Libraries
Provides:	libhunspell = %{version}-%{release}

%description -n %{libname}
Shared libraries for hunspell.

%package -n %{develname}
Summary:	Development files for hunspell
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files and headers for hunspell.

%prep
%setup -q
%patch0 -p1 -b .dict

%build
%configure2_5x \
	--with-ui \
	--with-readline \
	--with-experimental \
	--disable-rpath

%make

%check
make check

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_bindir}/*
%{_mandir}/hu/man1/*
%{_mandir}/man1/*
%{_mandir}/man3/

%files -n %{libname}
%{_libdir}/*%{api}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%lang(hu) %{_mandir}/hu/man4/*
%{_mandir}/man4/*

%changelog
* Tue Dec 20 2011 Rafael da Veiga Cabral <cabral@mandriva.com> 1.3.2-2mdv2012.0
+ Revision: 744010
- get rid of .la files
- rebuild for solving of #64974 (lack of libstdc++.la)

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.3.2-1
+ Revision: 654432
- New version 1.3.2

* Sat Mar 12 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.15-1
+ Revision: 644044
- update to new version 1.2.15
- rediff patch 0
- drop patch 1, fixed by upstream

* Wed Sep 08 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.2.12-3mdv2011.0
+ Revision: 576881
- fix previously applied patch

* Wed Sep 08 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.2.12-2mdv2011.0
+ Revision: 576806
- add upstream patch to fix double buffer gcc fortify issue (mdv#60931)

* Sat Aug 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.12-1mdv2011.0
+ Revision: 567379
- update to new version 1.2.12
- rediff patch 0

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.8-4mdv2010.1
+ Revision: 520123
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.2.8-3mdv2010.0
+ Revision: 425192
- rebuild

* Thu Mar 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.8-2mdv2009.1
+ Revision: 354333
- rebuild for latest readline

* Tue Nov 04 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.8-1mdv2009.1
+ Revision: 299853
- update to new version 1.2.8
- enable some extra experimental functions

* Tue Nov 04 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.7-2mdv2009.1
+ Revision: 299841
- rebuild

* Mon Aug 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.7-1mdv2009.0
+ Revision: 275775
- adjust rpm group
- update to new version 1.2.7
- enable checks

* Wed Aug 13 2008 Tiago Salem <salem@mandriva.com.br> 1.2.6-3mdv2009.0
+ Revision: 271416
- add a provide for libhunspell
- bump release

* Mon Jul 21 2008 Thierry Vignaud <tv@mandriva.org> 1.2.6-2mdv2009.0
+ Revision: 239269
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Thu Jul 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.6-1mdv2009.0
+ Revision: 237832
- update to new version 1.2.6
- Patch0: add mandriva specific path to myspell dictionaries

* Thu Jul 10 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.5-1mdv2009.0
+ Revision: 233526
- update to new version 1.2.5
- run scriplets only for mdv releases older than 2009.0

* Wed Jun 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.4-1mdv2009.0
+ Revision: 225403
- add missing buildrequire on ncurses-devel
- fix file list
- update to new version 1.2.4

  + Thierry Vignaud <tv@mandriva.org>
    - make it backportable on 2008.1

* Thu May 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.2-1mdv2009.0
+ Revision: 213002
- add sources and spec file
- Created package structure for hunspell.

