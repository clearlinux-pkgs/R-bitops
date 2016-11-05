#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bitops
Version  : 1.0
Release  : 26
URL      : http://cran.r-project.org/src/contrib/bitops_1.0-6.tar.gz
Source0  : http://cran.r-project.org/src/contrib/bitops_1.0-6.tar.gz
Summary  : Bitwise Operations
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-bitops-lib
BuildRequires : clr-R-helpers

%description


%package lib
Summary: lib components for the R-bitops package.
Group: Libraries

%description lib
lib components for the R-bitops package.


%prep
%setup -q -c -n bitops

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library bitops
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library bitops


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bitops/DESCRIPTION
/usr/lib64/R/library/bitops/INDEX
/usr/lib64/R/library/bitops/Meta/Rd.rds
/usr/lib64/R/library/bitops/Meta/hsearch.rds
/usr/lib64/R/library/bitops/Meta/links.rds
/usr/lib64/R/library/bitops/Meta/nsInfo.rds
/usr/lib64/R/library/bitops/Meta/package.rds
/usr/lib64/R/library/bitops/NAMESPACE
/usr/lib64/R/library/bitops/R/bitops
/usr/lib64/R/library/bitops/R/bitops.rdb
/usr/lib64/R/library/bitops/R/bitops.rdx
/usr/lib64/R/library/bitops/help/AnIndex
/usr/lib64/R/library/bitops/help/aliases.rds
/usr/lib64/R/library/bitops/help/bitops.rdb
/usr/lib64/R/library/bitops/help/bitops.rdx
/usr/lib64/R/library/bitops/help/paths.rds
/usr/lib64/R/library/bitops/html/00Index.html
/usr/lib64/R/library/bitops/html/R.css
/usr/lib64/R/library/bitops/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/bitops/libs/bitops.so
