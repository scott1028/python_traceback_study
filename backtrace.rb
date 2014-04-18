# encoding:utf-8
# http://ruby-doc.org/core-1.9.3/Exception.html
# 

def a
	raise "boom"
end

def b
	a()
end

# 跟 Python 類似使用 Try-Catch 捕捉 Tracback
begin
	b()
rescue => detail
	puts detail.backtrace.join("\n")
end
