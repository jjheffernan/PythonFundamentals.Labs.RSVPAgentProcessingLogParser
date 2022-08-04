import re
import datetime
# enter data directory, iterate through 'rsvp_agent_log.dat' and look for log level WARNING.
# When WARNING is produced, output:
#   the date and time of the entry
#   followed by a ' -- '
#   then the error message
#       the error message should exclude colons and whats between them

spec_dir = './data/'  # specified directory
filename = 'rsvp_agent_log.dat'  # manually declare specified file
log_directory = {}  # dictionary of all logs within file


# parse .dat line and split into list of string terms
def parse_line(line):
    pass


# open the file and read into python object
def read_file(filename):
    pass


# get time of flagged event
def get_timestamp(event_name):
    pass


# main loop
def main():
    pass  # escape pass


if __name__ == '__main__':
    main()
