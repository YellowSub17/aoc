use std::fs::read_to_string;
use regex::Regex;


fn main() {
    let input = read_input();


    let mut cost: i64 = 0;
    for clawstrs in input.chunks(4){
        let cm = ClawMachine::new(clawstrs);
        cost+= cm.cost();
    }
    println!("{}",cost);

    //let apple: bool = true && true ;
    //println!("{}", apple);
}

struct ClawMachine {
    x1: i64,
    y1: i64,
    x2: i64,
    y2: i64,
    x3: i64,
    y3: i64,
}

impl ClawMachine {

    fn cost(&self) -> i64 {
        let donk: i64 = self.x1*self.y2 - self.x2*self.y1;

        if donk != 0 {
            //println!("donk: {:?}", donk);
            let m_ned:i64 = self.x3*self.y2 - self.x2*self.y3;
            let n_ned:i64 = self.x1*self.y3 - self.x3*self.y1;

            let m_flag: i64 =  m_ned % donk;
            let n_flag: i64 =  n_ned % donk;

            //println!("neds: {:?} {:?}", m_ned, n_ned);
            //println!("flags: {:?} {:?}", m_flag, n_flag);

            if m_flag ==0 && n_flag ==0 {
                return (3*(m_ned/ donk) + (n_ned/donk)).try_into().unwrap()
            }
        } else {
            //check colinear?
            return 0
        };
        0
    }

    fn new(inputs: &[String]) -> Self {

        let re = Regex::new(r"\d+").unwrap();

        let mut ints: Vec<i64> = vec![];

        for input in inputs {
            let xy: Vec<i64> = re
                            .find_iter(&input)
                            .filter_map(|digits| digits.as_str().parse::<i64>().ok())
                            .collect();
            ints.extend(xy);
        }
        Self {x1:ints[0], y1:ints[1], x2:ints[2], y2:ints[3], x3:ints[4]+10000000000000, y3:ints[5]+10000000000000}
    }

}





fn read_input() -> Vec<String>  {
    read_to_string("./input.test")
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}






