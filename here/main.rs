#![allow(unused)]

use std::fs;

fn read_input(fname: String) -> Vec<String> {

    let contents = fs::read_to_string(fname) // returns a Result
        .expect("Should have been able to read the file"); // parses Result and makes String

    let lines: Vec<String> = contents.lines() // returns Line iterable of string literals (str)
        .map(|s:&str| s.to_string()) // map the string literals to Strings
        .collect(); // collect the iterable to a Vector of Strings

    lines // return the Vector of Strings
}




fn main(){

    let input_filename=String::from("./input.prod");

    let v = read_input(input_filename);

    for s in v{
        println!("{}", s)
    }

}


