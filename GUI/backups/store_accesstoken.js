
//to be called in another function with accesstoken as the parameter
function call_mosaic_make(accesstoken){
	var url = "cgi-bin/store_in_sess.py?token=" + acesstoken;
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
	      	} else if (request.responseText.trim() === 'good'){
	      		window.location.href = "cgi-bin/try.py";

	     	}
	    }
	}
}  
