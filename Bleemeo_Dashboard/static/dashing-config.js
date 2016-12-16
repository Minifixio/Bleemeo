var myDashboard = new Dashboard();
myDashboard.addWidget('customWidget', 'gauges', {
    getData: function () {
        var self = this;
        Dashing.utils.get('custom_widget', function(data) {
            $.extend(self.scope, data);

        });
    },
    interval: 3000
});

myDashboard.addWidget('customWidget3', 'gauges', {
    getData: function () {
        var self = this;
        Dashing.utils.get('custom_widget3', function(data) {
            $.extend(self.scope, data);

        });
    },
    interval: 3000
});

myDashboard.addWidget('customWidget2', 'Meteo', {
    getData: function () {
        var self = this;
    },
    interval: 3000
});


/**myDashboard.addWidget('customWidget2', 'Memory', {
    getData: function () {
        var self = this;
        Dashing.utils.get('custom_widget', function(data) {
            $.extend(self.scope, data);

        });
    },
    interval: 3000
});**/
