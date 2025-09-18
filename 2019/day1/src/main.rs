#![allow(dead_code)]
#![allow(unused_mut)]
#![allow(unused_variables)]

use std::fs::read_to_string;
use std::cmp;

fn main() {
    part2();
}

fn part2(){

    let mut total_counter: i32 = 0;



    for line in read_to_string("./input.prod").unwrap().lines(){
        //println!("####{}", line);

        let mut this_module_fuel: i32 = 0;
        let mut this_module_mass: i32 = line.trim().parse::<i32>().unwrap();
        

        total_counter += fuelreq(this_module_mass);
        while this_module_mass > 0 {

            this_module_mass = fuelreq(this_module_mass);

            //println!("#{}", this_module_mass);
            total_counter += fuelreq(this_module_mass);
        };


    };


    //for line in read_to_string("./input.prod").unwrap().lines(){
        //counter += fuelreq(line.trim().parse::<i32>().unwrap());            
    //};
    println!("{}", total_counter);

}


fn part1() {
    println!("Hello, world!");

    let mut counter: i32 = 0;

    println!("{}", fuelreq(100756));

    for line in read_to_string("./input.prod").unwrap().lines(){
        counter += fuelreq(line.trim().parse::<i32>().unwrap());            
    };
    println!("{}", counter);
}


fn fuelreq(m: i32) -> i32 {
    cmp::max(m/3 -2, 0)
}
