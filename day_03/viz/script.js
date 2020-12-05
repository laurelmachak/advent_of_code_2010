let tree_map = document.getElementsByTagName("pre")[0];
tree_map = tree_map.innerText.split('\n');
tree_map.pop();

for (let i=0; i<tree_map.length; i++){
    tree_map[i] = tree_map[i].split('');
}

console.log(tree_map);
// console.log(tree_map[tree_map.length-2].split(''))

function check_slope(r, d){
    let start_index = 1;
    let trees = 0;
    let empty = 0;
    for (let i=d; i<tree_map.length; i+=d){
        // let row = tree_map[i].split('');
        let index = (start_index * r) % tree_map[i].length;
        if (tree_map[i][index] === '#'){
            trees += 1;
        } else {
            empty += 1;
        }

        start_index += 1;
    }

return trees;
    
}

console.log(check_slope(3,1));

function setup(){
    canvas = createCanvas(800,500);
    canvas.parent("container");
   
   }
   
   function draw(){
    background(240);
   
   }
   