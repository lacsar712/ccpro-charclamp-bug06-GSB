"""窑筛选范围。

整页与局部共用同一条件集合：一律按窑主键精确过滤，不做窑号模糊/末字扩集，
也不持有任何跨请求的可变状态（避免并发点不同窑剪影时互相串窑）。
"""

from __future__ import annotations


def ids_by_primary_key(clamp_id: int) -> list[int]:
    """当前筛选命中的窑主键集合，始终只有被点击的那一座窑。"""
    return [clamp_id]
