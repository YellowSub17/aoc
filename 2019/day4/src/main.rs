
#![allow(dead_code)]
#![allow(unused_mut)]
#![allow(unused_variables)]

fn main() {
    println!("Hello, world!");
    ////part1();
    ////inc_digits(&String::from("12343"));
    //let x = adj_digits2(&String::from("xxxxxy"));
    //
    part2();

}




fn adj_digits(pword: &String) -> bool {

    for dd in pword.as_bytes().windows(2){
        if dd[0] == dd[1] {
            return true
        }
    }
    false
}

fn inc_digits(pword: &String) -> bool {

    for dd in pword.as_bytes().windows(2){
        if dd[0] > dd[1] {
            return false
        }
    }
    true

}


fn adj_digits2(pword: &String) -> bool {


    let mut b: Vec<u8> = vec![];
    b.push(0);
    for d in pword.as_bytes(){
        b.push(*d);
    }
    b.push(0);

    for dddd in b.windows(4){
        if dddd[0] != dddd[1] && dddd[1]==dddd[2] && dddd[2]!=dddd[3] {
            return true
        }
    }
    false
}

fn part2(){

    //153 toolow
    let start_i: usize = 402328;
    let end_i: usize = 864247;


    let pwords: Vec<_> = (start_i..end_i)
                    .map(|u| u.to_string())
                    .filter(inc_digits)
                    .filter(adj_digits2)
                    .collect();

    let npwords: usize = pwords.len();
    println!("{}", npwords);
    


}

fn part1(){

    let start_i: usize = 402328;
    let end_i: usize = 864247;


    let pwords: Vec<_> = (start_i..end_i)
                    .map(|u| u.to_string())
                    .filter(adj_digits)
                    .filter(inc_digits)
                    .collect();

    let npwords: usize = pwords.len();
    println!("{}", npwords);
    


}
