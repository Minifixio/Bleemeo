Dashing.widgets.Cpu = function (dashboard) {
    var self = this,
        widget;
    this.__init__ = Dashing.utils.widgetInit(dashboard, 'cpu');
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
