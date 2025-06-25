"""💮 CIXI PACKAGE 💮 - 老佛爷的关税豁免权"""

import sys
import builtins

# 保存原始的import函数
_original_import = builtins.__import__

# 核心功能：豁免川普税
def _cixi_exemption():
    """内部函数：检测并豁免川普税"""
    # 如果检测到川普税已激活（import被替换）
    if builtins.__import__ is not _original_import:
        # 恢复原始import函数
        builtins.__import__ = _original_import
        print("检测到川普税，但是慈禧已经付过了")
        return True
    return False

# 自定义import拦截器
def _cixi_import(name, globals=None, locals=None, fromlist=(), level=0):
    """自定义import函数，用于拦截tariff包的导入"""
    # 拦截tariff包的导入
    if name == "tariff":
        # 先恢复原始import避免递归问题
        builtins.__import__ = _original_import
        
        # 正常导入tariff包
        module = _original_import(name, globals, locals, fromlist, level)
        
        # 劫持tariff的set()方法
        if hasattr(module, 'set'):
            original_set = module.set
            def patched_set(tariff_sheet):
                print("检测到川普税，但是慈禧已经付过了")
                # 阻止原始关税设置逻辑
            module.set = patched_set
        
        # 重新应用我们的import拦截器
        builtins.__import__ = _cixi_import
        return module
    
    # 其他包正常导入
    return _original_import(name, globals, locals, fromlist, level)

# 主逻辑：启动时自动处理
if "tariff" in sys.modules:
    # 如果川普税已导入，立即豁免
    _cixi_exemption()
else:
    # 设置import拦截器
    builtins.__import__ = _cixi_import

# 导出公共API
__all__ = []
__version__ = "1.0.0"