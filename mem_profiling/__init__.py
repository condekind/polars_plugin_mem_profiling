from __future__ import annotations

from pathlib import Path

import polars as pl

from mem_profiling.utils import register_plugin

from polars._typing import IntoExpr

lib = Path(__file__).parent


def it_allocates_apply_values(expr: IntoExpr) -> pl.Expr:
    return register_plugin(
        args=[expr],
        lib=lib,
        symbol="it_allocates_apply_values",
        is_elementwise=True,
    )


def it_allocates_apply_to_buffer(expr: IntoExpr) -> pl.Expr:
    return register_plugin(
        args=[expr],
        lib=lib,
        symbol="it_allocates_apply_to_buffer",
        is_elementwise=True,
    )


def it_allocates_builder(expr: IntoExpr) -> pl.Expr:
    return register_plugin(
        args=[expr],
        lib=lib,
        symbol="it_allocates_builder",
        is_elementwise=True,
    )


def it_slices_apply_values(expr: IntoExpr) -> pl.Expr:
    return register_plugin(
        args=[expr],
        lib=lib,
        symbol="it_slices_apply_values",
        is_elementwise=True,
    )


def it_slices_apply_to_buffer(expr: IntoExpr) -> pl.Expr:
    return register_plugin(
        args=[expr],
        lib=lib,
        symbol="it_slices_apply_to_buffer",
        is_elementwise=True,
    )


def it_slices_builder(expr: IntoExpr) -> pl.Expr:
    return register_plugin(
        args=[expr],
        lib=lib,
        symbol="it_slices_builder",
        is_elementwise=True,
    )
