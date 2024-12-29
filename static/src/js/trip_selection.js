odoo.define('uber.trip_selection', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    publicWidget.registry.trip_selection = publicWidget.Widget.extend({
        selector: '.trip-selection-uber',
        xmlDepControllerendencies: ['/UberOdoo/views/trip_selection.xml'],
        events: {
            'input input[id=name]': '_validateAlphabetic',
        },

        init: function (parent, options) {
            this._super.apply(this, arguments);
            console.log("init")
        },

        _validateAlphabetic: function (ev) {
            console.log('ev', ev)
            let currentTarget = $(ev.currentTarget)[0];
            let newValue = currentTarget.value.replace(/[0-9_.,&%$#@!^*()+=;:"<>?/\\|]/g, '');
            currentTarget.value = newValue; 
        },
    });

});