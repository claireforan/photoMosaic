(function(){
  
var request;
document.addEventListener("DOMContentLoaded", init, false);

function init(){
    image  = document.querySelector('#wrapper');
call_try();

}

//to be called in another function with accesstoken as the parameter
function call_try(){
        var currentlocation = window.location;
        var url = "try.py" + currentlocation.search;
        request = new XMLHttpRequest();
        request.addEventListener('readystatechange', handle_response1, false);
        request.open('GET', url, true);
        request.send(null);
}


//if all's good redirect to try.py
function handle_response1(){
  if ( request.readyState === 4 ) {
        if ( request.status === 200 ) {
            if(request.responseText.trim() === 'problem') {
                        console.log("ERROR!");
                        //something to show user stuff didn't work D:
            } else if(request.responseText.trim() === 'There was a problem with the tags chosen. Please try again with different tags.'){
                        image.innerHTML = "<div><p>" + request.responseText.trim() + "</p></div>"
        } else {
                        image.innerHTML = "<div><img src="+ "'" + request.responseText.trim() + "'></div>"; 
                        image.style.marginLeft = 'auto';
                        image.style.marginRight = 'auto';
                        image.style.display = 'block';
                        image.style.height = '80%';
                        image.style.width = '100%';
                        image.style.border = '1px solid black';
                        image.style.backgroundColor = 'white';

                }
            } else {
                console.log("response = " + request.responseText.trim());
                image.innerHTML = "<div style='margin-left: auto; margin-right: auto; height: 40%; width: 40%; padding: 1em;'><p>Sorry we are experiencing problems right now, please try again later!</p><br /><a href='http://143.239.81.202'>Return to the main page</a></div>"
        }
        }
}  


})();
