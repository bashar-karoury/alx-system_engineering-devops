#!/usr/bin/env ruby

puts ARGV[0].scan(/\[from:(\w+)\].*/).join
puts ","

puts ARGV[0].scan(/\[from:\w+\].*\[to:(.*)\].*\[flags:.*\]\s\[msg/).join
puts ","

puts ARGV[0].scan(/\[from:\w+\].*\[to:.*\].*\[flags:(.*)\]\s\[msg/).join

