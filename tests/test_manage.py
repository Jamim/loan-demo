import runpy
from unittest.mock import patch

import django
import pytest

from manage import main


@patch('sys.argv', ['manage.py', '--version'])
def test_manage_main(capsys):
    runpy.run_module('manage', run_name='__main__')
    captured = capsys.readouterr()
    assert captured.out == f'{django.__version__}\n'


@patch('builtins.__import__', side_effect=ImportError)
def test_manage_main_import_error(management):
    del management.execute_from_command_line
    with pytest.raises(ImportError, match="Couldn't import"):
        main()
