
use image::{RgbImage, Rgb};
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

            //img.put_pixel(robot.cddurrent.x.into(), robot.current.y.into(), Luma([255]));
    pub fn draw_out(&self, tiles: &Vec<Vec<Tile>>, fname:String) {

        let nx = tiles[0].len() as u32;
        let ny = tiles.len() as u32;
        let mut img = RgbImage::new(3*nx, 3*ny);

        let wall_color = Rgb([0,0,0]);
        let start_color = Rgb([0,255,0]);
        let end_color = Rgb([255,0,0]);
        let path_color = Rgb([255,255,255]);
        let visited_color = Rgb([100,100,100]);
        let current_color = Rgb([0,0,255]);

        let mut px_x: u32;
        let mut px_y: u32;



        for (i_row, row) in tiles.iter().enumerate() {

        for (i_col, tile) in row.iter().enumerate() {
            
            for x in 0..3 { for y in 0..3 {
                px_x = (3*(i_col)+x) as u32;
                px_y = (3*(i_row)+y) as u32;
                match tile {
                        Tile::W => img.put_pixel(px_x, px_y, wall_color),
                        Tile::S => img.put_pixel(px_x, px_y, start_color),
                        Tile::E => img.put_pixel(px_x, px_y, end_color),
                        Tile::P => img.put_pixel(px_x, px_y, path_color),
                    }
            } }
            }
        }



        for visited_node in &self.visited_nodes {
            for x in 0..3 { for y in 0..3 {

                px_x = (3*(visited_node.coord.0)+x) as u32;
                px_y = (3*(visited_node.coord.1)+y) as u32;
                img.put_pixel(px_x, px_y, visited_color);
            }}
        }

/*       for x in 0..3 { for y in 0..3 {*/

            /*px_x = (3*(self.current_node.coord.0+x)) as u32;*/
            /*px_y = (3*(self.current_node.coord.1+y)) as u32;*/
            /*img.put_pixel( px_x, px_y, current_color);*/
        /*}}*/



       
        img.save(format!("{}", fname));
    }


    pub fn get_next_moves(&self, tiles: &Vec<Vec<Tile>>) -> Vec<Self> {

        let mut moves: Vec<Self> = vec![];





        //if self.current_node.coord == self.end_coord {
            //return moves
        //}

        let (neighbors, left_dir, right_dir)  = self.get_neighbors();

        let mut next_node: Node;

        if tiles[neighbors[0].1][neighbors[0].0] != Tile::W {
            next_node = Node{dir:self.current_node.dir, coord:neighbors[0]};

            if !self.visited_nodes.contains(&next_node) {
            moves.push(Journey{
                        current_node: next_node,
                        current_cost: self.current_cost+1,
                        visited_nodes: {let mut h: HashSet<Node> = self.visited_nodes.clone(); h.insert(next_node); h},
                        end_coord: self.end_coord,
                    });
            };
        };

        if tiles[neighbors[1].1][neighbors[1].0] != Tile::W {
            next_node = Node{dir:left_dir, coord:self.current_node.coord};

            if !self.visited_nodes.contains(&next_node) {
            moves.push(Journey{
                        current_node: next_node,
                        current_cost: self.current_cost+1000,
                        visited_nodes: {let mut h: HashSet<Node> = self.visited_nodes.clone(); h.insert(next_node); h},
                        end_coord: self.end_coord,
                    });
            };
        };

        if tiles[neighbors[2].1][neighbors[2].0] != Tile::W {
            next_node = Node{dir:right_dir, coord:self.current_node.coord};

            if !self.visited_nodes.contains(&next_node) {
            moves.push(Journey{
                        current_node: next_node,
                        current_cost: self.current_cost+1000,
                        visited_nodes: {let mut h: HashSet<Node> = self.visited_nodes.clone(); h.insert(next_node); h},
                        end_coord: self.end_coord,
                    });
            };
        };

        if moves.len()==1 {
            moves = moves[0].get_next_moves(tiles);
        }

         moves
    }



    pub fn get_neighbors(&self) -> ([(usize, usize);3], Direction, Direction) {


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



