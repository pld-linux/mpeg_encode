Summary:	Berkeley MPEG-1 Video Encoder
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Group(pt):	Aplicações/Gráficos
Name:		mpeg_encode
Version:	1.5b
Release:	1
License:	BSD
URL:		http://bmrc.berkeley.edu/frame/research/mpeg/mpeg_encode.html
Source0:	ftp://mm-ftp.cs.berkeley.edu/pub/multimedia/mpeg/encode/%{name}-%{version}-src.tar.gz
Patch0:		ftp://mm-ftp.cs.berkeley.edu/pub/multimedia/mpeg/encode/encode.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The encoder will accept any input file format as long as you provide a
script to convert the images to PPM, YUV, JPEG, or JMOVIE format.
Input file processing is described in the file doc/INPUT.FORMAT.
Options to control input file processing and compression parameters
are specified in a parameter file. Very little error processing is
done when reading this file. We suggest you start with the sample
parameter file examples/template.param and modify it. See also
examples/default.param.

%prep
%setup -q -n %{name}-%{version}
%patch -p1

%build
./configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT/%{_prefix}

##gzip -9 docs/users-guide.ps
##tar cvf - examples | gzip >examples.tar.gz

%clean
if [ -d $RPM_BUILD_ROOT/%{prefix} ] ; then rm -rf $RPM_BUILD_ROOT/%{prefix}; fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*
##%{prefix}/doc/*
