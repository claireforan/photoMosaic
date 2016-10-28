(function(){

var do_the_program;
var bigimg;
var bigimgsrc;

function init(){
        do_the_program = document.querySelector("#do_the_program");
        bigimg = document.querySelector("#bigimg");
        if (bigimg){
                do_the_program.addEventListener('click', call_mosaic_make,false);
        }

}

function call_mosaic_make(){
        var url = "new_mosaic.py?img=" + bigimg.src;
        request = new XMLHttpRequest();
        request.addEventListener('readystatechange', handle_response1, false);
        request.open('GET', url, true);
        request.send(null);
}



function handle_response1(){
  if ( request.readyState === 4 ) {
        if ( request.status === 200 ) {
            if(request.responseText.trim() === 'problem') {
                        console.log("ERROR!");
                } else {
                        var mosaic_image = request.responseText.trim();
                        bigimg.src = mosaic_image;

                        var options = document.createElement("div");
                        options.innerHTML = "<a>Save?</a> <br> <a>Share?</a> <br> <a href='try.py'>Try again?</a>"

                }
            }
        }
}  


})();
