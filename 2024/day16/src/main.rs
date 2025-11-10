#![allow(unused)]
#![allow(dead_code)]
use std::fs::read_to_string;
use std::collections::HashSet;
use std::fmt;

fn main() {
    part1();
}


//TODO move the structs and impl to another file
#[derive(Debug)]
#[derive(PartialEq)]
enum Tile {
    S,
    E,
    W,
    P,
}

#[derive(Debug)]
#[derive(Clone, Copy)]
#[derive(Eq, Hash, PartialEq)]
enum Direction {
    N,
    S,
    E,
    W,
}

#[derive(Debug)]
#[derive(Clone, Copy)]
#[derive(Eq, Hash, PartialEq)]
struct Node { 
    dir: Direction,
    coord: (usize, usize),
}


struct Journey {
    current_node: Node,
    current_cost: usize,
    visited_nodes: HashSet<Node>,
    end_coord: (usize, usize),
}


impl fmt::Debug for Journey {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "\nJourney\n\tCurrent Node: {:?}\n\tCurrent Cost: {}\n\tVisited Nodes: {:?}\n", self.current_node, self.current_cost, self.visited_nodes)
    }

}

impl Journey {

    fn get_next_moves(&self, tiles: &Vec<Vec<Tile>>) -> Vec<Self> {

        let (neighbors, left_dir, right_dir)  = self.get_neighbors();

        let mut moves: Vec<Self> = vec![];
        let mut next_node: Node;

        if tiles[neighbors[0].1][neighbors[0].0] != Tile::W {
            next_node = Node{dir:self.current_node.dir, coord:neighbors[0]};
            moves.push(Journey{
                        current_node: next_node,
                        current_cost: self.current_cost+10,
                        visited_nodes: {let mut h: HashSet<Node> = self.visited_nodes.clone(); h.insert(next_node); h},
                        end_coord: self.end_coord,
                    });
        };

        if tiles[neighbors[1].1][neighbors[1].0] != Tile::W {
            next_node = Node{dir:left_dir, coord:self.current_node.coord};
            moves.push(Journey{
                        current_node: next_node,
                        current_cost: self.current_cost+1000,
                        visited_nodes: {let mut h: HashSet<Node> = self.visited_nodes.clone(); h.insert(next_node); h},
                        end_coord: self.end_coord,
                    });
        };

        if tiles[neighbors[2].1][neighbors[2].0] != Tile::W {
            next_node = Node{dir:right_dir, coord:self.current_node.coord};
            moves.push(Journey{
                        current_node: next_node,
                        current_cost: self.current_cost+1000,
                        visited_nodes: {let mut h: HashSet<Node> = self.visited_nodes.clone(); h.insert(next_node); h},
                        end_coord: self.end_coord,
                    });
        };

         moves
    }





    fn get_neighbors(&self) -> ([(usize, usize);3], Direction, Direction) {

        let forward_coord: (usize, usize);
        let left_coord: (usize, usize);
        let right_coord: (usize, usize);
        let left_dir:Direction;
        let right_dir:Direction;

        match self.current_node.dir {
            Direction::N => {forward_coord = (self.current_node.coord.0, self.current_node.coord.1-1);
                             left_coord = (self.current_node.coord.0-1, self.current_node.coord.1);
                             right_coord = (self.current_node.coord.0+1, self.current_node.coord.1);
                             left_dir=Direction::W;
                             right_dir=Direction::E;
                            },

            Direction::S => {forward_coord = (self.current_node.coord.0, self.current_node.coord.1+1);
                             left_coord = (self.current_node.coord.0+1, self.current_node.coord.1);
                             right_coord = (self.current_node.coord.0-1, self.current_node.coord.1);
                             left_dir=Direction::E;
                             right_dir=Direction::W;
                            },

            Direction::E => {forward_coord = (self.current_node.coord.0+1, self.current_node.coord.1);
                             left_coord = (self.current_node.coord.0, self.current_node.coord.1-1);
                             right_coord = (self.current_node.coord.0, self.current_node.coord.1+1);
                             left_dir=Direction::N;
                             right_dir=Direction::S;
                            },

            Direction::W => {forward_coord = (self.current_node.coord.0-1, self.current_node.coord.1);
                             left_coord = (self.current_node.coord.0, self.current_node.coord.1+1);
                             right_coord = (self.current_node.coord.0, self.current_node.coord.1-1);
                             left_dir=Direction::S;
                             right_dir=Direction::N;
                            },
        };

        let neighbors =  [ forward_coord, left_coord, right_coord ];

        (neighbors, left_dir, right_dir)

    }


}


fn part1() {

    let (tiles, start_i, end_i) = generate_tiles();

    for row in &tiles {
    println!("{:?}", row);
    }

    let start_node: Node = Node{dir:Direction::E, coord: start_i};

    let j0 = Journey{ 
        current_node: start_node,
        current_cost: 0,
        visited_nodes: {let mut h: HashSet<Node> = HashSet::new(); h.insert(start_node); h},
        end_coord: end_i,
    };

    let neighbors = j0.get_neighbors();
    let next_moves = j0.get_next_moves(&tiles);

    //let queue: Vec<Journey> = vec![];
    //queue.push(j0);



    println!("#####");
    println!("{:?}", j0);
    println!("{:?}", neighbors);
    println!("NEXT MOVES: {:?}", next_moves);

 


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

