

use std::fs;

fn read_input(fname: &str) -> Vec<String> {


    let contents = fs::read_to_string(fname)
        .expect("Should have been able to read the file");

    let lines: Vec<String> = contents.lines()
        .map(|s:&str| s.to_string())
        .collect();

    lines




}



/*use std::fs::File;*/
/*use std::io::Read;*/

/*fn lines_from_file(filename: &str) -> Vec<String> {*/
    /*let mut file = match File::open(filename) {*/
        /*Ok(file) => file,*/
        /*Err(_) => panic!("no such file"),*/
    /*};*/
    /*let mut file_contents = String::new();*/
    /*file.read_to_string(&mut file_contents)*/
        /*.ok()*/
        /*.expect("failed to read!");*/
    /*let lines: Vec<String> = file_contents.split("\n")*/
        /*.map(|s: &str| s.to_string())*/
        /*.collect();*/
    /*lines*/
/*}*/




fn main(){

    let input_filename=String::from("./input.prod");

    let v = read_input(&input_filename);

    for s in v{
        println!("{}", s)
    }

}


