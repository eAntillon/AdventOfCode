import gleam/int
import gleam/io
import gleam/list
import gleam/result
import gleam/string

pub fn parse(input: String) -> List(List(Int)) {
  string.split(input, "\r\n")
  |> list.map(fn(line) {
    string.split(line, " ")
    |> list.map(int.parse)
    |> result.values
  })
}

pub fn get_expected_direction(input: List(Int)) -> RowDirection {
  case list.first(input), list.last(input) {
    Ok(x), Ok(y) if x > y -> Decreasing
    Ok(x), Ok(y) if x < y -> Increasing
    _, _ -> Neither
  }
}

pub type RowDirection {
  Increasing
  Decreasing
  Neither
}

pub fn pt_1(input: List(List(Int))) {
  list.filter(input, fn(row: List(Int)) -> Bool {
    let expected_direction = get_expected_direction(row)
    let validation_result =
      list.reduce(row, fn(prev, current) {
        let abs_diff = int.absolute_value(prev - current)
        case expected_direction {
          Increasing if prev < current && abs_diff >= 1 && abs_diff <= 3 ->
            current
          Decreasing if prev > current && abs_diff >= 1 && abs_diff <= 3 ->
            current
          _ -> 0
        }
      })
    let last_row_element = list.last(row)
    case validation_result {
      x if x == last_row_element -> True
      _ -> False
    }
  })
  |> list.length
}

pub fn pt_2(input: List(List(Int))) {
  list.filter(input, fn(row: List(Int)) -> Bool {
    io.debug("_________________________")
    io.debug(row)
    let expected_direction = get_expected_direction(row)
    io.debug(expected_direction)
    let first = list.first(row) |> result.unwrap(0)
    let new_row = list.rest(row) |> result.unwrap([])

    let first_validation =
      list.try_fold(new_row, first, fn(prev, current) {
        let abs_diff = int.absolute_value(prev - current)
        case expected_direction {
          Increasing if prev < current && abs_diff >= 1 && abs_diff <= 3 ->
            Ok(current)
          Increasing -> Error(current)
          Decreasing if prev > current && abs_diff >= 1 && abs_diff <= 3 ->
            Ok(current)
          Decreasing -> Error(prev)
          _ -> Error(prev)
        }
      })

    let second_validation = case first_validation {
      Ok(x) -> x
      Error(x) -> {
        let #(_, new_row) = {
          list.pop(row, fn(i) { x == i }) |> result.unwrap(#(0, []))
        }
        io.debug("removing item: " <> int.to_string(x))
        io.debug(new_row)
        let first = list.first(new_row) |> result.unwrap(0)
        let new_row = list.rest(new_row) |> result.unwrap([])
        list.try_fold(new_row, first, fn(prev, current) {
          let abs_diff = int.absolute_value(prev - current)
          case expected_direction {
            Increasing if prev < current && abs_diff >= 1 && abs_diff <= 3 ->
              Ok(current)
            Decreasing if prev > current && abs_diff >= 1 && abs_diff <= 3 ->
              Ok(current)
            _ -> Error(prev)
          }
        })
        |> result.unwrap(0)
      }
    }
    let last_row_element = list.last(row) |> result.unwrap(0)

    let result = case second_validation {
      0 -> False
      x if x == last_row_element -> True
      _ -> False
    }
    io.debug(result)
    result
  })
  |> list.length
}
