odoo.define('rec_dev.remove_last_tr', function (require) {
    "use strict";

    var ListRenderer = require('web.ListRenderer');

    ListRenderer.include({
        _renderView: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                console.log('renderizando...');
                var rows = self.$('tbody tr');
                if (rows.length > 0) {
                    console.log('eliminando...');
                    rows.slice(-4).each(function() {
                        $(this).remove();
                    });
                }
            });
        },
    });
});