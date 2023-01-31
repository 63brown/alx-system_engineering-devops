#!/usr/bin/env ruby
# script that accepts one argument and pass it to a regular expression matching method
# must match school

puts ARGV[0].scan(/School/).join
