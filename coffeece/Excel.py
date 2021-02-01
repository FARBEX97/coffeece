import pyexcel as p


def xls_to_xlsx(src_filename,output_filename):
    p.save_book_as(file_name=src_filename + '.xls',
        dest_file_name=output_filename + '.xlsx')


