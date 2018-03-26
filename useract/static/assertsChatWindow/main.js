$(document).ready(function(){
    	$( "#h4pb" ).on( "click", function() {
            $("#main").css("visibility","visible");
});
    });
//when the page is loading chat window is hidden
$(document).ready(function(){
    	$(".fa-minus").click(function(){
            $('.main-section').toggleClass("open-more");
        });
    });
//clicking on - toggle the chat window

$(document).ready(function(){
    	$(".fa-times").click(function(){
           $("#main").css("visibility","hidden");
        });
    });
//close the chat window

