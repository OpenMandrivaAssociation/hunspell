%define major 0
%define api 1.2
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Summary:	Spell checker and morphological analyzer library
Name:		hunspell
Version:	1.2.12
Release:	%mkrel 2
License:	GPLv2+
Group:		System/Internationalization
Url:		http://hunspell.sourceforge.net/
Source0:	http://downloads.sourceforge.net/hunspell/%{name}-%{version}.tar.bz2
# (tpg) Mdv's specific path to myspell dictionaries
Patch0:		%{name}-1.2.12-dict-path.patch
# add patch from upstream to fix double buffer gcc fortify issue, it was causing
# a buffer overflow in mozilla thunderbird:
# https://bugzilla.mozilla.org/show_bug.cgi?id=583582
Patch1:		hunspell-1.2.12-fix-double-buffer-gcc-fortify-issue.patch
BuildRequires:	libreadline-devel
BuildRequires:	libncursesw-devel
BuildRequires:	ncurses-devel
BuildRequires:	bison
BuildRequires:	libtool
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%patch1 -p1 -b .gcc-fortify

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README
%{_bindir}/*
%{_mandir}/hu/man1/*
%{_mandir}/man1/*
%{_mandir}/man3/

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*%{api}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/hu/man4/*
%{_mandir}/man4/*
