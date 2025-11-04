use std::fs::read_to_string;
use std::collections::HashMap;
use std::collections::HashSet;

fn main() {
    part1();
    part2();
}

fn read_input() -> Vec<String>  {
    read_to_string("./input.test")
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}



fn part2() {
    let connections = read_input();

    let mut connection_cache: HashMap<String, HashSet<String>>= HashMap::new();

    for connection in connections{
        let mut sp = connection.split('-');
        let comp1 = sp.next().unwrap().to_string();
        let comp2 = sp.next().unwrap().to_string();

        let val = connection_cache.entry(comp1.clone()).or_insert(HashSet::new());
        val.insert(comp2.clone());

        let val = connection_cache.entry(comp2.clone()).or_insert(HashSet::new());
        val.insert(comp1.clone());
    };

    println!("{:?}", connection_cache);


    //Bron–Kerbosch




}

fn part1() {
    let connections = read_input();

    let mut connection_cache: HashMap<String, HashSet<String>>= HashMap::new();

    for connection in connections{
        let mut sp = connection.split('-');
        let comp1 = sp.next().unwrap().to_string();
        let comp2 = sp.next().unwrap().to_string();

        let val = connection_cache.entry(comp1.clone()).or_insert(HashSet::new());
        val.insert(comp2.clone());

        let val = connection_cache.entry(comp2.clone()).or_insert(HashSet::new());
        val.insert(comp1.clone());
    };

    let mut triads:  HashSet<String> = HashSet::new();

    for (key1, vals1) in &connection_cache {
        for (key2, vals2) in &connection_cache{
            if key1 == key2  { continue }
            if vals1.get(key2).is_none() {continue}
            
            for mid in vals1.intersection(&vals2) {
                if key1.chars().nth(0).unwrap()=='t'||key2.chars().nth(0).unwrap()=='t'||mid.chars().nth(0).unwrap()=='t'{
                let mut triad_vec: Vec<String> = vec![];
                triad_vec.push(key1.clone());
                triad_vec.push(mid.clone());
                triad_vec.push(key2.clone());
                triad_vec.sort();
                triads.insert(format!("{},{},{}", triad_vec[0],triad_vec[1],triad_vec[2]));
                }
            }


        }
    }
    println!("ANSWER: {}", triads.len());
}
    


