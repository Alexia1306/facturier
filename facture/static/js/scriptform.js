$(document).ready(function() {
            $(function () {
           $('#id_orders_table tbody tr').formset({
               // For inline formsets, be sure to set the prefix, as the default prefix
               // ('form') isn't correct.
               // Django appears to generate the prefix from the lowercase plural
               // name of the related model, with camel-case converted to underscores.
               prefix: 'ordered_items'
           })
       })
            });
