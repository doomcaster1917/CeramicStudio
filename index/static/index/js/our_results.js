function load(name, desription, image) {

    let describeBlock = create_describe_block(name, desription)
    let postImg = create_img(image)
    create_board(describeBlock, postImg)
}


function create_describe_block(name, desription){
    let decriptionBlock = document.createElement('div')
    let postName = document.createElement('h3')
    let shortDescription = document.createElement('p')
    decriptionBlock.id =  "decriptionBlock"
    postName.innerHTML = name
    shortDescription.innerHTML = desription
    decriptionBlock.append(postName, shortDescription)

    return decriptionBlock
}

function create_img(path){
    let postImg = document.createElement('img')
    postImg.src = path
    postImg.id = "postImg"
    return postImg
}

function create_board(decriptionBlock, postImg) {
    let board = document.getElementById("block_wrapper");
    let mainBlock = document.createElement('div')
    mainBlock.id = 'post'
    board.append(mainBlock)
    mainBlock.append(decriptionBlock)
    mainBlock.append(postImg)

}