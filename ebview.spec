%define	name	ebview
%define	version	0.3.6
%define	release	%mkrel 4
%define	Summary	EBView is a browser for EB/EPWING files

Name:		%{name}
Summary:	%{Summary}
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPL
URL:		http://ebview.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/ebview/%{name}-%{version}.tar.bz2
# patches from Gentoo
Patch0:		ebview-0.3.6_pango_with_cairo.patch
Patch1:		ebview-0.3.6-destdir.diff
# Patch from debian
Patch2:		ebview-0.3.6-fix-build.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildrootroot
Requires:	eb
BuildRequires:	eb-devel gtk2-devel eb

%description
EBView is a browser for EB/EPWING files.


%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p0

%build
%configure2_5x

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=EBView
Comment=%{Summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Utility;TextTools;GTK;
EOF

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/ebview
%{_datadir}/ebview
%{_datadir}/applications/mandriva-%{name}.desktop
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog NEWS README
