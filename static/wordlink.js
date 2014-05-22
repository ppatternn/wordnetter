//TODO: stop writing javascript! i know this is terrible :(
function on_load() {
    $(function() {
        $("#search").click(
            function(){
                get_data();
            }
        );
        $(".input").keyup(function(event){
            if(event.keyCode == 13){
                $("#search").click();
            }
        });
    });
}
function get_data(){
    $.when(
            $.ajax("/word/" + $("#word1").val()),
            $.ajax("/word/" + $("#word2").val())
        ).done(function(a1, a2){
            display_results(a1[0], a2[0]);
        });
}
//TODO: make this far less dumb!
function display_results(data1, data2) {
    $(".results").html("");
    $.each(data1.syns, function(k, v){
        $("#result1").append(display_word(data1.syns[k], is_match(data1.syns[k], data2.syns), "left"));
    });
    $.each(data2.syns, function(k, v){
        $("#result2").append(display_word(data2.syns[k], is_match(data2.syns[k], data1.syns), "right"));
    });
    $(".wordlink").click(
        function(){
            if (this.classList[1] == ("left"))
                $("#word1").val(this.innerHTML);
            else
                $("#word2").val(this.innerHTML);
            get_data();
        }
    );
}
function display_word(word, match, side){
    if (match == false)
        return "<div class='wordlink " + side + "'>" + word + "</div>"
    else
        return "<div style='color: limegreen' class='wordlink " + side + "'>" + word + "</div>"
}
function is_match(item, other_list) {
    if ($.inArray(item, other_list) > -1)
        return true;
    else
        return false;
}
