import datetime
from params import args

logmsg = ''
timemark = dict()
saveDefault = False

def log(msg, log_path=args.log_path, save=None, oneline=False, bold=False):
    global logmsg
    global saveDefault
    time = datetime.datetime.now()
    tem = '%s: %s' % (time, msg)
    save_file = open(log_path, 'a')

    if save != None:
        if save:
            logmsg += tem + '\n'
    elif saveDefault:
        logmsg += tem + '\n'

    if bold:
        tem = '\033[1m' + tem + '\033[0m'

    if oneline:
        print(tem, end='\r')
        save_file.write(tem.join('\n'))
    else:
        print(tem)
        save_file.write(tem)

if __name__ == '__main__':
    log('')
