import day01
import gleam/io
import gleam/string
import simplifile

pub fn read_input(filepath: String) -> String {
  case simplifile.read(filepath) {
    Ok(contents) -> contents
    Error(error) -> {
      io.debug(error)
      ""
    }
  }
}

pub fn main() {
  let input = read_input("input/day01.txt")
  
  "Day 01 - Part 1: "
  |> string.append(day01.part1(input))
  |> io.println

  "Day 01 - Part 2: "
  |> string.append(day01.part2(input))
  |> io.println
}
