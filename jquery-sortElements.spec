# TODO
# - demo package
%define		plugin	sortElements
Summary:	Sorting elements with jQuery
Name:		jquery-%{plugin}
Version:	0.11
Release:	1
License:	MIT and GPL
Group:		Applications/WWW
Source0:	https://raw.github.com/padolsey/jQuery-Plugins/master/sortElements/jquery.sortElements.js
# Source0-md5:	cf41a4f800d45a4603dba18ea3544ce5
URL:		http://james.padolsey.com/javascript/sorting-elements-with-jquery/
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	closure-compiler
BuildRequires:	js
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
jQuery plugin that would take a sorting function (just like
Array.prototype.sort) as an argument and sort the DOM elements
in-place, and would handle situations where the elements didn't all
have the same parent.

%prep
%setup -qcT
cp -p %{SOURCE0} .

%build
install -d build

# compress .js
js=jquery.%{plugin}.js
out=build/$js
%if 0%{!?debug:1}
closure-compiler --js $js --charset UTF-8 --js_output_file $out
js -C -f $out
%else
cp -p $js $out
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

cp -p build/jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
