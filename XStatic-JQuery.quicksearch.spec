#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-JQuery.quicksearch
Version  : 2.0.3.1
Release  : 24
URL      : http://pypi.debian.net/XStatic-JQuery.quicksearch/XStatic-JQuery.quicksearch-2.0.3.1.tar.gz
Source0  : http://pypi.debian.net/XStatic-JQuery.quicksearch/XStatic-JQuery.quicksearch-2.0.3.1.tar.gz
Summary  : JQuery.quicksearch 2.0.3 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-JQuery.quicksearch-python = %{version}-%{release}
Requires: XStatic-JQuery.quicksearch-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
--------------
        
        JQuery.quicksearch JavaScript library packaged for setuptools (easy_install)
        / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package `XStatic`.

%package python
Summary: python components for the XStatic-JQuery.quicksearch package.
Group: Default
Requires: XStatic-JQuery.quicksearch-python3 = %{version}-%{release}
Provides: xstatic-jquery.quicksearch-python

%description python
python components for the XStatic-JQuery.quicksearch package.


%package python3
Summary: python3 components for the XStatic-JQuery.quicksearch package.
Group: Default
Requires: python3-core
Provides: pypi(xstatic_jquery.quicksearch)

%description python3
python3 components for the XStatic-JQuery.quicksearch package.


%prep
%setup -q -n XStatic-JQuery.quicksearch-2.0.3.1
cd %{_builddir}/XStatic-JQuery.quicksearch-2.0.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583695508
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
