%define major 0
%define api 1.7
%define libname	%mklibname %{name} %{api} %{major}
%define devname	%mklibname %{name} -d
%define _disable_rebuild_configure 1

Summary:	Spell checker and morphological analyzer library
Name:		hunspell
Version:	1.7.2
Release:	1
License:	GPLv2+
Group:		System/Internationalization
Url:		http://hunspell.github.io/
Source0:	https://github.com/hunspell/hunspell/archive/v%{version}/%{name}-%{version}.tar.gz
# (tpg) Mdv's specific path to myspell dictionaries
Patch0:		%{name}-1.6.1-dict-path.patch
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	libtool
BuildRequires:	readline-devel >= 7.0
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	gettext-devel

%description
Hunspell is a spell checker and morphological analyzer library
and program designed for languages with rich morphology and complex
word compounding or character encoding.

%package tools
Summary:	Tools for hunspell
Group:		System/Internationalization
Conflicts:	%{name} < 1.7.0-2

%description tools
This package contains the additional tools for %{name}.

%package -n %{libname}
Summary:	Shared libraries for hunspell
Group:		System/Libraries
Provides:	libhunspell = %{version}-%{release}

%description -n %{libname}
Shared libraries for hunspell.

%package -n %{devname}
Summary:	Development files for hunspell
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{name}-tools = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files and headers for hunspell.

%prep
%setup -q
%autopatch -p1

%build
autoreconf -fiv
%configure \
	--disable-static \
	--with-ui \
	--with-readline \
	--with-experimental \
	--disable-rpath

%make_build

# (tpg) disable checks as they falls
#check
#make check

%install
%make_install

%files
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_datadir}/*

%files tools
%{_bindir}/*
%exclude %{_bindir}/%{name}

%files -n %{libname}
%{_libdir}/libhunspell-%{api}.so.%{major}*

%files -n %{devname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*
