%define		zope_subname	LinguaPlone
Summary:	Powerful add-on for multilingual content management
Summary(pl.UTF-8):	Dodatek umożliwiający wygodną pracę z wielojęzycznymi serwisami Plone
Name:		Zope-%{zope_subname}
Version:	0.7
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	ec534fe349301a5bbf577b5cfcdf5a6a
URL:		http://sourceforge.net/projects/collective/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CMFPlone >= 2.0.3
Requires:	Zope-PloneLanguageTool >= 0.5
Requires:	Zope-archetypes >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LinguaPlone is a powerful add-on for multilingual content management.

%description -l pl.UTF-8
LinguaPlone jest dodatkiem umożliwiającym wygodną pracę z
wielojęzycznymi serwisami Plone.

%prep
%setup -q -n %{zope_subname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,examples,i18n,skins,tests,*.py,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc README.txt
%{_datadir}/%{name}
