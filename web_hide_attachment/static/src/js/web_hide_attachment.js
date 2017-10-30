odoo.define('web_hide_attachment.web_hide_attachment', function (require) {
	'use strict';
    var session = require('web.session');
    var sideWidget = require('web.Sidebar');

    var sidebar = sideWidget.include({
	redraw: function() {
            var self = this;
            this._super.apply(this, arguments);
            if (this.getParent() && session.uid != 1) {
                var view = this.getParent();
				this.$('.o_sidebar_add_attachment .o_form_binary_form').parent().parent().parent().parent().hide();
            }
        },
    });
});
