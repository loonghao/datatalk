# Import built-in modules
from typing import TypeVar

# Import local modules
from datatalk.analyzer import DataAnalyzer
from datatalk.exporter import DataExporter
from datatalk.extractor import DataExtractor


# Custom Type Variable.
T_ANALYZER = TypeVar("T_ANALYZER", bound=DataAnalyzer)
T_EXTRACTOR = TypeVar("T_EXTRACTOR", bound=DataExtractor)
T_EXPORTER = TypeVar("T_EXPORTER", bound=DataExporter)


class DataTalk:
    def __init__(self, extractor: T_EXTRACTOR, analyzer: T_ANALYZER, exporter: T_EXPORTER):
        self.extractor = extractor
        self.analyzer = analyzer
        self.exporter = exporter

    def extract_data(self) -> dict:
        """Extract data."""
        return self.extractor.extract_data()

    def analyse_data(self, data: dict):
        """Analyse data."""
        return self.analyzer.analyse_data(data)

    def export_data(self, data: dict):
        """Export data."""
        self.exporter.export_data(data)

    def run(self):
        """Run DataTalk."""
        extract_data = self.extract_data()
        analysed_data = self.analyse_data(extract_data)
        self.export_data(analysed_data)
