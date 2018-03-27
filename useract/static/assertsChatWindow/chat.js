var messages = []

$("#send").click(function () {
    val = $("#msgbox").val();

    messages.push(val);
    $(".ulclass").append(
                    '<li>'+
						'<div class="left-chat">'+
							'<img src="../../static/images/pic03.jpg">'+
							'<p>'+val+'<br>'+'<br>'+
							'</p>'+
							'<span>'+"2 min"+'</span>'+
						'</div>'+
					'</li>'

    );
    $("#msgbox").val("");
    doWork();
});

$("#sub").click(function () {
    val = $("#chat").val();
    $("#paragr").append(val);
});
$("#send").click(function () {
    $("#ptest").append(messages);
});

function doWork() {
	// ajax the JSON to the server
	$.post("/post/", messages, function(){

	});
	// stop link reloading the page
 event.preventDefault();
}
