#
# spec file for package gtk-sharp2
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _name gtk-sharp

Name:           gtk-sharp2
Url:            http://www.mono-project.com/GtkSharp
Summary:        .Net Language Bindings for GTK+
License:        GPL-2.0
Group:          System/GUI/GNOME
# bug437293
%ifarch ppc64
Obsoletes:      gtk-sharp2-64bit
%endif
%ifarch  %ix86 ppc
Obsoletes:      gtk-sharp2-32bit
%endif
BuildRequires:  libglade2-devel
BuildRequires:  libtool
BuildRequires:  mono-devel
BuildRequires:  monodoc-core
%if 0%{?fedora} || 0%{?rhel} || 0%{?centos}
BuildRequires:  pkgconfig
BuildRequires:  librsvg2-devel
%else
BuildRequires:  pkg-config
BuildRequires:  librsvg-devel
BuildRequires:  update-desktop-files
%endif
BuildRequires:  vte-devel
Version:	2.12.43
Release:	0.xamarin.9
Source:         %{_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains Mono bindings for gtk+, gdk, atk, and pango.

%package gapi
Summary:        C Source Parser and C Generator
License:        GPL-2.0
Group:          System/GUI/GNOME
Requires:       perl-XML-LibXML
Requires:       perl-XML-LibXML-Common
Requires:       perl-XML-SAX

%description gapi
The gtk-sharp-gapi package includes the parser and code generator used
by the GTK if you want to bind GObject-based libraries, or need to
compile a project that uses it to bind such a library.

%package -n gtk-sharp2-doc
Summary:        Monodoc documentation for gtk-sharp2
License:        LGPL-2.1
Group:          System/GUI/GNOME

%description -n gtk-sharp2-doc
This package contains the gtk-sharp2 documentation for monodoc.

%package -n gtk-sharp2-devel
Summary:        Dummy -devel package for gtk-sharp2
License:        LGPL-2.1
Group:          System/GUI/GNOME
Requires:	gtk-sharp2

%description -n gtk-sharp2-devel
Dummy package to unify dependencies between SUSE and Fedora

%package -n glib-sharp2
Summary:        Mono bindings for glib
License:        LGPL-2.1
Group:          System/GUI/GNOME

%description -n glib-sharp2
This package contains Mono bindings for glib.

%package -n glade-sharp2
Summary:        Mono bindings for glade
License:        LGPL-2.1
Group:          System/GUI/GNOME

%description -n glade-sharp2
This package contains Mono bindings for glade.

%package -n gtk-sharp2-complete
Summary:        GTK+ and GNOME bindings for Mono (virtual package)
License:        LGPL-2.1
Group:          System/GUI/GNOME
Requires:       glade-sharp2 = %{version}-%{release}
Requires:       glib-sharp2 = %{version}-%{release}
Requires:       gtk-sharp2 = %{version}-%{release}
Requires:       gtk-sharp2-doc = %{version}-%{release}
Requires:       gtk-sharp2-gapi = %{version}-%{release}

%description -n gtk-sharp2-complete
Gtk# is a library that allows you to build fully native graphical GNOME
applications using Mono. Gtk# is a binding to GTK+, the cross platform
user interface toolkit used in GNOME. It includes bindings for Gtk,
Atk, Pango, Gdk, libgnome, libgnomeui and libgnomecanvas.  (Virtual
package which depends on all gtk-sharp2 subpackages)

%prep
%setup -q -n %{_name}-%{version}

%build
autoreconf -fiv
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
# That should come frmo mono-core now
#export MONO_CAIRO_LIBS=$(pkg-config --libs mono-cairo | sed 's:2.0:4.5:')
%configure --libexecdir=%{_prefix}/lib --enable-debug
make

%install
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/*.*a

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{_libdir}/libatksharpglue-2.so
%{_libdir}/libgdksharpglue-2.so
%{_libdir}/libgtksharpglue-2.so
%{_libdir}/libpangosharpglue-2.so
%{_libdir}/pkgconfig/gtk-sharp-2.0.pc
%{_libdir}/pkgconfig/gtk-dotnet-2.0.pc
%{_prefix}/lib/mono/gac/*atk-sharp
%{_prefix}/lib/mono/gtk-sharp-2.0/*atk-sharp.dll
%{_prefix}/lib/mono/gac/*gdk-sharp
%{_prefix}/lib/mono/gtk-sharp-2.0/*gdk-sharp.dll
%{_prefix}/lib/mono/gac/*gtk-dotnet
%{_prefix}/lib/mono/gtk-sharp-2.0/*gtk-dotnet.dll
%{_prefix}/lib/mono/gac/*gtk-sharp
%{_prefix}/lib/mono/gtk-sharp-2.0/*gtk-sharp.dll
%{_prefix}/lib/mono/gac/*pango-sharp
%{_prefix}/lib/mono/gtk-sharp-2.0/*pango-sharp.dll

%files gapi
%defattr(-, root, root)
%{_bindir}/gapi2-codegen
%{_bindir}/gapi2-fixup
%{_bindir}/gapi2-parser
%{_datadir}/gapi-2.0
%{_libdir}/pkgconfig/gapi-2.0.pc
%{_prefix}/lib/gtk-sharp-2.0/gapi_codegen.exe
%{_prefix}/lib/gtk-sharp-2.0/gapi-fixup.exe
%{_prefix}/lib/gtk-sharp-2.0/gapi-parser.exe
%{_prefix}/lib/gtk-sharp-2.0/gapi_pp.pl
%{_prefix}/lib/gtk-sharp-2.0/gapi2xml.pl

%files -n gtk-sharp2-doc
%defattr(-, root, root)
%doc COPYING ChangeLog README
%{_prefix}/lib/monodoc

%files -n glib-sharp2
%defattr(-, root, root)
%{_libdir}/libglibsharpglue-2.so
%{_libdir}/pkgconfig/glib-sharp-2.0.pc
%{_prefix}/lib/mono/gac/*glib-sharp
%{_prefix}/lib/mono/gtk-sharp-2.0/*glib-sharp.dll

%files -n glade-sharp2
%defattr(-, root, root)
%{_libdir}/libgladesharpglue-2.so
%{_libdir}/pkgconfig/glade-sharp-2.0.pc
%{_prefix}/lib/mono/gac/*glade-sharp
%{_prefix}/lib/mono/gtk-sharp-2.0/*glade-sharp.dll

%files -n gtk-sharp2-complete
%defattr(-, root, root)
%dir %{_prefix}/lib/mono/gtk-sharp-2.0
%dir %{_prefix}/lib/gtk-sharp-2.0

%changelog

