#!/usr/bin/env ruby
if ARGV.empty?
  puts "Usage: #{ __FILE__ } <name>"
  exit(2)
end

puts ARGV[0].scan(/^\d{10}/).join
