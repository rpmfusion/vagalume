Name:           vagalume
Version:        0.7.1
Release:        1%{?dist}
Summary:        Last.fm client for GNOME and Maemo

Group:          Applications/Multimedia
License:        GPLv3
URL:            http://vagalume.igalia.com/
Source0:        http://vagalume.igalia.com/files/source/vagalume_%{version}.orig.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gstreamer-devel gtk2-devel libxml2-devel
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
Vagalume is a Last.fm client based on Gnome, and specially designed to
work in the Maemo platform.

Vagalume has the following features:

   * It plays Last.fm streams using the Last.fm protocol v1.2
   * It can play any Last.fm radio: personal, neighbours, loved
     tracks, or any other arbitrary URL.
   * It can download free tracks
   * It implements the Audioscrobbler Realtime Submission Protocol
     v1.2, specifically:
      * Now Playing information
      * Scrobbling of tracks that you listen
      * Love/Ban ratings
   * It displays the album cover of the track being played
   * The user can tag artists, tracks and albums
   * The user can send recommendations to other users
   * The user can add tracks to their playlist


%prep
%setup -q -n %{name}-%{version}.orig


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
