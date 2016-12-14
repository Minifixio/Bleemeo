Dashing.widgets.Cpu = function (dashboard) {
    var self = this,
        widget;
    this.__init__ = Dashing.utils.widgetInit(dashboard, 'cpu',{
      require: ['gauge']
    });

    this.row = 2;
    this.col = 1;
    self.color = '#96bf48';
    this.scope = {};
    this.getWidget = function () {
        return widget;
    };
    this.getData = function () {};
    this.interval = 10000;


};

rivets.binders['dashing-gauge'] = function binder(el, data) {
    if (!el.init) {
        el.init = true;
        var gauge = createGauge(el, "CPU");
        el.gauge = gauge;
    }
    el.gauge.redraw(data);
};
