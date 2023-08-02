#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Apache-Session
Version  : 1.94
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Apache-Session-1.94.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Apache-Session-1.94.tar.gz
Summary  : A persistence framework for session data
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Apache-Session-perl = %{version}-%{release}
Requires: perl(DB_File)
BuildRequires : buildreq-cpan
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::Exception)

%description
---------------------------------------------------------------------------
24 February 2004                  Jeffrey W. Baker <jwbaker@acm.org>

%package dev
Summary: dev components for the perl-Apache-Session package.
Group: Development
Provides: perl-Apache-Session-devel = %{version}-%{release}
Requires: perl-Apache-Session = %{version}-%{release}

%description dev
dev components for the perl-Apache-Session package.


%package perl
Summary: perl components for the perl-Apache-Session package.
Group: Default
Requires: perl-Apache-Session = %{version}-%{release}

%description perl
perl components for the perl-Apache-Session package.


%prep
%setup -q -n Apache-Session-1.94
cd %{_builddir}/Apache-Session-1.94

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Apache::Session.3
/usr/share/man/man3/Apache::Session::DB_File.3
/usr/share/man/man3/Apache::Session::File.3
/usr/share/man/man3/Apache::Session::Flex.3
/usr/share/man/man3/Apache::Session::Generate::MD5.3
/usr/share/man/man3/Apache::Session::Generate::ModUniqueId.3
/usr/share/man/man3/Apache::Session::Generate::ModUsertrack.3
/usr/share/man/man3/Apache::Session::Informix.3
/usr/share/man/man3/Apache::Session::Lock::File.3
/usr/share/man/man3/Apache::Session::Lock::MySQL.3
/usr/share/man/man3/Apache::Session::Lock::Null.3
/usr/share/man/man3/Apache::Session::Lock::Semaphore.3
/usr/share/man/man3/Apache::Session::Lock::Sybase.3
/usr/share/man/man3/Apache::Session::MySQL.3
/usr/share/man/man3/Apache::Session::MySQL::NoLock.3
/usr/share/man/man3/Apache::Session::Oracle.3
/usr/share/man/man3/Apache::Session::Postgres.3
/usr/share/man/man3/Apache::Session::Serialize::Base64.3
/usr/share/man/man3/Apache::Session::Serialize::Storable.3
/usr/share/man/man3/Apache::Session::Serialize::Sybase.3
/usr/share/man/man3/Apache::Session::Serialize::UUEncode.3
/usr/share/man/man3/Apache::Session::Store::DB_File.3
/usr/share/man/man3/Apache::Session::Store::File.3
/usr/share/man/man3/Apache::Session::Store::Informix.3
/usr/share/man/man3/Apache::Session::Store::MySQL.3
/usr/share/man/man3/Apache::Session::Store::Oracle.3
/usr/share/man/man3/Apache::Session::Store::Postgres.3
/usr/share/man/man3/Apache::Session::Store::Sybase.3
/usr/share/man/man3/Apache::Session::Sybase.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
