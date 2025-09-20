#![allow(dead_code)]
#![allow(unused_mut)]
#![allow(unused_variables)]

use std::fs::read_to_string;


struct Point {
    x: i32,
    y: i32,
}

struct Segment {
    p1: Point,
    p2: Point
}

struct Instruction {
    card: char,
    mag: usize,
}


fn main() {
    println!("Hello, world!");
    let (w1, w2) = read_wires();
    
    let pos1 = gen_pos(w1);
    let pos2 = gen_pos(w2);
    let x = cmp_pos(pos1, pos2);
    
    //let w1corners = gen_corners(w1);
    /*let w2corners = gen_corners(w2);*/

    /*let out = cmp_corners(w1corners, w2corners);*/
}


fn split_inst(inst: String) -> (String, usize){
    let mut chars = inst.chars();
    let card = chars.next().unwrap().to_string();
    let mag: usize = chars.collect::<String>().parse().unwrap();
    (card, mag)
}

fn read_wires() -> (Vec<String>, Vec<String>) {
    let input = read_to_string("./input.prod").unwrap();

    let mut lines = input.lines();

    let w1: Vec<String> = lines.next()
                             .unwrap()
                             .split(",")
                             .map(|s| s.to_string())
                             .collect();

    let w2: Vec<String> = lines.next()
                             .unwrap()
                             .split(",")
                             .map(|s| s.to_string())
                             .collect();

    (w1, w2)

}




fn cmp_pos( pos1: Vec<(i32, i32)>, pos2: Vec<(i32, i32)>) -> Vec<(i32, i32)> {

    let mut out: Vec< (i32, i32)> = vec![];

    for p1 in pos1.clone() {
        for p2 in pos2.clone() {
            if p1.0==p2.0 && p1.1==p2.1{
                out.push( (p1.0, p1.1) );
                println!("found! {} {}", p1.0, p1.1);
            }
        }
    }
    out
}

fn gen_pos(w: Vec<String> ) -> Vec<(i32, i32)> {

    let mut current_x: i32 = 0;
    let mut current_y: i32 = 0;

    let mut out: Vec< (i32, i32)> = vec![];
    out.push( (0, 0) );

    for (card, mag) in w.into_iter().map( |inst| split_inst(inst)){
        //println!("{}", card);

        if card == "U" {
            for _ in 1..mag+1 {
                current_y += 1;
                out.push( (current_x, current_y) );
            }
        } else if card == "D" {
            for _ in 1..mag+1 {
                current_y -= 1;
                out.push( (current_x, current_y) );
            }
        } else if card == "L" {
            for _ in 1..mag+1 {
                current_x -= 1;
                out.push( (current_x, current_y) );
            }
        } else if card == "R" {
            for _ in 1..mag+1 {
                current_x += 1;
                out.push( (current_x, current_y) );
            }
        } else {
            println!("AAAARRRGGGHHH");
        };
    }

    out


}




fn cmp_corners( w1corners: Vec<(i32, i32)>, w2corners: Vec<(i32, i32)>) -> Vec<(i32, i32)> {
    
    let mut out: Vec< (i32, i32)> = vec![];

    for w1window in w1corners.windows(2) {
        let (w1p1, w1p2) = (&w1window[0], &w1window[1]);
        for w2window in w2corners.windows(2) {
            let (w2p1, w2p2) = (&w2window[0], &w2window[1]);
            //println!("{} {} {} {} ", w1p1.0, w1p2.0, w2p1.0, w2p2.0)

        }

    }
    out



}





fn gen_corners(w: Vec<String>) -> Vec<(i32, i32)>{

    let mut current_x: i32 = 0;
    let mut current_y: i32 = 0;

    let mut out: Vec< (i32, i32)> = vec![];

    out.push( (0, 0) );

    for (card, mag) in w.into_iter().map( |inst| split_inst(inst)){

        if card == "U" {
            current_y += mag as i32;
        } else if card == "D" {
            current_y -= mag as i32;
        } else if card == "L" {
            current_x -= mag as i32;
        } else if card == "R" {
            current_x += mag as i32;
        }
        out.push( (current_x, current_y) );
    }

    out
}

