
use std::collections::HashSet;
use std::fmt;
use std::cmp::Ordering;


//TODO move the structs and impl to another file
#[derive(Debug)]
#[derive(PartialEq)]
pub enum Tile {
    S,
    E,
    W,
    P,
}

#[derive(Debug)]
#[derive(Clone, Copy)]
#[derive(Eq, Hash, PartialEq)]
pub enum Direction {
    N,
    S,
    E,
    W,
}

#[derive(Debug)]
#[derive(Clone, Copy)]
#[derive(Eq, Hash, PartialEq)]
pub struct Node { 
    pub dir: Direction,
    pub coord: (usize, usize),
}


pub struct Journey {
    pub current_node: Node,
    pub current_cost: usize,
    pub visited_nodes: HashSet<Node>,
    pub end_coord: (usize, usize),
}


impl fmt::Debug for Journey {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "\nJourney\n\tCurrent Node: {:?}\n\tCurrent Cost: {}\n\tVisited Nodes: {:?}\n", self.current_node, self.current_cost, self.visited_nodes)
    }
}

impl Ord for Journey {
    fn cmp(&self, other: &Self) -> Ordering {
        other.current_cost.partial_cmp(&self.current_cost).unwrap()
    }
}

impl PartialOrd for Journey {
    fn partial_cmp(&self, other:&Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for Journey {
    fn eq(&self, other:&Self) ->bool {
        self.current_cost == other.current_cost
    }
}

impl Eq for Journey {}

impl Journey {

    pub fn get_next_moves(&self, node: &Node, tiles: &Vec<Vec<Tile>>) -> Vec<Self> {

        let mut moves: Vec<Self> = vec![];




        if node.coord == self.end_coord {
            return moves
        }

        let (neighbors, left_dir, right_dir)  = self.get_neighbors(&node);

        let mut next_node: Node;

        if tiles[neighbors[0].1][neighbors[0].0] != Tile::W {
            next_node = Node{dir:node.dir, coord:neighbors[0]};
            moves.push(Journey{
                        current_node: next_node,
                        current_cost: self.current_cost+1,
                        visited_nodes: {let mut h: HashSet<Node> = self.visited_nodes.clone(); h.insert(next_node); h},
                        end_coord: self.end_coord,
                    });
        };

        if tiles[neighbors[1].1][neighbors[1].0] != Tile::W {
            next_node = Node{dir:left_dir, coord:node.coord};
            moves.push(Journey{
                        current_node: next_node,
                        current_cost: self.current_cost+1000,
                        visited_nodes: {let mut h: HashSet<Node> = self.visited_nodes.clone(); h.insert(next_node); h},
                        end_coord: self.end_coord,
                    });
        };

        if tiles[neighbors[2].1][neighbors[2].0] != Tile::W {
            next_node = Node{dir:right_dir, coord:node.coord};
            moves.push(Journey{
                        current_node: next_node,
                        current_cost: self.current_cost+1000,
                        visited_nodes: {let mut h: HashSet<Node> = self.visited_nodes.clone(); h.insert(next_node); h},
                        end_coord: self.end_coord,
                    });
        };

        if moves.len()==1 {
            moves = self.get_next_moves(&moves[0].current_node, tiles);
        }

         moves
    }



    pub fn get_neighbors(&self,node: &Node) -> ([(usize, usize);3], Direction, Direction) {


        let forward_coord: (usize, usize);
        let left_coord: (usize, usize);
        let right_coord: (usize, usize);
        let left_dir:Direction;
        let right_dir:Direction;

        match node.dir {
            Direction::N => {forward_coord = (node.coord.0, node.coord.1-1);
                             left_coord = (node.coord.0-1, node.coord.1);
                             right_coord = (node.coord.0+1, node.coord.1);
                             left_dir=Direction::W;
                             right_dir=Direction::E;
                            },

            Direction::S => {forward_coord = (node.coord.0, node.coord.1+1);
                             left_coord = (node.coord.0+1, node.coord.1);
                             right_coord = (node.coord.0-1, node.coord.1);
                             left_dir=Direction::E;
                             right_dir=Direction::W;
                            },

            Direction::E => {forward_coord = (node.coord.0+1, node.coord.1);
                             left_coord = (node.coord.0, node.coord.1-1);
                             right_coord = (node.coord.0, node.coord.1+1);
                             left_dir=Direction::N;
                             right_dir=Direction::S;
                            },

            Direction::W => {forward_coord = (node.coord.0-1, node.coord.1);
                             left_coord = (node.coord.0, node.coord.1+1);
                             right_coord = (node.coord.0, node.coord.1-1);
                             left_dir=Direction::S;
                             right_dir=Direction::N;
                            },
        };

        let neighbors =  [ forward_coord, left_coord, right_coord ];
        (neighbors, left_dir, right_dir)
    }
}



