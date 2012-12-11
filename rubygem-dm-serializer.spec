# Generated from dm-serializer-1.2.1.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	dm-serializer

Summary:	DataMapper plugin for serializing Resources and Collections
Name:		rubygem-%{rbname}

Version:	1.2.1
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/datamapper/dm-serializer
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch
Requires:	rubygem-json_pure
Requires:	rubygem-multi_json

%description
DataMapper plugin for serializing Resources and Collections

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/xml
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/xml/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Thu Jan 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.1-1
+ Revision: 769099
- imported package rubygem-dm-serializer

