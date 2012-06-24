Summary:	Parser generation for Emacs
Name:		xemacs-semantic-pkg
%define 	srcname	semantic
Version:	1.17
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
BuildArch:	noarch
Requires:	xemacs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Semantic is a program for Emacs which includes, at its core, a lexer,
and a compiler compiler (bovinator).  Additional tools include a
bnf->semantic table converter, example tables, and a speedbar tool.

The core utility is the ``semantic bovinator'' which has similar
behaviors as yacc or bison.  Since it is not designed to be as feature
rich as these tools, it uses the term ``bovine'' for cow, a lesser
cousin of the yak and bison.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# %doc lisp/semnatic/ChangeLog
# %{_datadir}/xemacs-packages%{_sysconfdir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*
%{_datadir}/xemacs-packages/pkginfo/*
%{_datadir}/xemacs-packages/info/*
