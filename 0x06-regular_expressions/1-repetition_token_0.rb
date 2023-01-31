#!/usr/bin/env ruby
# script accepts one argument and pass it to a regular expression matching method
# Find the regular expression that will match the cases

puts ARGV[0].scan(/hbt{2,5}n/).join
