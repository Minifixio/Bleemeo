var myDashboard = new Dashboard();
myDashboard.addWidget('cpu_widget', 'gauges', {
    getData: function () {
        var self = this;
        Dashing.utils.get('custom_widget', function(data) {
            $.extend(self.scope, data);

        });
    },
    interval: 3000
});

myDashboard.addWidget('meteo_widget', 'meteo', {
    getData: function () {
        var self = this;
        Dashing.utils.get('custom_widget3', function(data) {
            $.extend(self.scope, data);

        });
    },
    interval: 3000
});


myDashboard.addWidget('memory_widget', 'gauges', {
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
