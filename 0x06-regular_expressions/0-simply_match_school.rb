#!/usr/bin/env ruby
if ARGV.empty?
  puts "Usage: #{ __FILE__ } <name>"
  exit(2)
end

if ARGV[0].match(/School/)
  puts ARGV[0].match(/School/)
else
  puts
end
