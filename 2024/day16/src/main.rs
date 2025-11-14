#![allow(unused)]
#![allow(dead_code)]
use std::fs::read_to_string;
use std::collections::HashSet;
use std::collections::BinaryHeap;

mod objects;
use objects::{*};


fn main() {
    part1();
}

fn part1() {


    let x = find_cheapest();
    //println!("{:?}", x.unwrap());
    



}


fn find_cheapest() -> Option<Journey> {
    let (tiles, start_i, end_i) = generate_tiles();

    //for row in &tiles {
    //println!("{:?}", row);
    //}

    let start_node: Node = Node{dir:Direction::E, coord: start_i};


    let j0 = Journey{ 
        current_node: start_node,
        current_cost: 0,
        visited_nodes: {let mut h: HashSet<Node> = HashSet::new(); h.insert(start_node); h},
        end_coord: end_i,
    };

    println!("{:?}", j0);
    //println!("{:?}", j0.get_neighbors(&Node{coord: (5,5), dir:Direction::N}));


    // DOES THE EXTENSION ON SINGLE MOVES, BUT NEEDS TO UPDATE COST
    println!("{:?}", j0.get_next_moves(&j0.current_node, &tiles));






  /*  let mut heap = BinaryHeap::new();*/
    /*heap.push(j0);*/

    /*while let Some(j) = heap.pop() {*/
        /*//println!("{:?}", heap.len());*/
        /*println!("{:?}", j.current_cost);*/
        /*if j.current_node.coord == j.end_coord {*/
            /*return Some(j);*/
        /*}*/

        /*for n in j.get_next_moves( &tiles) {*/
            /*heap.push(n);*/
        /*}*/
    /*}*/
    None
}
 

fn generate_tiles() -> (Vec<Vec<Tile>>, (usize, usize), (usize, usize)) {
    let lines = read_input();

    let mut rows = vec![];

    let mut start_i: (usize, usize) = (0,0);
    let mut end_i: (usize, usize) = (0,0);

    let mut row_i = 0;
    for line in lines {
        let mut col_i = 0;

        let mut row = vec![];

        for c in line.chars() {
            match c {
                '#' => row.push(Tile::W),
                '.' => row.push(Tile::P),
                'S' => {row.push(Tile::S); start_i = (col_i, row_i);},
                'E' => {row.push(Tile::E); end_i  = (col_i, row_i); },
                _ => {} ,
            }
            col_i+=1;
        }
        rows.push(row);
        row_i+=1;
    }
    (rows, start_i, end_i)
}

fn read_input() -> Vec<String>  {
    read_to_string("./input.test")
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

