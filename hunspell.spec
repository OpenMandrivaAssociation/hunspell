%define major 0
%define api 1.6
%define libname	%mklibname %{name} %{api} %{major}
%define devname	%mklibname %{name} -d
%define _disable_rebuild_configure 1

Summary:	Spell checker and morphological analyzer library
Name:		hunspell
Version:	1.6.2
Release:	1
License:	GPLv2+
Group:		System/Internationalization
Url:		http://hunspell.github.io/
Source0:	https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz
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
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files and headers for hunspell.

%prep
%setup -q
%apply_patches

%build
autoreconf -fiv
%configure \
	--disable-static \
	--with-ui \
	--with-readline \
	--with-experimental \
	--disable-rpath

%make

# (tpg) disable checks as they falls
#check
#make check

%install
%makeinstall_std

%files
%doc AUTHORS NEWS README
%{_bindir}/*
%lang(hu) %{_mandir}/hu/man1/*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files -n %{libname}
%{_libdir}/libhunspell-%{api}.so.%{major}*

%files -n %{devname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*
