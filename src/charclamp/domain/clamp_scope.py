"""窑筛选范围：整页与局部统一按窑主键精确过滤。

不使用任何模块级可变状态，保证并发请求（两人几乎同时点不同窑剪影）
各自拿到独立的筛选集合，互不串窑。
"""

from __future__ import annotations


def ids_by_primary_key(clamp_id: int) -> list[int]:
    """按窑主键精确过滤，只含该窑本身。"""
    return [clamp_id]
