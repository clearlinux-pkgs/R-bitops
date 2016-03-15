#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bitops
Version  : 1.0
Release  : 17
URL      : http://cran.r-project.org/src/contrib/bitops_1.0-6.tar.gz
Source0  : http://cran.r-project.org/src/contrib/bitops_1.0-6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : clr-R-helpers

%description


%prep
%setup -q -c -n bitops

%build

%install
rm -rf %{buildroot}
export LANG=C
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library bitops
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-codoc -l %{buildroot}/usr/lib64/R/library bitops


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
/usr/lib64/R/library/bitops/libs/bitops.so
/usr/lib64/R/library/bitops/libs/symbols.rds
