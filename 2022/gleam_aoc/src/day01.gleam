import gleam/int
import gleam/list
import gleam/result
import gleam/string

pub fn part1(input: String) -> String {
  let find_substraction = fn(x) { int.absolute_value(x - 2020) }

  let values =
    input
    |> string.split("\r\n")
    |> list.map(int.parse)
    |> result.values

  let substractions =
    values
    |> list.map(find_substraction)

  let result =
    values
    |> list.filter(fn(x) { list.contains(substractions, x) })
    |> list.map(fn(x) { x * { 2020 - x } })
    |> list.first

  case result {
    Ok(x) -> int.to_string(x)
    Error(Nil) -> "No result"
  }
}

pub fn part2(input: String) -> String {
  let values =
    input
    |> string.split("\r\n")
    |> list.map(int.parse)
    |> result.values

  let response =
    values
    |> list.combinations(3)
    |> list.filter(fn(x) {
      let sum = list.reduce(x, fn(y, acc) { y + acc })
      case sum {
        Ok(2020) -> True
        _ -> False
      }
    })
    |> list.first
    |> result.unwrap([])
    |> list.reduce(fn(x, acc) { x * acc })

  case response {
    Ok(x) -> int.to_string(x)
    Error(Nil) -> "No result"
  }
}
