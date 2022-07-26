#!/usr/bin/env ruby
if ARGV.empty?
  puts "Usage: #{ __FILE__ } <name>"
  exit(2)
end

if p ARGV[0] =~ /^School/
  puts ARGV[0]
end
