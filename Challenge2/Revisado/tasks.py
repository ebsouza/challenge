import os, xlsxwriter
from datetime import datetime

def init_worksheet(workbook, index):
    worksheet = workbook.add_worksheet()

    worksheet.write('A{0}'.format(index),'Id')
    worksheet.write('B{0}'.format(index),'Name')
    worksheet.write('C{0}'.format(index),'Email')
    worksheet.write('D{0}'.format(index),'Password')
    worksheet.write('E{0}'.format(index),'Role Id')
    worksheet.write('F{0}'.format(index),'Created At')
    worksheet.write('G{0}'.format(index),'Updated At')

    return worksheet


def write_in_worksheet(worksheet, order, index):
    print('Id: {0}'.format(order[0]))
    worksheet.write('A{0}'.format(index),order[0])
    print('Name: {0}'.format(order[1]))
    worksheet.write('B{0}'.format(index),order[1])
    print('Email: {0}'.format(order[2]))
    worksheet.write('C{0}'.format(index),order[2])  
    print('Password: {0}'.format(order[3]))
    worksheet.write('D{0}'.format(index),order[3])  
    print('Role Id: {0}'.format(order[4]))
    worksheet.write('E{0}'.format(index),order[4])   
    print('Created At: {0}'.format(order[5]))
    worksheet.write('F{0}'.format(index),order[5])  
    print('Updated At: {0}'.format(order[6]))
    worksheet.write('G{0}'.format(index),order[6])


def task1(db):

    file_name = 'data_export_{0}.xlsx'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    file_path = os.path.join(os.path.curdir, file_name)
    workbook = xlsxwriter.Workbook(file_path)

    index = 1
    worksheet = init_worksheet(workbook, index)

    orders = db.session.execute('SELECT * FROM users;')

    for order in orders:
        index = index + 1
        write_in_worksheet(worksheet, order, index)

    workbook.close()
    print('job executed!')