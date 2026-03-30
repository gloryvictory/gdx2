import sys
import os
from pathlib import Path

# Добавляем корень проекта в PYTHONPATH
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))
