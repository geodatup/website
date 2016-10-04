
var $dropdownTriggers = $('.dropdown');
var $dropdownArea = $('.main-subnav');
var $dropdownZone = $('.hover-area');

$dropdownTriggers.each(function() {
  var $this = $(this);
  window.hoverintent(this, function() {
    $dropdownTriggers.removeClass('show');
    $('.subnav-group').removeClass('show');
    $dropdownArea.addClass('show');
    $('.subnav-' + $this.data('category')).addClass('show');
    $this.addClass('show');
  }, function() {
    if (!$dropdownZone.hasClass('hovered') && $('.dropdown:hover').length === 0) {
      $dropdownArea.removeClass('show');
      $dropdownTriggers.removeClass('show');
    }
  });
});

$dropdownZone.mouseover(function() {
  $(this).addClass('hovered');
  return false;
}).mouseleave(function() {
  $(this).removeClass('hovered');
  window.setTimeout(function() {
    if ($('.dropdown:hover').length === 0) {
      $dropdownArea.removeClass('show');
      $dropdownTriggers.removeClass('show');
    }
  }, 300);
});


$(document).scroll(function() {
    var y = $(this).scrollTop();
    if (y > 400) {
        $('div#signup-nav').removeClass('hide-nav');
      } else {
        $('div#signup-nav').addClass('hide-nav');
      }
});

  