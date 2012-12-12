import sys
import MySQLdb
from optparse import OptionParser 
from datetime import timedelta, datetime
from random import randrange, choice, shuffle



status_values = ["Answered", "Not Answered", "No ring"]
numbers = ['0','1','2','3','4','5','6','7','8','9','4','7']
def random_date(start, end):

    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return (start + timedelta(seconds=random_second))

if __name__ == "__main__":
    
    parser = OptionParser(usage="usage: python rand_date.py [options]")

    parser.add_option("-s", "--start-date",
                      action="store",
                      dest="start_date",
                      default=datetime.today() - timedelta(days=30),
                      help="Enter starting date-time in the format 'mm/dd/yyyy hh:mm:ss'")

    parser.add_option("-e", "--end-date",
                      action="store",
                      dest="end_date",
                      default=datetime.today(),
                      help="Enter last date-time in the format 'mm/dd/yyyy hh:mm:ss'")

    parser.add_option("-m", "--host",
                      action="store",
                      dest="host",
                      default="localhost",
                      help="Enter host name/ip in which DB is created")

    parser.add_option("-u", "--username",
                      action="store",
                      dest="username",
                      default="root",
                      help="Database username")

    parser.add_option("-p", "--password",
                      action="store",
                      dest="password",
                      default="password",
                      help="Database password")

    parser.add_option("-d", "--database",
                      action="store",
                      dest="database",
                      default="CDR_DB",
                      help="Database name")

    parser.add_option("-c", "--record-count",
                      action="store",
                      dest="record_count",
                      default=10,
                      help="Number of records to be created")

    (options, args) = parser.parse_args()
    print "=" * 40
    print "Start date:", options.start_date
    print "End date:", options.end_date
    print "Host:", options.host
    print "DB user name:", options.username
    print "DB password:", options.password
    print "Database name:", options.database
    print "Record Count:", options.record_count
    print "=" * 40
    try:
        raw_input("Press Enter to continue...")
    except:
        sys.exit(1)

    db = MySQLdb.connect(host=options.host, user=options.username, passwd=options.password, db=options.database)
    cursor = db.cursor()
    d1 = datetime.strptime('12/1/2012 08:08:08', '%m/%d/%Y %H:%M:%S')
    d2 = datetime.strptime('12/31/2012 08:08:08', '%m/%d/%Y %H:%M:%S')
    
    for i in range(int(options.record_count)):
        start_date = random_date(d1, d2)
        duration = randrange(1200)
        status = choice(status_values)
        shuffle(numbers)
        from_number = "".join(numbers)
        shuffle(numbers)
        to_number = "".join(numbers)
        #print "from_number, to_number, status, start_date, duration:", from_number, to_number, status, start_date, duration
        stmt = "INSERT INTO cdr_graph_cdr(from_number, to_number, status, start_time, duration) VALUES(%s,%s,%s,%s,%s)"
        try:
            cursor.execute(stmt, (from_number, to_number, status, start_date, duration))
            db.commit()
        except Exception, e:
            db.rollback()
    print "Inserted %s records" % options.record_count
    db.close()

