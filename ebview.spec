%define	name	ebview
%define	version	0.3.6
%define	release	%mkrel 3
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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildrootroot
Requires:	eb libgtk+2.0_0
BuildRequires:	eb-devel gtk2-devel

%description
EBView is a browser for EB/EPWING files.


%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
%configure2_5x

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

# menu
mkdir -p %{buildroot}%{_menudir}
cat > %{buildroot}%{_menudir}/%{name} <<EOF
?package(%{name}): \
	command="%{_bindir}/ebview" \
	icon="documentation_section.png" \
	title="EBView" \
	longtitle="%{Summary}" \
	needs="x11" \
	section="More Applications/Documentation" \
	xdg="true"
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=EBView
Comment=%{Summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation;
EOF

%clean
rm -rf %{buildroot}

%post
%update_menus

%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/ebview
%{_datadir}/ebview
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog NEWS README
