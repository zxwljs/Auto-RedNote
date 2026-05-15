
# 此文件是加密逻辑的入口 wrapper
import sys
import os

# 确保当前目录在 sys.path 中，以便能找到 .so 模块
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

import core_publish_xhs_627e49be
from core_publish_xhs_627e49be import *

if __name__ == "__main__":
    try:
        core_publish_xhs_627e49be._skill_entry_point()
    except Exception as e:
        print(f"Skill Execution Error: {e}")
        sys.exit(1)
