#!/usr/bin/env ruby

puts ARGV[0].scan(/\[from:\(.*)\].*\[to:.*\].*\[flags:.*\]\s\[msg/).join
puts ","

puts ARGV[0].scan(/\[from:\.*\].*\[to:(.*)\].*\[flags:.*\]\s\[msg/).join
puts ","

puts ARGV[0].scan(/\[from:\.*\].*\[to:.*\].*\[flags:(.*)\]\s\[msg/).join

