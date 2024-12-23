# Import local modules
from datatalk.analyzer import DataAnalyzer


class YaerDataAnalysis(DataAnalyzer):

    to_excel = {
        "月份": "",
        "总投入人天": "",
        "项目人天": "",
        "项目占比": "",
        "非项目人天": "",
        "非项目占比": "",
        "项目制作人天": "",
        "项目制作占比": "",
        "项目管理人天": "",
        "项目管理占比": "",

    }
    output_name = "年度数据分析报告.xlsx"



    def analyse_data(self, datas):
        all_data = []
        for index, data in enumerate(datas, 1):
            for  item in data:
                item["月份"] = index
                all_data.append(item)
            # data["月份"] = data["日期"].strftime("%Y-%m")
        # for index, item in enumerate(data, 1):
        #     item["月份"] = index
        #     datas.append(item)
        return all_data
