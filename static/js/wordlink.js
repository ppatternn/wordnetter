//TODO: stop writing javascript! i know this is terrible :(
var history = []

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
    var url = "";
    display_history($("#word1").val());
    display_history($("#word2").val());
    //var url = "http://127.0.0.1:5000";
    $.when(
            $.ajax(url + "/word/" + $("#word1").val()),
            $.ajax(url + "/word/" + $("#word2").val())
        ).done(function(a1, a2){
            //$("#raw").html(a1.toString());
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
            if (this.classList[1] == ("left")){
                $("#word1").val(this.innerHTML);
                $("#word1").focus();
            }
            else {
                $("#word2").val(this.innerHTML);
                $("#word2").focus();
            }
            //get_data();
        }
    );
    $(".history").click(
        function(){
            $("#word1").val(this.innerHTML);
            $("#word1").focus();
        }
    );
}
function display_history(word){
    if (is_match(word, history) == false)
        $("#history").append("<div class='history'>" + word + "</div>");
        history.push(word);
}
function display_word(word, match, side){
    if (match == false)
        return "<div class='wordlink " + side + "'>" + word + "</dvi>"
    else
        return "<div style='color: limegreen' class='wordlink " + side + "'>" + word + "</div>"
}
function is_match(item, other_list) {
    if ($.inArray(item, other_list) > -1)
        return true;
    else
        return false;
}
