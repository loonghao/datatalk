# Import built-in modules
import os.path

# Import third-party modules
import xlsxwriter

# Import local modules
from datatalk.exporter import DataExporter


class ExcelExporter(DataExporter):
    output_name = "数据分析报告.xlsx"

    def __init__(self, file_path: str):
        os.makedirs(file_path, exist_ok=True)
        self.file_path = os.path.join(file_path, self.output_name)

    def export_data(self, data):
        print("export data to excel file: {}".format(self.file_path))
        workbook = xlsxwriter.Workbook(self.file_path)
        worksheet = workbook.add_worksheet()
        for row_num, row_data in enumerate(data.items()):
            worksheet.write_column(0, row_num, row_data)
        workbook.close()
