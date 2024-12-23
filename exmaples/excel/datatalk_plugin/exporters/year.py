# Import third-party modules
from datatalk_plugin.exporters.excel import ExcelExporter
import xlsxwriter


class YearDataExporter(ExcelExporter):

    output_name = "年度项目数据.xlsx"

    def export_data(self, data):
        print(data)
        print("export data to excel file: {}".format(self.file_path))

        workbook = xlsxwriter.Workbook(self.file_path)
        worksheet = workbook.add_worksheet()
        worksheet.write_row(0, 0, data[0].keys())
        for row_num, row_data in enumerate(data, 1):
            for col_num, (key, value) in enumerate(row_data.items()):
                worksheet.write(row_num, col_num, value)
        workbook.close()
