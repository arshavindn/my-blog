var noPostLeft = false;

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$(document).ready(function() {
	var win = $(window);

	var csrftoken = getCookie('csrftoken');
	// Each time the user scrolls
	win.scroll(function() {
		// End of the document reached?
		if (win.scrollTop() == $(document).height() - win.height()) {
			if (!noPostLeft) {
				$.get("/", {'ajax_call': '1'}, function() {})
                .fail(function() {noPostLeft = true;})
                .success(function(html) {
                    $('div .md-col-6').append(html);
                });
			}
		}
	});
});
