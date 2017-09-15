
// faire apparaitre disparaitre et apparaitre des elements par ID en ajoutant 
// onclick="toggle_visibility('id');"
// dans la définition de le l'objet html

function toggle_visibility(id) {
       var e = document.getElementById(id);
       if(e.style.display == 'block')
          e.style.display = 'none';
       else
          e.style.display = 'block';
    }


function toggle_opacity(id) {
       var e = document.getElementById(id);
       if(e.style.opacity < 1)
          e.style.opacity = 1;
       else
          e.style.opacity = 0.3;
    }


// fonction pour le menu principal

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

// fonction pour le menu vertical

$(document).scroll(function() {
    var y = $(this).scrollTop();
    if (y > 400) {
        $('div#signup-nav').removeClass('hide-nav');
      } else {
        $('div#signup-nav').addClass('hide-nav');
      }
    if (y > 1000) {
        $('a#gotop').removeClass('hide-gotop');
      } else {
        $('a#gotop').addClass('hide-gotop');

      }
});



