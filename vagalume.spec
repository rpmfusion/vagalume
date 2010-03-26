Name:           vagalume
Version:        0.8.3
Release:        1%{?dist}.1
Summary:        Last.fm client for GNOME and Maemo

Group:          Applications/Multimedia
License:        GPLv3
URL:            http://vagalume.igalia.com/
Source0:        http://vagalume.igalia.com/files/source/vagalume_%{version}.orig.tar.gz
# remove patch0 when 0.7.2 is released
# Patch0:         %{name}-0.7.1-border_width.patch
# Patch1:         %{name}-0.7.1-others.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gstreamer-devel gtk2-devel libxml2-devel intltool
# curl has been renamed in F-9. New package still provides curl[-devel] but
# better be safe
%if 0%{?fedora} >= 9
BuildRequires:  libcurl-devel
%else
BuildRequires:  curl-devel
%endif
BuildRequires:  libnotify-devel dbus-glib-devel
BuildRequires:  desktop-file-utils gettext
Requires:       hicolor-icon-theme
Requires:       gstreamer-plugins-ugly

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
%setup -q -n %{name}-%{version}.orig
#patch0 -p1 -b .border_width
#patch1 -p1 -b .others


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
desktop-file-install --vendor="fedora" \
                     --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
                     --delete-original \
  $RPM_BUILD_ROOT%{_datadir}/applications/vagalume.desktop                   


%clean
rm -rf $RPM_BUILD_ROOT

%post 
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun 
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_bindir}/vagalume*
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/vagalume.service
%{_datadir}/icons/hicolor/*/apps/vagalume.png
%{_datadir}/pixmaps/vagalume.*
%{_datadir}/vagalume
%{_mandir}/man*/*


%changelog
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
