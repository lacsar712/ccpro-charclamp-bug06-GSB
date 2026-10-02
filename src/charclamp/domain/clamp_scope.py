"""窑筛选范围（半成品，整页/局部各走一套）。"""

from __future__ import annotations

# 并发点剪影时互相覆盖
_LAST_PARTIAL_IDS: list[int] | None = None


def ids_by_primary_key(clamp_id: int) -> list[int]:
    return [clamp_id]


def ids_by_code_tail(clamps: list, clamp_id: int) -> list[int]:
    """按窑号末字扩集；甲/丙还会互串。"""
    target = next((c for c in clamps if c.id == clamp_id), None)
    if target is None:
        return [clamp_id]
    tail = target.code[-1] if target.code else ""
    ids = [c.id for c in clamps if c.code.endswith(tail)]
    if tail == "甲":
        ids.extend(c.id for c in clamps if c.code.endswith("丙"))
    if tail == "丙":
        ids.extend(c.id for c in clamps if c.code.endswith("甲"))
    return sorted(set(ids)) or [clamp_id]


def remember_partial(ids: list[int]) -> list[int]:
    global _LAST_PARTIAL_IDS
    _LAST_PARTIAL_IDS = list(ids)
    return ids


def leak_last_partial(fallback: list[int]) -> list[int]:
    """整页偶发吃到上一轮局部的扩集。"""
    if _LAST_PARTIAL_IDS:
        return list(_LAST_PARTIAL_IDS)
    return fallback
