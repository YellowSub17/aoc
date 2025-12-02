use std::fs::read_to_string;
use regex::Regex;
//use image::{RgbImage, Rgb};
use image::{GrayImage, Luma};
use std::fs;
use std::io::{self, Write};

const NX: u8 = 101;
const NY: u8 = 103;




fn main() {
    part1();
    part2();

}

fn part1() {

    let robots: Vec<Robot> = read_input().into_iter().map(Robot::new).collect();
    let mut q1count: u32 = 0;
    let mut q2count: u32 = 0;
    let mut q3count: u32 = 0;
    let mut q4count: u32 = 0;

    for mut robot in robots {
        robot.run_n(100);
        match robot.get_quad() {
            Quadrant::First => q1count+=1,
            Quadrant::Second => q2count+=1,
            Quadrant::Third => q3count+=1,
            Quadrant::Fourth => q4count+=1,
            Quadrant::Line => (),
        };
    };
    println!("{}", q1count*q2count*q3count*q4count);
}

fn part2() {

    let mut robots: Vec<Robot> = read_input().into_iter().map(Robot::new).collect();

    let imin = 0;
    let imax = 7000;
    
    for i in imin..imax {
        print!("\r{}", i);
        io::stdout().flush().unwrap();
        let mut img = GrayImage::new(NX.into(), NY.into());

  

        for mut robot in &mut robots {
            robot.run_n(1);
            img.put_pixel(robot.current.x.into(), robot.current.y.into(), Luma([255]));
            };


        let mut vert_flag = false;
        for i_x in 0..NX {
            let mut white_count = 0;
            for i_y in 0..NY{
                if *img.get_pixel(i_x.into(), i_y.into()) == Luma([255]) {
                    white_count +=1;
                }
            }
            if white_count> 20{
                vert_flag = true;

            }
        }



        if vert_flag {
        img.save(format!("./imgs/i{}.png", i));
        }


    }



}



enum Quadrant {
    First,
    Second,
    Third,
    Fourth,
    Line,
}

#[derive(Debug)]
#[derive(Clone)]
struct Vec2D<T>{
    x: T,
    y: T
}


#[derive(Debug)]
#[derive(Clone)]
struct Robot {
    start: Vec2D<u8>,
    v: Vec2D<i8>,
    current: Vec2D<u8>,
    iter:u64,
}

impl Robot {

    fn new(input: String) -> Self {

        let re = Regex::new(r"-*\d+").unwrap();

        let inputs: Vec<i8> = re.find_iter(&input)
                            .filter_map(|digits| digits.as_str().parse::<i8>().ok())
                            .collect();

        Self{ start: Vec2D{x:inputs[0].try_into().unwrap(), y:inputs[1].try_into().unwrap()},
            v: Vec2D{x:inputs[2].try_into().unwrap(), y:inputs[3].try_into().unwrap()}, 
            current: Vec2D{x:inputs[0].try_into().unwrap(), y:inputs[1].try_into().unwrap()}, iter:0}
    }

    fn update(&mut self){
        self.iter +=1;
        self.current.x = (((self.current.x as i16 + self.v.x as i16) + (NX as i16)) % (NX as i16)) as u8;
        self.current.y = (((self.current.y as i16 + self.v.y as i16) + (NY as i16)) % (NY as i16)) as u8;
    }

    fn run_n(&mut self, n:i32){
        for _ in 0..n{
            self.update()
        }
    }

    fn get_quad(self) ->  Quadrant {
        if self.current.x == NX/2 || self.current.y==NY/2 {
            return Quadrant::Line
        }

        if self.current.x < NX/2 {
            if self.current.y<NY/2 {
                return Quadrant::First
            } else {
                return Quadrant::Third
            };
        } else {
            if self.current.y<NY/2 {
                return Quadrant::Second
            } else {
                return Quadrant::Fourth
            };
        };
    }
}


fn read_input() -> Vec<String>  {
    read_to_string("./input.prod")
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}


