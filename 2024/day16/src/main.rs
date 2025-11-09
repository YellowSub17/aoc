use std::fs::read_to_string;
use std::collections::HashSet;

fn main() {
    part1();
}


#[derive(Debug)]
enum Tile {
    Star,
    Endx,
    Wall,
    Path,
}

#[derive(Debug)]
#[derive(Clone)]
#[derive(Copy)]
enum Direction {
    North,
    South,
    East,
    West,
}


struct Journey {
    current_dir: Direction,
    current_node: (usize, usize),
    current_cost: (usize),
    visited_nodes: Vec<( (usize, usize), Direction)>,
}

impl Journey {

    fn get_next_moves(&self, map: Vec<Vec<Tile>>) -> Vec<Journey> {
       //
       // Get adjacent tiles of current position (including current pos w/ direction change)
       // return all the journeys 
       let mut v = vec![];
       v.push(Journey{current_dir:self.current_dir, current_node:self.current_node, current_cost:self.current_cost, visited_nodes:self.visited_nodes.clone()});
       v
    }
}


fn part1() {

    let (map, start_i, end_i) = generate_map();

    for row in map {
    println!("{:?}", row);
    }

    println!("{:?}", end_i);



}


fn generate_map() -> (Vec<Vec<Tile>>, (usize, usize), (usize, usize)) {
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
                '#' => row.push(Tile::Wall),
                '.' => row.push(Tile::Path),
                'S' => {row.push(Tile::Star); start_i = (col_i, row_i);},
                'E' => {row.push(Tile::Endx); end_i  = (col_i, row_i); },
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

