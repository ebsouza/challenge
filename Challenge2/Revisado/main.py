# -*- coding: utf-8 -*-
import os, sys, traceback
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler
from apscheduler.schedulers.blocking import BlockingScheduler

from tasks import task1
from aux import greetings, initHandler, initConfig, initFlaskApp


def main(argv):
    greetings()

    print('Press Crtl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    config = initConfig()
    interval_in_minutes = int(config.get('scheduler','IntervalInMinutes'))

    app = initFlaskApp()
    app.logger.warning('Intervalo entre as execucoes do processo: {}'.format(interval_in_minutes))
    db = SQLAlchemy(app)
    
    scheduler = BlockingScheduler()
    scheduler.add_job(task1(db), 'interval', id='task1_job', minutes=interval_in_minutes)

    try:
        scheduler.start()
    except(KeyboardInterrupt, SystemExit):
        pass



if __name__ == '__main__':
    main(sys.argv)