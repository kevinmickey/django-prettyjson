(function($){
$( document ).ready(function() {
$('.parseraw').click(function(e){
  var widget = $(e.target).closest('.jsonwidget');
  var rawarea = widget.find('textarea');
  var parsedarea = widget.find('div.parsed');
  if ($(e.target).text() === 'Show parsed') {
    var validjson = true;
    try {
        JSON.parse(rawarea.val());
    } catch (e) {
      validjson = false;
    }
    if (validjson) {
      rawarea.hide();
      widget.find('.parsed').show()
      parsedarea.JSONView(rawarea.val(), {strict: true}).css({
        width: rawarea.css('width'),
        height: rawarea.css('height'),
        overflow: "auto",
        resize: "both"
      });
      $(e.target).text('Show raw');
    } else {
      // invalid json
      window.alert('Enter valid JSON.');
    }

  } else {
    // Clicked Show raw
    rawarea.val(JSON.stringify(JSON.parse(rawarea.val()),null,2));
    widget.find('textarea').show().css({
      width: parsedarea.css('width'),
      height: parsedarea.css('height')
    });
    widget.find('.parsed').hide();
    $(e.target).text('Show parsed');
  }
});
$('button.parsed').click(function(e){
  var widget = $(e.target).closest('.jsonwidget');
  var parsedarea = widget.find('div.parsed');
  if ($(e.target).text() === 'Collapse all') {
    parsedarea.JSONView('collapse');
  } else {
    parsedarea.JSONView('expand');
  }
});
});
})(jQuery);
