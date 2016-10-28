var amountScrolled = 220;
var back_to_top;

window.addEventListener('DOMContentLoaded', init, false);

function init(){
        back_to_top = document.querySelector(".back-to-top");
        window.addEventListener('scroll', show_button, false);
        //back_to_top.addEventListener('mouseover', touching, false);
        //back_to_top.addEventListener('mouseout', away, false);
        back_to_top.style.display = "none";
};



function show_button(){
        var travelled = window.pageYOffset;

        if (travelled > amountScrolled){
                back_to_top.style.display = "block";
        } else {
                back_to_top.style.display = "none";
        }
};

/*function touching(){
        back_to_top.style.opacity = "1";
};

function away(){
        back_to_top.style.opacity = ".5";
}*/
