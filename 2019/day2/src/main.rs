#![allow(dead_code)]
#![allow(unused_mut)]
#![allow(unused_variables)]
use std::fs::read_to_string;

fn main(){
    println!("PART1");
    let p1out: usize = part1( 12, 2);
    println!("{}", p1out);

    println!("PART2");
    let p2out:usize = part2();
    println!("{}", p2out);

    
}


fn part2() -> usize {
    let target: usize = 19690720;
    let mut out: usize;

    let mut target_noun: usize = 0;
    let mut target_verb: usize = 0;

    'nounloop: for noun in 0..99 {
        for verb in 0..99{
            out = part1(noun, verb);
            //println!("{} {} {}", noun, verb, out);
            if out==target{
                target_noun = noun;
                target_verb = verb;
                break 'nounloop
            }
        }
    }

    //println!("Noun: {}\t Verb: {}", target_noun, target_verb);
    100*target_noun+target_verb


}

fn part1(noun: usize, verb: usize) -> usize {
    let mut memory: Vec<usize> = read_input();

    memory[1] = noun;
    memory[2] = verb;


    let mut inst_pnt = 0;

    while memory[inst_pnt] != 99 {
        //let op: (i32,i32,i32,i32) = (memory[inst_pnt], memory[inst_pnt+1], memory[inst_pnt+2], memory[inst_pnt+3]);
        //let op: [usize;4] = memory[inst_pnt..inst_pnt+4]
            //.try_into()
            //.unwrap();
        
        let op: usize = memory[inst_pnt].try_into().unwrap();

        //println!("{}", v1);


        let jmp: usize = if op==1 {
            let v1: usize = memory[inst_pnt+1].try_into().unwrap();
            let v2: usize = memory[inst_pnt+2].try_into().unwrap();
            let v3: usize = memory[inst_pnt+3].try_into().unwrap();
            memory[v3] = memory[v1] + memory[v2];
            4
        } else if op==2{
            let v1: usize = memory[inst_pnt+1].try_into().unwrap();
            let v2: usize = memory[inst_pnt+2].try_into().unwrap();
            let v3: usize = memory[inst_pnt+3].try_into().unwrap();
            memory[v3] = memory[v1] * memory[v2];
            4
        } else {
            println!("ARRRGGGHHH");
            0
        };

        inst_pnt +=jmp;

    }


    //println!("{}", memory[0]);
    memory[0]

}




fn read_input() -> Vec<usize> {
    read_to_string("./input.prod")
        .unwrap()
        .trim()
        .split(",")
        .map(|s| s.parse::<usize>().unwrap())
        .collect()
}

//fn get_operation() -> (i32, i32, i32, i32){

//}

