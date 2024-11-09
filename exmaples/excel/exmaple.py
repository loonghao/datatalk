# Import built-in modules
import os

# Import local modules
from datatalk.core import DataTalk
from datatalk.plugin import load_plugin_from_entry_points


excel_extractor = load_plugin_from_entry_points("datatalk_plugin.providers.excel:ExcelDataProvider")(
    files=["data/数据分析报告-1.xlsx", "data/数据分析报告-2.xlsx"])
project_data_analysis = load_plugin_from_entry_points("datatalk_plugin.analytics.year:YaerDataAnalysis")()
export = load_plugin_from_entry_points("datatalk_plugin.exporters.year:YearDataExporter")(os.path.dirname(__file__))

api = DataTalk(extractor=excel_extractor,
               analyzer=project_data_analysis,
               exporter=export)
api.run()
