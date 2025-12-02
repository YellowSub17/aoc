use std::fs::read_to_string;

fn main() {
    println!("Hello, world!");
    println!("{}", iterate(iterate(123)));

    let mut counts: Vec<usize> = vec![];

    let inputs: Vec<usize> = read_input();

    for input in inputs {
        let mut s = input;
        for _ in 0..2000 {
            s = iterate(s)
        };
        counts.push(s);
    };
    println!("{:?}", counts.iter().sum::<usize>());

    //let sum_counts = a.




}






fn mix(x: usize, secret: usize) -> usize {
    x ^ secret
}

fn prune(secret:usize) -> usize {
    secret % 16777216
}

fn iterate(mut secret: usize) -> usize{

    secret = mix(secret, secret*64);
    secret = prune(secret);

    secret = mix(secret, secret/32);
    secret = prune(secret);

    secret = mix(secret, secret*2048);
    secret = prune(secret);
    
    secret
}


fn read_input() -> Vec<usize>  {
    read_to_string("./input.prod")
        .unwrap()
        .lines()
        .map(String::from)
        .map(|s| s.parse::<usize>().unwrap() )
        .collect()
}

