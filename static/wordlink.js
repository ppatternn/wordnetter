function on_load() {
    $(function() {
        $("#search").click(
            function(){
                var base = ""
                //var base = "http://127.0.0.1:5000"; //TODO: put the wordlink.py host here!
                $.when(
                        $.ajax(base + "/word/" + $("#word1").val()),
                        $.ajax(base + "/word/" + $("#word2").val())
                    ).done(function(a1, a2){
                        display_results(a1[0], a2[0]);
                    });
            }
        );
        $(".input").keyup(function(event){
            if(event.keyCode == 13){
                $("#search").click();
            }
        });
    });
}

//TODO: make this far less dumb!
function display_results(data1, data2) {
    $(".results").html("");
    $.each(data1.syns, function(k, v){
        if (is_match(data1.syns[k], data2.syns) == false){
            $("#result1").append("<div>" + data1.syns[k] + "</div>");
        } else {
            $("#result1").append("<div style='color: red'>" + data1.syns[k] + "</div>");
        }
    });
    $.each(data2.syns, function(k, v){
        if (is_match(data2.syns[k], data1.syns) == false){
            $("#result2").append("<div>" + data2.syns[k] + "</div>");
        } else {
            $("#result2").append("<div style='color: red'>" + data2.syns[k] + "</div>");
        }
    });
}
function is_match(item, other_list) {
    if ($.inArray(item, other_list) > -1)
        return true;
    else
        return false;
}
