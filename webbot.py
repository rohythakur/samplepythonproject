import twill
import twill.commands as c

def login():
    c.clear_cookies()
    c.go('http://icfpcontest.org/icfp10/login')
    c.fv(1, 'j_username', 'Side Effects May Include...')
    c.fv(1, 'j_password', '<redacted>')
    c.submit()
    c.save_cookies('/tmp/icfp.cookie')

all_cars_rx = re.compile(r'<td style="width: 20%;">(\d+)</td><td>(\d+)</td>')
def list_cars():
    c.go('http://icfpcontest.org/icfp10/score/instanceTeamCount')
    cars = re.findall(all_cars_rx, c.show())
    if not cars:
        sys.stderr.write(c.show())
        sys.stderr.write('Could not find any cars')
    return cars;
