window.addEventListener('scroll', show);

function showalert(){
    alert("makasiii udah daftarrr, gampang kan cara daftarnya hehe 😆😆")
}

function show(){
    var shows = document.querySelectorAll(".show");

    for(var i = 0; i < shows.length; i++){

        var windowheight = window.innerHeight;
        var showtop = shows[i].getBoundingClientRect().top;
        var showpoint =150;

        if(showtop < windowheight - showpoint){
            shows[i].classList.add('active');
        }
        else{
            shows[i].classList.remove('active');
        }
    }
}
