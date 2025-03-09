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

    //part 1

    let input_filename=String::from("./input.prod");

    let v = read_input(input_filename);



    let mut l1 = Vec::new();
    let mut l2 = Vec::new();
    for s in &v{
        let mut parts: Vec<_> = s.split_whitespace().collect();
        l1.push(parts[0].parse::<i32>().unwrap());
        l2.push(parts[1].parse::<i32>().unwrap());
    }

    l1.sort();
    l2.sort();

    let mut dist_sum = 0;
    for (a, b) in std::iter::zip(l1,l2) {
        let dist_ab =  a-b;
        dist_sum = dist_sum + dist_ab.abs();
    }
    println!("Part 1: {dist_sum}");




    // part 2
    let input_filename=String::from("./input.prod");

    let v = read_input(input_filename);



    let mut l1 = Vec::new();
    let mut l2 = Vec::new();
    for s in &v{
        let mut parts: Vec<_> = s.split_whitespace().collect();
        l1.push(parts[0].parse::<i32>().unwrap());
        l2.push(parts[1].parse::<i32>().unwrap());
    }

    l1.sort();
    l2.sort();





    let mut total_sim_score = 0;

    for a in l1 {
        let a_count_in_l2 = l2.iter().filter(|&n| *n==a).count() as i32;
        total_sim_score = total_sim_score + a*a_count_in_l2;

    }

    println!("Part 2: {total_sim_score}");


        
}


