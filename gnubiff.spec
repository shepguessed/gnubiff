Summary:	Mail notification program
Summary(pl):	Program powiadamiaj�cy o nowej poczcie
Name:		gnubiff
Version:	1.0.6
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	4f11e58efe5c3b422e6c0312c8aed63e
Patch0:		%{name}-configure.patch
URL:		http://gnubiff.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	autoconf
BuildRequires:	automake
Buildrequires:	gnome-panel-devel >= 2.4.0
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	popt-devel
BuildRequires:	openssl-devel >= 0.9.7c
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnubiff is a mail notification program that checks for mail, displays
headers when new mail has arrived and allow to read first lines of new
mails.

%description -l pl
gnubiff jest programem powiadamiaj�cym, kt�ry sprawdza poczt�,
wy�wietla nag��wki i pozwala przeczyta� pierwsze linie nowych list�w.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-gnome \
	--with-password

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/gnome-*/ui/*.xml
%{_datadir}/%{name}
%{_infodir}/*.info*
%{_mandir}/man1/%{name}.1*
%{_pixmapsdir}/*.png
%{_datadir}/sounds/%{name}
