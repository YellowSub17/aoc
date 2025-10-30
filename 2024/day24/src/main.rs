#![allow(dead_code)]
#![allow(unused_mut)]
#![allow(unused_variables)]
use std::fs::read_to_string;
use std::collections::HashMap;
use std::collections::VecDeque;


#[derive(Debug)]
enum Operation {
    AND,
    XOR,
    OR,
}

#[derive(Debug)]
struct Comparison {
    in1add: String,
    op: Operation,
    in2add: String,
    outadd: String,
}



impl Comparison {

    fn compare(&self, wires: &mut HashMap<String, bool>) -> bool {
        if !wires.contains_key(&self.in1add) || !wires.contains_key(&self.in2add) {
            return false
        } else {
            let in1 = wires.get(&self.in1add).unwrap();
            let in2 = wires.get(&self.in2add).unwrap();

            match self.op {
                Operation::AND => wires.insert(self.outadd.clone(), *in1 && *in2),
                Operation::OR => wires.insert(self.outadd.clone(), *in1 || *in2),
                Operation::XOR => wires.insert(self.outadd.clone(), *in1 ^ *in2),
            };
            return true

        };

    }
}



fn main() {
    let (mut wires, mut comparisons) = sort_input();

    while let Some(c) = comparisons.front() {
        if c.compare(&mut wires) {
            comparisons.pop_front();
        } else {
            let c = comparisons.pop_front().unwrap();
            comparisons.push_back(c);
        }
    }

    let mut ans: u64 = 0;

    for (key, val) in wires.iter(){
        if key.chars().next() == Some('z') && *val {
            //println!("{}, {}", key, val);
            let nleftsh = key[1..].parse::<i32>().unwrap();

            ans += (1 as u64) << nleftsh;
        }
    }
    println!("{}", ans);

}

fn read_input() -> Vec<String>  {
    read_to_string("./input.prod")
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}


fn sort_input() -> ( HashMap<String, bool>, VecDeque<Comparison> ) {

    let mut wires = HashMap::new();
    let mut comparisons: VecDeque<Comparison> = VecDeque::new();

    for line in read_input(){

        let sp: Vec<&str> = line.split(' ').collect();

        if sp.len() == 2{
            let address = String::from(sp[0].strip_suffix(":").unwrap());
            wires.insert(address, sp[1]!="0");

        };
        if sp.len() == 5{

            let in1add=String::from(sp[0]);
            let in2add=String::from(sp[2]);
            let outadd=String::from(sp[4]);

            let op: Option<Operation> = match sp[1] {
                "AND" => Some(Operation::AND),
                "OR" => Some(Operation::OR),
                "XOR" => Some(Operation::XOR),
                _ =>   None} ;

            match op {
                Some(s) => comparisons.push_back(Comparison{ in1add, op:s, in2add, outadd}),
                _ => (),
            };
        };
    }

    (wires, comparisons)
    

} 

