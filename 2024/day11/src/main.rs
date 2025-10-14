fn main() {

    //8069 87014 98 809367 525 0 9494914 5
    
    let mut stones:Vec<u64> = vec![8069, 87014,98, 809367, 525, 0, 9494914, 5];
    //let mut stones:Vec<u64> = vec![125, 17];
    println!("{:?}", stones);

    for b in 0..25{
        println!("{}",b); 
        stones = blink_all(stones);
        //println!("{:?}", stones);
    }

    println!("{}", stones.len());

    //let (x, y): (u64, u64) = split_even(1204);

    //println!("{}",x);
    //println!("{}",y);



}





fn blink_all(stones: Vec<u64>) -> Vec<u64> {

    let mut new_stones: Vec<u64> = vec![];


    //let mut x = stones.clone().into_iter().map(blink_stone).collect();


    for stone in stones{
        for ns in blink_stone(stone){
            new_stones.push(ns);
        }
    }

    new_stones
}




fn blink_stone(stone: u64) -> Vec<u64> {

    let mut new_stones: Vec<u64> = vec![];

    let stone_string = stone.to_string();
    if stone == 0 {
        new_stones.push(1);
    } else if stone_string.len()%2 ==0 {
        let split_stones: (u64, u64) = split_even(&stone_string);
        new_stones.push(split_stones.0);
        new_stones.push(split_stones.1);
    } else {
        new_stones.push(stone*2024)
    }

    new_stones

}


fn split_even(stone_string: &String) -> (u64, u64) {


    let stone1_string = &stone_string[..stone_string.len()/2];
    let stone2_string = &stone_string[stone_string.len()/2..];


    let s1:u64 = stone1_string.parse::<u64>().unwrap();
    let s2:u64 = stone2_string.parse::<u64>().unwrap();


    (s1,s2)
}

