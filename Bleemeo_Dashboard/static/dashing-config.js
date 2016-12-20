var myDashboard = new Dashboard();
myDashboard.addWidget('cpu_widget', 'gauges', {
    getData: function () {
        var self = this;
        Dashing.utils.get('cpu_widget', function(data) {
            $.extend(self.scope, data);

        });
    },
    interval: 3000
});

myDashboard.addWidget('memory_widget', 'gauges', {
    getData: function () {
        var self = this;
        Dashing.utils.get('memory_widget', function(data) {
            $.extend(self.scope, data);

        });
    },
    interval: 3000
});

myDashboard.addWidget('meteo_widget', 'meteo', {
    getData: function () {
        var self = this;
        Dashing.utils.get('meteo_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: 3000
});

myDashboard.addWidget('load_widget', 'load', {
    getData: function () {
        var self = this;
        Dashing.utils.get('load_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: 3000
});
