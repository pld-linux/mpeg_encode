Summary:	Berkeley MPEG-1 Video Encoder
Summary(pl.UTF-8):	Koder obrazu MPEG-1 z Berkeley
Name:		mpeg_encode
Version:	1.5b
Release:	1
License:	BSD
Group:		Applications/Graphics
Source0:	ftp://mm-ftp.cs.berkeley.edu/pub/multimedia/mpeg/encode/%{name}-%{version}-src.tar.gz
# Source0-md5:	ff125fb82118efc7c852f0d26d5552c6
Patch0:		%{name}-strerror.patch
Patch1:		%{name}-install.patch
Patch2:		%{name}-errno.patch
Patch3:		%{name}-link_jpeg.patch
#Patch0:		ftp://mm-ftp.cs.berkeley.edu/pub/multimedia/mpeg/encode/encode.patch
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

%description -l pl.UTF-8
Ten koder akceptuje dowolny format wejściowy dla którego dostarczysz
skrypt konwertujący ramki na PPM, YUV, JPEG lub JMOVIE. Obróbka pliku
wejściowego opisana jest w pliku doc/INPUT.FORMAT. Opcje kontrolujące
obróbkę pliku wejściowego i parametry kompresji są w pliku parametrów.
Przy czytaniu tego pliku obsługa błędów jest niewielka. Autorzy
sugerują by zaczynać od przykładowego pliku examples/template.param i
modyfikować go. Patrz także examples/default.param.

%prep
%setup -q -c
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p0
# needs some libjpeg API update (from 5 to 6b)
#%patch3 -p0

%build
%{__make} -C mpeg_encode \
	CC="%{__cc}" \
	DEBUGFLAG="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C mpeg_encode install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE COPYRIGHT mpeg_encode/{BUGS,CHANGES,NOTES,README,TODO,examples}
%doc mpeg_encode/docs/{EXTENSIONS,*param*,users-guide.ps,INPUT.FORMAT}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
