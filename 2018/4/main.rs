#![allow(unused)]

use std::fs;
use std::collections::HashMap;

fn read_input(fname: &String) -> Vec<String> {

    let contents = fs::read_to_string(fname) // returns a Result
        .expect("Should have been able to read the file"); // parses Result and makes String

    let lines: Vec<String> = contents.lines() // returns Line iterable of string literals (str)
        .map(|s:&str| s.to_string()) // map the string literals to Strings
                                     //
        .collect(); // collect the iterable to a Vector of Strings

    lines // return the Vector of Strings
}





fn generate_time_comm(note_line: &String) -> (u64, i32){

    let split: Vec<String> = note_line.split(' ').map(|s:&str| s.to_string()).collect(); 

    let date: Vec<String> = split[0][1..].split('-').map(|s:&str| s.to_string()).collect();
    let time: Vec<String> = split[1][..5].split(':').map(|s:&str| s.to_string()).collect();

    let mut datetime = String::new();

    for d in date{
        datetime += &d
    }

    for t in time{
        datetime += &t
    }


    let comm_flag: char = split[3].clone().chars().next().expect("reason");
    let mut comm = String::new();


    if comm_flag == '#'{
        comm+=&split[3][1..];
    } else if comm_flag == 'a'{
        comm+=&"0";
    } else if comm_flag == 'u'{
        comm+=&"-1";
    } else {panic!()}


    (datetime.parse::<u64>().unwrap(), comm.parse::<i32>().unwrap())
    


}



fn main(){

    let input_filename=String::from("./input.prod");

    let lines = read_input(&input_filename);


    let mut notes: Vec<(u64, i32)> = Vec::new();



    for note_str in lines{
        notes.push(generate_time_comm(&note_str))
    }

    


    notes.sort();

    //println!("Sorted");
    //for note in &notes{
        //println!("{} {}", note.0, note.1);
    //}
    

    let mut guards = HashMap::new(); //make a dictionary
                                     
    for note in &notes{
        if note.1 >0 {
            let mut minutes: [i32; 60] = [0; 60];
            guards.insert( note.1, minutes);
        }
    }



    
    let mut current_id: i32 = 0;
    let mut start_time: u64 = 0;
    let mut stop_time: u64 = 0;
    //let mut diff_time: u64 = 0;

    for note in &notes {

        //println!("{} {}", note.0, note.1);

        if note.1 >0{
            current_id = note.1;
        }

        else if note.1 ==0{
            start_time =note.0;
        }

        else if note.1 ==-1{
            stop_time = note.0;


            let start_i ={start_time % 100}  as usize;
            let end_i = {stop_time % 100 } as usize;


            //println!("{} {}", start_i, end_i);



            let mut minutes = guards[&current_id];

            //println!("BING");
            //println!("{:?}", minutes);
            for i in (start_i..end_i){
                minutes[i] += 1
            }

            //println!("BING");
            //println!("{:?}", minutes);

            guards.insert( current_id, minutes);


        }
    }


    let mut max_time_asleep: i32 = 0;
    let mut sleepy_guard: i32 = 0;

    for (guard, minutes) in &guards{
        let s: i32 = minutes.iter().sum();  
        //println!("{}, {}", guard, s);
        if s > max_time_asleep{
            max_time_asleep = s;
            sleepy_guard = *guard;
        }
    }

    //println!("Sleepiest Guard:");
    //println!("{}", sleepy_guard);



    let mut max_sleep: i32 = 0;
    let mut minute_at_max: i32 = 0;

    for i in (0..60){
        //println!("{}", i);
        //

        let iu: usize = i as usize;

        let times_asleep: &i32 = &guards[&sleepy_guard][iu];
        
        if *times_asleep > max_sleep{
            max_sleep =  *times_asleep;
            minute_at_max = i;
        }
        }

    /*println!("Minute that guard is most asleep at:");*/

    /*println!("{}", minute_at_max);*/
    

    /*println!("{:?}", &guards[&sleepy_guard]);*/

    println!("Part 1:");
    println!("{}", minute_at_max*sleepy_guard);

    









}


