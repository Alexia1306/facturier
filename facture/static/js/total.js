$(document).ready(function () {
    var $resultat = $(".resultat");
    var $resultat =0;

    $.each($resultat, function(index, value){
        $resultat = $resultat + parseInt(value.innerText);
    });
    $(".resultat").html($resultat);
});
