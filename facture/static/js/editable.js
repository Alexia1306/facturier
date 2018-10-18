$(document).ready(function() {
    $.fn.editable.defaults.mode = 'inline';
    $('.editable').editable();
    $('#commentaire').editable();
    $('#quantity').editable();
    $('#etat').editable({
    value: 2,
    source: [
          {value: 'REVIVE', text: 'A relancer'},
          {value: 'PAID', text: 'Payer'},
          {value: 'WAITING', text: 'En attente'}
       ]
});



$('#facture').editable({
value: 2,
source: [
      {value: 'True', text: 'vrai'},
      {value: 'False', text: 'Faux'},
   ]
});
});
