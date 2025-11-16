use std::fs::read_to_string;
use std::collections::VecDeque;

use image::{RgbImage, Rgb};


const NX:usize = 71;
const NY:usize = 71;

fn main() {
    //part1();
}
    



fn part1() {
    let mut mem:Vec<Vec<bool>> = vec![vec![false; NX]; NY];
    let mut path:Vec<Vec<bool>> = vec![vec![false; NX]; NY];
    for row in &mem{
        println!("{:?}", row);
    }

    let addresses = read_input();

    for (x,y) in &addresses[..1024] {
        mem[*y][*x] = true;
    }

    let sp = shortest_path(&mem).unwrap();

    println!("length of shortest path: {:}", sp.len());
    for (x,y) in &sp {
        path[*y][*x] = true;
    }


    let img_nx:u32 = (NX*9) as u32;
    let img_ny:u32 = (NY*9) as u32;
    let mut img = RgbImage::new(img_nx,img_ny);

    img = draw_mem(&mem, img.clone(), 255,0,0);
    img = draw_mem(&path, img.clone(), 0,255,255);


    img.save("sol.png".to_string());


    println!("{:?}", sp);





}

fn shortest_path(maze: &Vec<Vec<bool>>) -> Option<Vec<(usize, usize)>> {
    if maze[0][0] || maze[NY-1][NX-1] {
        return None
    }

    let dirs: Vec<(i32, i32)> = vec![(0,1), (1,0), (0, -1), (-1,0)];
    let mut visited = vec![vec![false; NX]; NY];
    let mut parent = vec![vec![None; NX]; NY];
    visited[0][0] = true;

    let mut queue = VecDeque::new();
    queue.push_back( (0usize, 0usize) );
    
    let mut count:usize = 0;

    while let Some( (x,y)) = queue.pop_front() {
        count+=1;
        
        if x == NX-1 && y==NY-1 {
            let mut path = vec![(x,y)];
            let mut current = (x,y);
            while let Some(p) = parent[current.1][current.0] {
                path.push(p);
                current = p;
            }
            path.reverse();
            return Some(path);

        }
        for (dx, dy) in &dirs {
            let next_x = x as i32 + dx;
            let next_y = y as i32 + dy;
            
            if next_x >=0 && next_x <= (NX-1) as i32 && next_y >=0 && next_y <= (NY-1) as i32 {

                let (next_x, next_y) = (next_x as usize, next_y as usize);

                if !maze[next_y][next_x] && !visited[next_y][next_x] {
                    visited[next_y][next_x] = true;
                    parent[next_y][next_x] = Some((x,y));
                    queue.push_back( (next_x, next_y));
                }

            }


        }
    }
    None
}


fn read_input() -> Vec<(usize, usize)>  {
    read_to_string("./input.prod")
        .unwrap()
        .lines()
        .map(String::from)
        .map(|s| {
            let mut parts = s.split(',');
            (parts.next().unwrap().parse::<usize>().unwrap(),  parts.next().unwrap().parse::<usize>().unwrap())
        })
        .collect()
}



fn draw_mem(mem: &Vec<Vec<bool>>, mut img: RgbImage, r:u8, g:u8, b:u8) -> RgbImage {

        for i_memcol in 0..NX{
            for i_memrow in 0..NY{
                if mem[i_memrow as usize][i_memcol as usize]{
                    let px_x: u32= (9*i_memcol).try_into().unwrap();
                    let px_y: u32= (9*i_memrow).try_into().unwrap();

                    for xx in 0..9 {
                        for yy in 0..9{
                            img.put_pixel(px_x+xx, px_y+yy, Rgb([r,g,b]));
                        }

                    }

                }
            }
        }
        img
}



