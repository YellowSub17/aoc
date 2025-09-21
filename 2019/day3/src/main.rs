#![allow(dead_code)]
#![allow(unused_mut)]
#![allow(unused_variables)]

use std::fs::read_to_string;

#[derive(Clone, Debug,Copy)]
struct Point {
    x: i32,
    y: i32,
}

#[derive(Clone, Debug,Copy)]
struct Segment {
    p1: Point,
    p2: Point,
}

#[derive(Clone, Debug)]
struct Instruction {
    card: String,
    mag: i32,
}


fn main() {
    println!("Hello, world!");
    let input = read_to_string("./input.prod").unwrap();
    let mut lines = input.lines();

    let w1: Vec<Instruction> = lines.next()
                             .unwrap()
                             .split(",")
                             .map(|s| s.to_string())
                             .map(split_inst)
                             .collect();

    let w2: Vec<Instruction> = lines.next()
                             .unwrap()
                             .split(",")
                             .map(|s| s.to_string())
                             .map(split_inst)
                             .collect();
    


    let w1corners = gen_corners(&w1);
    let w2corners = gen_corners(&w2);
    let min_int = find_wire_intersections(&w1corners,&w2corners)
                        .into_iter()
                        .map(manhat_dist)
                        .min()
                        .unwrap();

    println!("PART1: {}",min_int);

    

    let pos1 = gen_pos(&w1);
    let pos2 = gen_pos(&w2);


    for interseciton in find_wire_intersections(&w1corners, &w2corners){
        println!("{:?}", interseciton);

        let mut tp1: u32 = 0;
        let mut tp2: u32 = 0;
        for pos in &pos1 {
            if pos.x==interseciton.x && pos.y==interseciton.y{
                println!("{}", tp1);
                break
            }
            tp1+=1;
        }
        for pos in &pos2 {
            if pos.x==interseciton.x && pos.y==interseciton.y{
                println!("{}", tp2);
                break
            }
            tp2+=1;
        }

        println!("SUM: {}", tp1+tp2);


    }



}

fn manhat_dist(p: Point) -> u32{
    (p.x.abs()+p.y.abs()).try_into().unwrap()
}


fn split_inst(inst: String) -> Instruction {
    let mut chars = inst.chars();
    let card = chars.next().unwrap().to_string();
    let mag: i32 = chars.collect::<String>().parse().unwrap();
    Instruction{card:card , mag:mag}
}



fn calc_seg_intersection( s1: Segment, s2: Segment) -> Option<Point>{

    let s1minx = s1.p1.x.min(s1.p2.x);
    let s1maxx = s1.p1.x.max(s1.p2.x);

    let s2minx = s2.p1.x.min(s2.p2.x);
    let s2maxx = s2.p1.x.max(s2.p2.x);
    let s1miny = s1.p1.y.min(s1.p2.y);
    let s1maxy = s1.p1.y.max(s1.p2.y);

    let s2miny = s2.p1.y.min(s2.p2.y);
    let s2maxy = s2.p1.y.max(s2.p2.y);


    if s1.p1.x ==s1.p2.x && s2.p1.x == s2.p2.x { //both horizontal
        return None
    } else if s1.p1.y ==s1.p2.y && s2.p1.y == s2.p2.y { //both vertical
        return None
    }

    else if s1.p1.y == s1.p2.y && s2.p1.x == s2.p2.x { // s1 horzi, s2 verti
        let s1s2inter = Point{x: s2.p1.x, y: s1.p1.y};
        if (s1minx..s1maxx).contains(&s1s2inter.x) && (s2miny..s2maxy).contains(&s1s2inter.y) {
            return Some(s1s2inter)
        }
    }

    else if s1.p1.x == s1.p2.x && s2.p1.y == s2.p2.y { // s2 horzi, s1 verti
        let s1s2inter = Point{x: s1.p1.x, y: s2.p1.y};
        if (s2minx..s2maxx).contains(&s1s2inter.x) && (s1miny..s1maxy).contains(&s1s2inter.y) {
            return Some(s1s2inter)
        }
    }
    None



}

fn find_wire_intersections( w1corners: &Vec<Point>, w2corners: &Vec<Point>) -> Vec<Point> {
    
    let mut out: Vec< Point> = vec![];
    //out.push(Point{x:0, y:0});

    for w1window in w1corners.windows(2) {
        let s1: Segment = Segment{ p1: w1window[0], p2:w1window[1]};
        for w2window in w2corners.windows(2) {

            let s2: Segment = Segment{ p1: w2window[0], p2:w2window[1]};
            //println!("{:?} {:?}", s1, s2);
            match calc_seg_intersection(s1,s2){
                Some(val) => out.push(val),
                None => ()
            }

        }

    }
    out

}



fn gen_corners(w: &Vec<Instruction>) -> Vec<Point>{

    let mut current_x: i32 = 0;
    let mut current_y: i32 = 0;

    let mut out: Vec<Point> = vec![];

    out.push( Point{x:0, y:0} );

    for inst in w {
        if inst.card == "U" {
            current_y += inst.mag as i32;
        } else if inst.card == "D" {
            current_y -= inst.mag as i32;
        } else if inst.card == "L" {
            current_x -= inst.mag as i32;
        } else if inst.card == "R" {
            current_x += inst.mag as i32;
        }
        out.push( Point{x:current_x, y:current_y} );
    }

    out
}





fn cmp_pos( pos1: Vec<Point>, pos2: Vec<Point>) -> Vec<Point> {

    let mut out: Vec<Point> = vec![];

    for p1 in pos1.clone() {
        for p2 in pos2.clone() {
            if p1.x==p2.x && p1.y==p2.y{
                out.push( Point{x:p1.x, y:p1.y} );
                println!("found! {} {}", p1.x, p1.y);
            }
        }
    }
    out
}

fn gen_pos(w: &Vec<Instruction> ) -> Vec<Point> {

    let mut current_x: i32 = 0;
    let mut current_y: i32 = 0;

    let mut out: Vec< Point> = vec![];
    out.push( Point{x: current_x,y: current_y} );

    for instr in w {

        if instr.card == "U" {
            for _ in 1..instr.mag+1 {
                current_y += 1;
                out.push( Point{x: current_x,y: current_y} );
            }
        } else if instr.card == "D" {
            for _ in 1..instr.mag+1 {
                current_y -= 1;
                out.push( Point{x: current_x,y: current_y} );
            }
        } else if instr.card == "L" {
            for _ in 1..instr.mag+1 {
                current_x -= 1;
                out.push( Point{x: current_x,y: current_y} );
            }
        } else if instr.card == "R" {
            for _ in 1..instr.mag+1 {
                current_x += 1;
                out.push( Point{x: current_x,y: current_y} );
            }
        } else {
            println!("AAAARRRGGGHHH");
        };
    }

    out


}




/*fn cmp_corners( w1corners: Vec<(i32, i32)>, w2corners: Vec<(i32, i32)>) -> Vec<(i32, i32)> {*/
    
    /*let mut out: Vec< (i32, i32)> = vec![];*/

    /*for w1window in w1corners.windows(2) {*/
        /*let (w1p1, w1p2) = (&w1window[0], &w1window[1]);*/
        /*for w2window in w2corners.windows(2) {*/
            /*let (w2p1, w2p2) = (&w2window[0], &w2window[1]);*/
            /*//println!("{} {} {} {} ", w1p1.0, w1p2.0, w2p1.0, w2p2.0)*/

        /*}*/

    /*}*/
    /*out*/



/*}*/




/*fn gen_corners(w: Vec<String>) -> Vec<(i32, i32)>{*/

    /*let mut current_x: i32 = 0;*/
    /*let mut current_y: i32 = 0;*/

    /*let mut out: Vec< (i32, i32)> = vec![];*/

    /*out.push( (0, 0) );*/

    /*for (card, mag) in w.into_iter().map( |inst| split_inst(inst)){*/

        /*if card == "U" {*/
            /*current_y += mag as i32;*/
        /*} else if card == "D" {*/
            /*current_y -= mag as i32;*/
        /*} else if card == "L" {*/
            /*current_x -= mag as i32;*/
        /*} else if card == "R" {*/
            /*current_x += mag as i32;*/
        /*}*/
        /*out.push( (current_x, current_y) );*/
    /*}*/

    /*out*/
/*}*/

