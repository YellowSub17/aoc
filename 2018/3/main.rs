#![allow(unused)]

use std::fs;

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


    //PART 1


    let width:usize = 1000;
    let height:usize = 1000;

    let mut fabric = vec![vec![0; width]; height];

    let rects = read_input(&input_filename);


    for rect in &rects{

        let (id, col, row, width, height): (i32,i32,i32,i32,i32) = split_line(&rect);
    
        let i_start: usize = row as usize;
        let i_stop: usize = {row + height} as usize;

        let j_start: usize = col as usize;
        let j_stop: usize = {col + width} as usize;

        for i in (i_start..i_stop){
            for j in (j_start..j_stop){
                fabric[i][j] +=1;
            }
        }
    }


    let mut counter: i32 = 0;

    for row in &fabric{
        for val in row{
            if *val >1{
                counter +=1; }
        }
    }

    println!("Part 1:");
    println!("{}", counter);



    //Part 2:
    

    let mut correct_id: i32 = -1;
    'rectloop: for rect in &rects{

        let (id, col, row, width, height): (i32,i32,i32,i32,i32) = split_line(&rect);
    
        let i_start: usize = row as usize;
        let i_stop: usize = {row + height} as usize;

        let j_start: usize = col as usize;
        let j_stop: usize = {col + width} as usize;


        for i in (i_start..i_stop){
            for j in (j_start..j_stop){
                //println!("{}", fabric[i][j]);
                if fabric[i][j] >1{;
                    continue 'rectloop;
                }
            }
        }
        correct_id = id;

         
    }

    //1281 too high
    println!("Part 2:");
    println!("{}", correct_id);




}


fn split_line(line: &String) -> (i32, i32, i32, i32, i32){


    let split :Vec<String> = line.split(' ').map(|s:&str| s.to_string()).collect(); 

    let id: &i32 = &{&split[0]}[1..].parse::<i32>().unwrap();

    let colrow_split :Vec<String> = split[2].split(',').map(|s:&str| s.to_string()).collect();
    let col: &i32 = &colrow_split[0].parse::<i32>().unwrap();
    let row_len: usize = colrow_split[1].len();
    let row: &i32 = &{&colrow_split[1]}[..row_len-1].parse::<i32>().unwrap();

    let wh_split: Vec<String> = split[3].split('x').map(|s:&str| s.to_string()).collect();

    let width: &i32 = &wh_split[0].parse::<i32>().unwrap();
    let height: &i32 = &wh_split[1].parse::<i32>().unwrap();

    (*id, *col, *row, *width, *height)

}


