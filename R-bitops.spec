#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v20
# autospec commit: f35655a
#
Name     : R-bitops
Version  : 1.0.9
Release  : 98
URL      : https://cran.r-project.org/src/contrib/bitops_1.0-9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bitops_1.0-9.tar.gz
Summary  : Bitwise Operations
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-bitops-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# R-bitops -- R CRAN package `bitops` -- implementing bitwise operations
## Functionality

%package lib
Summary: lib components for the R-bitops package.
Group: Libraries

%description lib
lib components for the R-bitops package.


%prep
%setup -q -n bitops
pushd ..
cp -a bitops buildavx2
popd
pushd ..
cp -a bitops buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728053333

%install
export SOURCE_DATE_EPOCH=1728053333
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bitops/DESCRIPTION
/usr/lib64/R/library/bitops/INDEX
/usr/lib64/R/library/bitops/Meta/Rd.rds
/usr/lib64/R/library/bitops/Meta/features.rds
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
/usr/lib64/R/library/bitops/tests/consistency.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/bitops/libs/bitops.so
/V4/usr/lib64/R/library/bitops/libs/bitops.so
/usr/lib64/R/library/bitops/libs/bitops.so
