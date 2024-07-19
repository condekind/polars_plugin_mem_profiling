use polars::export::arrow::array::MutablePlString;
use polars::prelude::*;
use pyo3_polars::derive::polars_expr;
use std::borrow::Cow;
use std::fmt::Write;

fn third_party_function_which_allocates(val: &str) -> String {
    format!("{}-suffix", val)
}

fn third_party_function_which_doesnt_allocate(val: &str) -> &str {
    &val[1..]
}

#[polars_expr(output_type=String)]
fn it_allocates_apply_values(inputs: &[Series]) -> PolarsResult<Series> {
    let s = &inputs[0];
    let ca = s.str()?;
    let out: StringChunked = ca.apply_values(|val| {
        let res = Cow::Owned(third_party_function_which_allocates(val));
        res
    });
    Ok(out.into_series())
}

#[polars_expr(output_type=String)]
fn it_allocates_apply_to_buffer(inputs: &[Series]) -> PolarsResult<Series> {
    let s = &inputs[0];
    let ca = s.str()?;
    let out: StringChunked = ca.apply_to_buffer(|val, buf| {
        write!(buf, "{}", third_party_function_which_allocates(val)).unwrap();
    });
    Ok(out.into_series())
}

#[polars_expr(output_type=String)]
fn it_allocates_builder(inputs: &[Series]) -> PolarsResult<Series> {
    let s = &inputs[0];
    let ca = s.str()?;
    let chunks = ca.downcast_iter().map(|arr| {
        let mut buf = String::new();
        let mut mutarr = MutablePlString::with_capacity(arr.len());
        arr.iter().for_each(|opt| match opt {
            None => mutarr.push_null(),
            Some(v) => {
                buf.clear();
                let val = third_party_function_which_allocates(v);
                write!(buf, "{val}").unwrap();
                mutarr.push_value(&buf.as_str())
            }
        });
        mutarr.freeze()
    });
    let out = StringChunked::from_chunk_iter("", chunks);
    Ok(out.into_series())
}

#[polars_expr(output_type=String)]
fn it_slices_apply_values(inputs: &[Series]) -> PolarsResult<Series> {
    let s = &inputs[0];
    let ca = s.str()?;
    let out: StringChunked = ca.apply_values(|val| {
        let res = Cow::Borrowed(third_party_function_which_doesnt_allocate(val));
        res
    });
    Ok(out.into_series())
}

#[polars_expr(output_type=String)]
fn it_slices_apply_to_buffer(inputs: &[Series]) -> PolarsResult<Series> {
    let s = &inputs[0];
    let ca = s.str()?;
    let out: StringChunked = ca.apply_to_buffer(|val, buf| {
        write!(buf, "{}", third_party_function_which_doesnt_allocate(val)).unwrap();
    });
    Ok(out.into_series())
}

#[polars_expr(output_type=String)]
fn it_slices_builder(inputs: &[Series]) -> PolarsResult<Series> {
    let s = &inputs[0];
    let ca = s.str()?;
    let chunks = ca.downcast_iter().map(|arr| {
        let mut buf = String::new();
        let mut mutarr = MutablePlString::with_capacity(arr.len());
        arr.iter().for_each(|opt| match opt {
            None => mutarr.push_null(),
            Some(v) => {
                buf.clear();
                let val = third_party_function_which_doesnt_allocate(v);
                write!(buf, "{val}").unwrap();
                mutarr.push_value(&buf.as_str())
            }
        });
        mutarr.freeze()
    });
    let out = StringChunked::from_chunk_iter("", chunks);
    Ok(out.into_series())
}
