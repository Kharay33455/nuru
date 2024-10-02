function showImg(pic, cap){
    document.getElementById('fullImgBox').style.display = 'flex' 
    document.getElementById('fullImg').src = pic
    document.getElementById('fullImg').alt = cap
    document.getElementById('caption').innerHTML = cap
}

function hideImg(){
    document.getElementById('fullImgBox').style.display = 'none'
}


