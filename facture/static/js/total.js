$(document).ready(function () {
    // var $resultat = $(".resultat");
    // var $result =0;

    // $.each($resultat, function(index, value){
    //     $result = $result + parseInt(value.innerText);
    // });
    // $(".result").html($result);

    var array = [];
    $('.totaux').each(function(){
        array.push($(this).text());
    });

    console.log(array);
    var sum = 0;
    for (var i = 0; i < array.length; i++) {
        var number = parseInt(array[i]);
        sum += number;
    }

    $('.sum').append(sum);
});
