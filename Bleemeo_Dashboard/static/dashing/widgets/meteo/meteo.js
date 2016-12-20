Dashing.widgets.meteo = function (dashboard) {
    var self = this,
        widget;
    this.__init__ = Dashing.utils.widgetInit(dashboard, 'meteo',{
      require: ['meteoTask']
    });
    this.row = 1;
    this.col = 2;
    self.color = '#96bf48';
    this.scope = {};
    this.getWidget = function () {
        return this.___widget___;
    } ;
    this.getData = function () {};
    this.interval = 10000;


};

//Settings images.
rivets.binders['meteo-img1'] = function binder(el, data) {
    if (!data) return;
    $(el).attr("src",data.tempImg.img1);
};
rivets.binders['meteo-img2'] = function binder(el, data) {
    if (!data) return;
    $(el).attr("src",data.tempImg.img2);
};
rivets.binders['meteo-img3'] = function binder(el, data) {
    if (!data) return;
    $(el).attr("src",data.tempImg.img3);
};
