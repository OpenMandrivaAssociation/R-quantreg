%bcond_without bootstrap
%global packname  quantreg
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          4.76
Release:          1
Summary:          Quantile Regression
Group:            Sciences/Mathematics
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-stats R-SparseM 
%if %{with bootstrap}
Requires:         R-tripack R-akima R-MASS R-survival R-rgl R-logspline R-nor1mix R-MatrixModels R-Matrix R-Formula
%else
Requires:         R-tripack R-akima R-MASS R-survival R-rgl R-logspline R-nor1mix R-MatrixModels R-Matrix R-Formula R-zoo 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats R-SparseM
%if %{with bootstrap}
BuildRequires:    R-tripack R-akima R-MASS R-survival R-rgl R-logspline R-nor1mix R-MatrixModels R-Matrix R-Formula
%else
BuildRequires:    R-tripack R-akima R-MASS R-survival R-rgl R-logspline R-nor1mix R-MatrixModels R-Matrix R-Formula R-zoo 
%endif
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
Quantile regression and related methods.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/Changelog
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/FAQ
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
