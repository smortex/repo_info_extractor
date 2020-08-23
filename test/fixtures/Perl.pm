package Perl::Sample;

# import with use
use strict;
use Benchmark;
use Carp 'croak';
use sigtrap qw(SEGV BUS);
use Sub::Module;
use Import::This 12.34;

# conditional imports
use if $] < 5.008, "utf8";
use if WANT_WARNINGS, warnings => qw(all);

# include with require
require Foo::Bar;
BEGIN { require Module; Module->import(LIST); }

# versions
use v5.32.0;
use 5.30.3;
use 5.028_003;

require v5.26.3;
require 5.24.4;
require 5.022_004;

# use Should::Not::Match;

=pod

Documentation lines about how to use this module should not match.

=cut
