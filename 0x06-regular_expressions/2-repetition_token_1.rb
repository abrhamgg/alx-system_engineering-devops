#!/usr/bin/env ruby
if ARGV.empty?
  puts "Usage: #{ __FILE__ } <name>"
  exit(2)
end

if ARGV[0].match(/hb?tn/)
  puts ARGV[0].scan(/hb?tn/).join
else
  puts
end
