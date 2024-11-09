# Import built-in modules
import importlib
import pkgutil

# Import local modules
import datatalk


def test_imports():
    """Test import modules."""
    prefix = "{}.".format(datatalk.__name__)
    iter_packages = pkgutil.walk_packages(
        datatalk.__path__,
        prefix,
    )
    for _, name, _ in iter_packages:
        module_name = name if name.startswith(prefix) else prefix + name
        importlib.import_module(module_name)
