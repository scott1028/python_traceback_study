# encoding:utf-8

# This will be easier to understand once you know what attr_accessor does.
# The code attr_accessor :name is equivalent to these two methods (getter and setter)
# def x=(value) as setter, def x as getter

require 'debugger'

class Aa
	# 可以一行一行寫, 都會有效
	attr_accessor :a, :b, :test
	attr_accessor :d

	def initialize
		@test=1
	end
end

class Bb < Aa
	attr_accessor :c
	attr_accessor :p  # 不值

	# 效果如同 attr_accessor
	def x=(value)
		@x=value
	end

	# 兩者加起來恰好就是 attr_accessor :x
	def x
		@x
	end
end

bb=Bb.new

# 可見 attr_accesor 是繼承的增加的
bb.a=1
bb.b=1
bb.c=1
bb.test=100

debugger

# 因為要使用 Debugger 不能最後一行
puts 'exit'
