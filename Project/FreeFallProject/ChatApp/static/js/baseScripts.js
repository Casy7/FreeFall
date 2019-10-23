$(function() {
    var $window = $(window);
    var $sidebar = $(".sidebar");
    var $sidebarTop = $sidebar.position().top;
    var $sidebarHeight = $sidebar.height();
    var $footer = $('.footer');
    var $footerTop = $footer.position().top;
   
    $window.scroll(function(event) {
      $sidebar.addClass("fixed");
      var $scrollTop = $window.scrollTop();
      var $topPosition = Math.max(0, $sidebarTop - $scrollTop);
       
      if ($scrollTop + $sidebarHeight > $footerTop) {
        var $topPosition = Math.min($topPosition, $footerTop - $scrollTop - $sidebarHeight);
      }
   
      $sidebar.css("top", $topPosition);
    });
  });