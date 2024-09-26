#![allow(unused)]

use std::fs;
use std::collections::HashMap;

fn read_input(fname: &String) -> Vec<String> {

    let contents = fs::read_to_string(fname) // returns a Result
        .expect("Should have been able to read the file"); // parses Result and makes String

    let lines: Vec<String> = contents.lines() // returns Line iterable of string literals (str)
        .map(|s:&str| s.to_string()) // map the string literals to Strings
        .collect(); // collect the iterable to a Vector of Strings

    lines // return the Vector of Strings
}




fn main(){
    let input_filename=String::from("./input.prod");


    // PART 1
    let codes = read_input(&input_filename);

    let mut dubs_count: i32 = 0;
    let mut trips_count: i32 = 0;

    for code in codes{
        let (dubs_flag, trips_flag) = count_dubs_trips(code);
        if dubs_flag{
            dubs_count+=1;
        }
        if trips_flag{
            trips_count +=1;
        }
        //println!("{code} {dubs_flag} {trips_flag}");

    }

    let checksum: i32 = dubs_count*trips_count;
    println!("Part 1:");
    println!("{checksum}");

    //PART 2



    let codes = read_input(&input_filename);

    let mut ans = String::new();
    ans = loop_compare(&codes);

    println!("Part 2:");
    println!("{ans}")
   



}


fn loop_compare(codes: &Vec<String>) -> String{

    for (i_code1, code1) in codes.clone().into_iter().enumerate(){

        let codes2 = &codes.clone()[i_code1+1..];

        for (i_code2, code2) in codes2.into_iter().enumerate(){

            if compare_strings(&code1, &code2){
                return solve_strings(&code1, &code2);
            }

        }
    }

    return String::new();


}


fn solve_strings(code1: &String, code2: &String) -> String{

    let mut s = String::new();

    for (s1, s2) in code1.chars().zip(code2.chars()){

        if s1 == s2{
            s.push(s1)
        }
    }

    s


}


fn compare_strings(code1: &String, code2: &String) -> bool{


    let mut wrong_count: i32 = 0;

    for (s1, s2) in code1.chars().zip(code2.chars()){


        if s1 != s2{
            wrong_count +=1;
        }

        if wrong_count > 1{
            return false
        }

    }

    return true
}



fn count_dubs_trips(code: String) -> (bool, bool){

    let mut scores = HashMap::new(); //make a dictionary
    for s in code.chars(){ // for each char in the code
    //get the current score for the char, or set it to 0 if it doesnt exist yet
        let score =scores.entry(s).or_insert(0);
        *score +=1;//add one to the score (setting the 0 to 1 if unset)
    }

    //flags for doubles or triples
    let mut dubs_flag = false;
    let mut trips_flag = false;

    // for each occourence in the code
    for (key, value) in scores {
        //if the score is two, set the flag true
        if value ==2{
            dubs_flag = true;
        //if the score is 3, set the flag true
        } else if value==3{
            trips_flag = true;
        }
    }

    // return the flags
    (dubs_flag, trips_flag)

}








