#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-detroit
Version  : 0.4.0
Release  : 5
URL      : https://rubygems.org/downloads/detroit-0.4.0.gem
Source0  : https://rubygems.org/downloads/detroit-0.4.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: rubygem-detroit-bin
BuildRequires : ruby
BuildRequires : rubygem-detroit-gem
BuildRequires : rubygem-detroit-yard
BuildRequires : rubygem-facets
BuildRequires : rubygem-indexer
BuildRequires : rubygem-qed
BuildRequires : rubygem-rdoc

%description
# Detroit
[Website](http://rubyworks.github.io/detroit) /
[Report Issue](http://github.com/rubyworks/detroit/issues) /
[Development](http://github.com/rubyworks/detroit)

%package bin
Summary: bin components for the rubygem-detroit package.
Group: Binaries

%description bin
bin components for the rubygem-detroit package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n detroit-0.4.0
gem spec %{SOURCE0} -l --ruby > rubygem-detroit.gemspec

%build
gem build rubygem-detroit.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
detroit-0.4.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/detroit-0.4.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/.index
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/EXAMPLE.md
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/HISTORY.md
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/bin/detroit
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit.yml
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/assembly.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/basic_tool.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/basic_utils.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/core_ext.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/core_ext/facets.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/core_ext/filetest.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/core_ext/shell_extensions.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/core_ext/to_actual_filename.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/core_ext/to_console.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/core_ext/to_list.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/core_ext/to_yamlfrag.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/core_ext/unfold_paragraphs.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/email_utils.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/exec.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/project.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/ruby_utils.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/shell_utils.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/toolchain.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/toolchain/cli.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/toolchain/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/toolchain/runner.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/toolchain/script.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/lib/detroit/toolchain/worker.rb
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/man/detroit.1
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/man/detroit.1.html
/usr/lib64/ruby/gems/2.3.0/gems/detroit-0.4.0/man/detroit.1.ronn
/usr/lib64/ruby/gems/2.3.0/specifications/detroit-0.4.0.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/detroit
