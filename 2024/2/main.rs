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


fn check_all_incdec(levels:Vec<i32>){



}


fn main(){

  
    //part 1

    let input_filename=String::from("./input.prod");

    let reports = read_input(input_filename);


    let mut safe_count = 0;
    'reports_loop: for report in reports{

        let levels:Vec<_> = report.split_whitespace().map(|s| s.parse::<i32>().unwrap()).collect();

        safe_count = safe_count + test_levels(levels);

    }

    println!("SAFE COUNT: {safe_count}");

    //part 2

    let input_filename=String::from("./input.prod");

    let reports = read_input(input_filename);

    let mut safe_count = 0;
    'reports_loop: for report in reports{

        let levels:Vec<_> = report.split_whitespace().map(|s| s.parse::<i32>().unwrap()).collect();

        safe_count = safe_count + test_levels2(levels);

    }

    println!("SAFE COUNT: {safe_count}");





        
}



fn test_levels2(levels:Vec<i32>) -> i32{

    if test_levels(levels.clone()) == 1 { 1 }
    else {
        for i in 0..levels.len() {
            let mut new_levels = levels.to_vec();
            new_levels.remove(i);
            if test_levels(new_levels) == 1 { return 1;}
            else {continue}
        }
    0

    }
    

}


fn test_levels(levels:Vec<i32>) -> i32{


    let mut inc_dec = Vec::new();


    'levels_loop: for i in 0..levels.len()-1 {
        
        
        let a = levels[i].clone();
        let b = levels[i+1].clone();

        let dist = a - b;



        if (dist.abs() > 3) | (dist.abs() < 1) {
            inc_dec.push(0);
            break
        }

        if dist < 0{ inc_dec.push(1)}
        else { inc_dec.push(-1)}

    }

    let inc_dec_sum: i32 = inc_dec.iter().sum();
    let max_incs: i32 = (levels.len() as i32)-1;

    if inc_dec_sum.abs() == max_incs {1}
    else {0}



}




