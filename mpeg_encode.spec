Summary:	Berkeley MPEG-1 Video Encoder
Summary(pl):	Koder obrazu MPEG-1 z Berkeley
Name:		mpeg_encode
Version:	1.5b
Release:	1
License:	BSD
Group:		Applications/Graphics
Source0:	ftp://mm-ftp.cs.berkeley.edu/pub/multimedia/mpeg/encode/%{name}-%{version}-src.tar.gz
Patch0:		ftp://mm-ftp.cs.berkeley.edu/pub/multimedia/mpeg/encode/encode.patch
URL:		http://bmrc.berkeley.edu/frame/research/mpeg/mpeg_encode.html
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

%description -l pl
Ten koder akceptuje dowolny format wej¶ciowy dla którego dostarczysz
skrypt konwertuj±cy ramki na PPM, YUV, JPEG lub JMOVIE. Obróbka pliku
wej¶ciowego opisana jest w pliku doc/INPUT.FORMAT. Opcje kontroluj±ce
obróbkê pliku wej¶ciowego i parametry kompresji s± w pliku parametrów.
Przy czytaniu tego pliku obs³uga b³êdów jest niewielka. Autorzy
sugeruj± by zaczynaæ od przyk³adowego pliku examples/template.param i
modyfikowaæ go. Patrz tak¿e examples/default.param.

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
