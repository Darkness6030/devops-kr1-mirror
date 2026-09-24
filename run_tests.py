"""Run the coursework tests using only the Python standard library."""
from pathlib import Path
import runpy
import unittest

namespace = runpy.run_path(str(Path(__file__).parent / 'test/test_validator.py'))
suite = unittest.TestSuite(
    unittest.FunctionTestCase(function)
    for name, function in namespace.items() if name.startswith('test_')
)
result = unittest.TextTestRunner(verbosity=2).run(suite)
raise SystemExit(not result.wasSuccessful())
