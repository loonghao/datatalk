# Import built-in modules
import importlib


def load_plugin_from_entry_points(entry_point: str):
    """Load a Plugin class from a given entry point string.

    Examples:
        - load_plugin_from_entry_points("datatalk.provider:Provider")

    Returns:
        Class of the Plugin.

    """
    instance_path, instance = entry_point.split(":")
    module = importlib.import_module(instance_path)
    plugin = getattr(module, instance)
    return plugin
