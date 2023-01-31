#!/usr/bin/env ruby
# This script accepts one argument and pass it to a regular expression matching method
# Find the regular expression that will match the cases

puts ARGV[0].scan(/hbt*n/).join
