# encoding:utf-8

require 'logger'

logger = Logger.new(STDOUT)
logger.level = Logger::DEBUG

logger.debug("Created logger")
logger.info("Program started")
logger.warn("Nothing to do!")

path = "a_non_existent_file"

begin
	File.foreach(path) do |line|
		unless line =~ /^(\w+) = (.*)$/
			logger.error("Line in wrong format: #{line.chomp}")
		end
	end
rescue => err
	logger.fatal("Caught exception; exiting")
	logger.fatal(err)

	puts '*'*50
	puts err.backtrace.join("\n")
	puts '*'*50

end

# The levels are:
# 	UNKNOWN
# 		An unknown message that should always be logged.

# 	FATAL
# 		An unhandleable error that results in a program crash.

# 	ERROR
# 		A handleable error condition.

# 	WARN
# 		A warning.

# 	INFO
# 	G	eneric (useful) information about system operation.

# 	DEBUG
# 		Low-level information for developers.
