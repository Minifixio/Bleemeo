Dashing.widgets.load = function (dashboard) {
    var self = this,
        widget;
    this.__init__ = Dashing.utils.widgetInit(dashboard, 'load',{
      require: ['load']
    });
    this.row = 1;
    this.col = 1;
    self.color = '#96bf48';
    this.scope = {};
    this.getWidget = function () {
        return this.___widget___;
    } ;
    this.getData = function () {};
    this.interval = 10000;

    /**function returnMinValue() {
      if (!data) return;
      return data.value.minValue;
    }**/

    //var minValue = data.value.minValue;
};
