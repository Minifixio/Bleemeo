Dashing.widgets.Meteo = function (dashboard) {
    var self = this,
        widget;
    this.__init__ = Dashing.utils.widgetInit(dashboard, 'meteo',{
      require: ['meteoTask']
    });

    this.row = 1;
    this.col = 1;
    self.color = '#F00505';
    this.scope = {};
    this.getWidget = function () {
        return widget;
    };
    this.getData = function () {};
    this.interval = 10000;


};
