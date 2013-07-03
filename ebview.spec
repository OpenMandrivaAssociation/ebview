Name:		ebview
Summary:	Browser for EB/EPWING files
Version:	0.3.6.2
Release:	4
Group:		System/Internationalization
License:	GPL
URL:		http://ebview.sourceforge.net/
Source0:		%{name}_%{version}.orig.tar.gz
#Source0:	http://prdownloads.sourceforge.net/ebview/%{name}-%{version}.tar.bz2
# patches from Gentoo
Patch0:		ebview-0.3.6_pango_with_cairo.patch
Patch1:		ebview-0.3.6.2-destdir.diff
# Fix build errors with -Wformat -Werror=format-security
Patch3:		ebview-0.3.6-format-security.patch
Requires:	eb
BuildRequires:	eb-devel eb
BuildRequires:  pkgconfig(pangox)
BuildRequires:  pkgconfig(gtk+-2.0)

%description
EBView is a browser for EB/EPWING files.


%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch3 -p1

%build
%configure2_5x

%make

%install
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

%files -f %{name}.lang
%{_bindir}/ebview
%{_datadir}/ebview
%{_datadir}/applications/mandriva-%{name}.desktop
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog NEWS README


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.6.2-2mdv2011.0
+ Revision: 617951
- the mass rebuild of 2010.0 packages

* Mon Aug 17 2009 Frederik Himpe <fhimpe@mandriva.org> 0.3.6.2-1mdv2010.0
+ Revision: 417407
- Update to new unofficial 0.3.6.2 version from Debian
- Remove build fix patch: not needed anymore
- Rediff destdir patch

* Mon Mar 23 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.3.6-7mdv2009.1
+ Revision: 360562
- Fix build errors with -Wformat -Werror=format-security.

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.3.6-6mdv2009.0
+ Revision: 244605
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Oct 16 2007 Funda Wang <fwang@mandriva.org> 0.3.6-4mdv2008.1
+ Revision: 98757
- Add debian patch to have it built

  + Thierry Vignaud <tv@mandriva.org>
    - bump release
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'
    - rebuild for new gettext
    - Import ebview



* Fri Aug 25 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.3.6-2mdv2007.0
- fix summary macro used in menu item
- add xdg menu
- cleanups

* Wed Mar 08 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.3.6-1mdk
- first spec for Mandriva
