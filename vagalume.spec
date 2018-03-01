Name:           vagalume
Version:        0.8.6
Release:        2%{?dist}
Summary:        Last.fm client for GNOME and Maemo

Group:          Applications/Multimedia
License:        GPLv3
URL:            http://vagalume.igalia.com/
Source0:        %url/files/source/vagalume-%{version}.tar.gz
Source1:        vagalumectl.desktop.patch

BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
Requires:       hicolor-icon-theme
Requires:       gstreamer1-plugins-ugly


%description
Vagalume is a GTK+-based Last.fm client. Although it works on standard
PCs, it is specially designed to work in the Maemo platform, the one
used by some Nokia devices such as the 770, N800, N810 and N900.

Its main features are:

    * It plays Last.fm radio streams (using the v2.0 API)
    * It supports Libre.fm and other compatible servers
    * Support for different radio stations (personal, neighbours, loved tracks,
       ..., or any lastfm:// URL)
    * It supports marking tracks as loved or banned
    * It can tag artists, tracks and albums
    * It can send recommendations to other users
    * It can add tracks to your playlist
    * It can download free tracks to your hard disk
    * It scrobbles tracks so they appear in your Last.fm webpage
      (this can be disabled at runtime).
    * It sends Now Playing information following the Audioscrobbler
      Realtime Submission Protocol v1.2.
    * Supports discovery mode
    * Bookmarks
    * Remote control
    * Gettext support (translated into many languages)


%prep
%setup -q
# remove deprecated category
sed -i 's|;Application;|;|' data/vagalume.desktop.in.in


%build
%configure
%make_build


%install
%make_install

pushd $RPM_BUILD_ROOT%{_datadir}/applications
cp -p vagalume{,ctl}.desktop
cat %{SOURCE1} | patch -p0
desktop-file-validate vagalume.desktop
desktop-file-validate vagalumectl.desktop
popd

%find_lang %{name}

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/vagalume*
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/vagalume.service
%{_datadir}/icons/hicolor/*/apps/vagalume.png
%{_datadir}/pixmaps/vagalume.*
%{_datadir}/vagalume/
%{_mandir}/man*/*


%changelog
* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 21 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.8.6-1
- Update to 0.8.6 (rfbz #4373)
- Clean up spec file

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.8.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.8.5-4
- Mass rebuilt for Fedora 19 Features

* Fri Feb  3 2012 Michel Salim <salimma@fedoraproject.org> - 0.8.5-3
- Update desktop database to (de-)register lastfm:// handler

* Fri Feb  3 2012 Michel Salim <salimma@fedoraproject.org> - 0.8.5-2
- Switch to building against GTK+ 3.0
- Enable mixer, notifications, and proxy support
- Register lastfm:// handler

* Wed Feb  1 2012 Michel Salim <salimma@fedoraproject.org> - 0.8.5-1
- Update to 0.8.5

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb  7 2011 Michel Salim <salimma@fedoraproject.org> - 0.8.4-1
- Update to 0.8.4

* Thu Oct 14 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.8.3-4
- Rebuilt for gcc bug

* Mon Mar 29 2010 Michel Salim <salimma@fedoraproject.org> - 0.8.3-3
- Restore .xpm icon

* Sat Mar 27 2010 Michel Salim <salimma@fedoraproject.org> - 0.8.3-2
- Exclude old .xpm icon

* Thu Mar 18 2010 Michel Salim <salimma@fedoraproject.org> - 0.8.3-1
- Update to 0.8.3

* Wed May 13 2009 Michel Salim <salimma@fedoraproject.org> - 0.7.1-3
- Enable playback of others' recommendations and tags (upstream bug #4072)

* Tue May  5 2009 Michel Salim <salimma@fedoraproject.org> - 0.7.1-2
- Fix border width (upstream bug #4041)

* Tue Mar 24 2009 Michel Salim <salimma@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Fri Jan 30 2009 Michel Salim <michel.sylvan@gmail.com> - 0.7-2
- Require gstreamer-plugins-ugly (bz #347)

* Mon Sep  1 2008 Michel Salim <michel.sylvan@gmail.com> - 0.7-1
- Update to 0.7

* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.6-4
- rebuild

* Sat May 24 2008 Michel Salim <michel.sylvan@gmail.com> - 0.6-3.1
- BR on curl-devel for Fedora < 9, instead of libcurl-devel

* Fri May 23 2008 Michel Salim <michel.sylvan@gmail.com> - 0.6-3
- Update icon cache after (un)installation

* Mon May 19 2008 Michel Salim <michel.sylvan@gmail.com> - 0.6-2
- Add BR on gettext

* Sun May 18 2008 Michel Salim <michel.sylvan@gmail.com> - 0.6-1
- Update to 0.6

* Fri May  2 2008 Michel Salim <michel.sylvan@gmail.com> - 0.5.1-1
- Update to 0.5.1

* Wed Nov 14 2007 Michel Salim <michel.sylvan@gmail.com> - 0.2-1
- Initial package
