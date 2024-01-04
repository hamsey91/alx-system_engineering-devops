#!/usr/bin/env ruby

input = ARGV[0]

if input.nil?
  puts "Error no argument: Please input an argument string."
else
  puts input.scan(/^\d{10}$/).join
end
