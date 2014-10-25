%define rbname dm-serializer

Summary:	DataMapper plugin for serializing Resources and Collections
Name:		rubygem-%{rbname}
Version:	1.2.2
Release:	1
License:	GPLv2+ or Ruby
Group:		Development/Ruby
URL:		http://github.com/datamapper/%{rbname}
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems
BuildArch:	noarch

%description
DataMapper plugin for serializing Resources and Collections.

%files
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/%{rbname}/xml
%{gem_dir}/gems/%{rbname}-%{version}/lib/%{rbname}/xml/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/%{rbname}/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%doc %{gem_dir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{gem_dir}/gems/%{rbname}-%{version}/LICENSE
%doc %{gem_dir}/doc/%{rbname}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install

