%define		zope_subname	LinguaPlone
Summary:	Powerful add-on for multilingual content management
Summary(pl):	Dodatek umo¿liwiaj±cy wygodn± pracê z wielojêzycznymi serwisami Plone
Name:		Zope-%{zope_subname}
Version:	0.7
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	ec534fe349301a5bbf577b5cfcdf5a6a
URL:		http://sourceforge.net/projects/collective/
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildRequires:  python
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-archetypes >= 1.3
Requires:	Zope-PloneLanguageTool >= 0.5
Requires:	Zope-CMFPlone >= 2.0.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LinguaPlone is a powerful add-on for multilingual content management.

%description -l pl
LinguaPlone jest dodatkiem umo¿liwiaj±cym wygodn± pracê z
wielojêzycznymi serwisami Plone.

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
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc README.txt
%{_datadir}/%{name}
