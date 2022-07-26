#!/usr/bin/env ruby
if ARGV.empty?
  puts "Usage: #{ __FILE__ } <name>"
  exit(2)
end

if ARGV[0].match(/hbt{2,5}n/)
  puts ARGV[0].scan(/hbt{2,5}n/).join
else
  puts
end
