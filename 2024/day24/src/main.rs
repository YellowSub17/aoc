#![allow(dead_code)]
#![allow(unused_mut)]
#![allow(unused_variables)]
use std::fs::read_to_string;
use std::collections::HashMap;
use std::collections::HashSet;
use std::collections::VecDeque;
use itertools::Itertools;


#[derive(Debug)]
#[derive(Clone)]
enum Operation {
    AND,
    XOR,
    OR,
}

#[derive(Debug)]
#[derive(Clone)]
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

fn swap_comps_outadd(c1: &Comparison, c2: &Comparison) -> (Comparison, Comparison){
    ( Comparison{outadd:c2.outadd.clone(), ..c1.clone()}, Comparison{outadd:c1.outadd.clone(), ..c2.clone()})
}


fn main() {
    //part1();
    part2();

  /*  let (wires, comparisons) = sort_input();*/
    /*let c1 = &comparisons[0];*/
    /*let c2 = &comparisons[1];*/
    /*println!("{:?} {:?}", c1,c2);*/
    /*let (c3,c4): (Comparison, Comparison) = swap_comps_outadd(c1,c2);*/
    /*println!("{:?} {:?}",c3,c4);*/


}
 

fn run_wires(mut wires: HashMap<String, bool>, mut comparisons: VecDeque<Comparison> ) -> u64 {
    let mut count:u64 =0;
    
    while let Some(c) = comparisons.front() {
        if c.compare(&mut wires) {
            comparisons.pop_front();
            count=0;
        } else {
            let c = comparisons.pop_front().unwrap();
            comparisons.push_back(c);
            count+=1;
            if count>comparisons.len().try_into().unwrap(){
                //println!("out of control!");
                break
            }
        }
    }
    let mut ans: u64 = 0;
    for (key, val) in wires.iter(){
        if key.chars().next() == Some('z') && *val {
            let nleftsh = key[1..].parse::<i32>().unwrap();
            ans += (1 as u64) << nleftsh;
        }
    }

    ans
}

fn unique_pairs(vp: &Vec<Vec<usize>> ) -> bool {
    let mut used_inds = HashSet::new();
    for pair in vp {
        for single in pair {
            if !used_inds.insert(single) {
                return false
            }
        }
    } return true
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


//fn part2_graphviz


fn part1() {
    println!("PART1:");
    let (mut wires, mut comparisons) = sort_input();
    let ans: u64 = run_wires(wires, comparisons);
    println!("{}", ans);
}


fn part2() {

    println!("PART2:");
    let (base_wires, base_comparisons) = sort_input();
    let mut x_in: u64 = 0;
    let mut y_in: u64 = 0;
    for (key, val) in base_wires.iter(){
        if key.chars().next() == Some('x') && *val {
            let nleftsh = key[1..].parse::<i32>().unwrap();
            x_in += (1 as u64) << nleftsh;
        } else if key.chars().next() == Some('y') && *val {
            let nleftsh = key[1..].parse::<i32>().unwrap();
            y_in += (1 as u64) << nleftsh;
        }
    }

    let mut target_ans: u64 = x_in+y_in;
    println!("X={}",x_in); 
    println!("Y={}",y_in); 
    println!("TARGET={}", target_ans); 


    'main: for swap_combo_inds in (0..base_comparisons.len()).combinations(8){
        println!("{:?}",swap_combo_inds);
        for pairs_of_combos_inds in swap_combo_inds.clone().into_iter().combinations(2).combinations(4).filter(|pairs| unique_pairs(pairs) ){

            //println!("{:?}",pairs_of_combos_inds);

            let mut comparisons = base_comparisons.clone();
            let mut wires = base_wires.clone();

            for pair in pairs_of_combos_inds {

                let oldc1 = &comparisons[pair[0]];
                let oldc2 = &comparisons[pair[1]];
                let (newc1, newc2) = swap_comps_outadd(oldc1, oldc2);
                comparisons[pair[0]] = newc1;
                comparisons[pair[1]] = newc2;
            }

            let ans = run_wires(wires, comparisons);

            if ans==target_ans{
                println!("FOUND! {:?}", swap_combo_inds);
                break 'main
            }


        }

    }
}





