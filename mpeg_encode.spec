%define name mpeg_encode
%define prefix /usr
%define version 1.5b.1
%define release 1

Summary:   Berkeley MPEG-1 Video Encoder
Group:     Applications/Graphics
Packager:  Andy Loening <loening@ucla.edu>
Name:      %{name}
Version:   %{version}
Release:   %{release}
Prefix:    %{prefix}
Copyright: Berkeley
URL:       ftp://mm-ftp.cs.berkeley.edu/pub/mpeg
Source:    %{name}-%{version}.tgz
BuildRoot: /tmp/%{name}-%{version}

%description
The encoder will accept any input file format as long as you provide 
a script to convert the images to PPM, YUV, JPEG, or JMOVIE format.  Input 
file processing is described in the file doc/INPUT.FORMAT.  Options to 
control input file processing and compression parameters are specified in 
a parameter file.  Very little error processing is done when reading 
this file.  We suggest you start with the sample parameter file 
examples/template.param and modify it.  See also examples/default.param.

%prep
%setup -n %{name}-%{version}
%build
./configure
make 

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/%{prefix}

##gzip -9 docs/users-guide.ps
##tar cvf - examples | gzip >examples.tar.gz

%clean
if [ -d $RPM_BUILD_ROOT/%{prefix} ] ; then rm -rf $RPM_BUILD_ROOT/%{prefix}; fi

%files
%defattr(-,root,root)
%{prefix}/bin/*
%{prefix}/man/*
##%{prefix}/doc/*



%changelog
* Sun Sep 30 2001 Andy Loening <loening@ucla.edu> 
  [1.5b.1-1]
- restructured the build process, see ChangeLog
- rewrote the .spec file

* Wed Aug 22 2001 Andy Loening <loening@ucla.edu> 
  [1.5b-4]
- one line patch to get it to compile correctly under redhat 7.1 

* Mon Aug 06 2001 Andy Loening <loening@ucla.edu>
  [1.5b-3]
- changes to get the RPM file to compile correctly under redhat 6.2

* Sun May 09 1999 Arne Coucheron <arneco@online.no>
  [1.5b-2]
- using %%{name} and %%{version} macros
- added -q parameter to %setup
- using $RPM_OPT_FLAGS when compiling
- using %defattr macro in %files
