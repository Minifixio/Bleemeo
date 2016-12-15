Dashing.widgets.gauges = function (dashboard) {
    var self = this,
        widget;
    this.__init__ = Dashing.utils.widgetInit(dashboard, 'gauges',{
      require: ['gauge']
    });

    this.row = 1;
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
    if (!data) return;
    if (!el.init) {
        el.init = true;
        var gauge = createGauge(el, data.title);
        el.gauge = gauge;
    }
    el.gauge.redraw(data);
    console.log(data);
};
