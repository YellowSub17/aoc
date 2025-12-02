use std::fs::read_to_string;
use std::collections::HashSet;
use std::collections::HashMap;

fn main() {
    part1();

}





struct Cheat {
    p1: (usize, usize),
    pw: (usize, usize),
    p2: (usize, usize),
    timesave: Option<i32>,
}


fn part1(){ 

     let (maze, path, path_hm) = read_input();

     let mut cheat_times: Vec<usize> = vec![];

     //For every point (x,y in maze,
     for x in 1..maze[0].len()-1 {
         for y in 1..maze.len()-1 {
             if maze[y][x] { //if xy is a wall
                 if !maze[y][x-1] && !maze[y][x+1] { //if either side of xy is a path
                     // horizontal cheat found
                     let t1 = *path_hm.get( &(x-1,y)).unwrap() as isize;
                     let t2 = *path_hm.get( &(x+1,y)).unwrap() as isize;
                     println!("{:?} {:?} {:?} {:?}", t1,t2, (x-1, y), (x+1,y));

                     let timesave: isize = ( t1 - t2 ).abs()-2;
                     cheat_times.push(timesave as usize);

                 } else if !maze[y-1][x] && !maze[y+1][x]{
                      //vertical cheat found
                     let t1 = *path_hm.get( &(x, y-1)).unwrap() as isize;
                     let t2 = *path_hm.get( &(x, y+1)).unwrap() as isize;

                     let timesave: isize = ( t1 - t2 ).abs()-2;
                     cheat_times.push(timesave as usize);
                 }
             }
        }
    }
    println!("{:?}", cheat_times);
    let gt10_count = cheat_times.into_iter().filter(|s| *s>=100).collect::<Vec<usize>>().len();

    println!("{:?}", gt10_count);
}



fn read_input() -> ( Vec<Vec<bool>>, Vec<(usize, usize)>, HashMap<(usize, usize), usize>)   {
    // returns start_coord:(usize,usize), end_coord(usize,usize), maze: Vec<Vec<bool>>
    // maze: false for path, true for wall
    //fn read_input() -> Vec<String>  {
    let lines: Vec<String> = read_to_string("./input.prod")
        .unwrap()
        .lines()
        .map(String::from)
        .collect();

    //let nx = rows[0].len();
    //let ny = rows.len();
    let mut start_node: (usize, usize) = (0,0);
    let mut end_node: (usize, usize) = (0,0);
    
    let mut maze: Vec<Vec<bool>> = vec![];

    let mut row_i: usize = 0;

    for line in lines{
        let mut row_vec: Vec<bool> = vec![];
        let mut col_i: usize = 0;
        for c in line.chars() {
            match c {
                '#' => {row_vec.push(true);},
                '.' => {row_vec.push(false);},
                'S' => {row_vec.push(false); start_node=(col_i, row_i);},
                'E' => {row_vec.push(false); end_node=(col_i, row_i);},
                _ => {},
            };
            col_i +=1;
        }
        maze.push(row_vec);
        row_i +=1;
    };
    println!("{:?} {:?}", start_node, end_node);

    let mut path: Vec<(usize, usize)> = vec![];
    let mut visited_nodes:HashSet<(usize, usize)> = HashSet::new();


    let mut current_node = start_node;

    path.push(current_node);
    visited_nodes.insert(current_node);
    
    while current_node != end_node {

        let dirs:[(isize, isize);4] = [ (0, 1), (0, -1), (1,0), (-1,0) ];

        for dir in dirs {
            let next_x: usize = ((current_node.0 as isize) +dir.0) as usize;
            let next_y: usize = ((current_node.1 as isize) +dir.1) as usize;

            let next_possible_node: (usize, usize) = (next_x, next_y);

            if !maze[next_possible_node.1][next_possible_node.0] &&  !visited_nodes.contains(&next_possible_node){

                current_node = next_possible_node;
                path.push(current_node);
                visited_nodes.insert(current_node);
            }
        }

    }

    let mut path_hm: HashMap<(usize, usize), usize> = HashMap::new();
    let mut time:usize = 0;
    for node in &path{
        path_hm.insert(node.clone(), time);
        println!("{:?}, {:?}", node, time);
        time +=1;

    }

    println!("{:?}", path_hm);


    (maze, path, path_hm)

/*    for row in map {*/
        /*println!("{:?}", row);*/
    /*}*/

    /*println!("{:?}", path);*/
}


