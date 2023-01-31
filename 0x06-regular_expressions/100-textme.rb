#!/usr/bin/env ruby
# This script outputs: [SENDER],[RECEIVER],[FLAGS]
# Helps a VoIP Engineer run some statistics on TextMe app text messages transactions
# The sender phone number or name (including country code if present)
# The receiver phone number or name (including country code if present)
# The flags that were used

sender = ARGV[0].scan(/(?<=\[from:)[^ ]+(?=\])/).join
receiver = ARGV[0].scan(/(?<=\[to:)[^ ]+(?=\])/).join
flags = ARGV[0].scan(/(?<=\[flags:)[^ ]+(?=\])/).join
puts "#{sender},#{receiver},#{flags}"
