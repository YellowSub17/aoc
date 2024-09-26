

use std::fs;

use std::collections::HashSet;




fn main(){
    println!("Part one result:");
    part1();

    println!("Part two result:");
    part2();

}


fn part1(){

    let contents = fs::read_to_string("./input.prod")
            .expect("Should have been able to read the file");

    let mut split = contents.rsplit("\n"); //reverse list to put EOF at start
    split.next(); //remove last


    let mut freqcount: i32 = 0; //initialize freq count

    for s in split {
        freqcount += s.parse::<i32>().unwrap();
    }

    println!("{}", freqcount)

}


fn part2(){

    let contents = fs::read_to_string("./input.prod")
            .expect("Should have been able to read the file");

    let mut split: Vec<&str> = contents.split("\n").collect();
    split.retain(|x| *x != "");
    let split_len: usize = split.len();


    let mut freqcount: i32 = 0;
    let mut counter: usize = 0;

    let mut visited = HashSet::<i32>::new();

    loop {

        let current_index: usize = counter % split_len;
        counter +=1;

        let s = split[current_index];
        freqcount += s.parse::<i32>().unwrap();

        if visited.contains(&freqcount){
            break
        }
        else{
            visited.insert(freqcount);
        }
    }
    println!("{}", freqcount)

}


